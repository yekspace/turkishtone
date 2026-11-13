"""TurkishTone için ortak Responses API ve yazım talimatları."""

import json
import re
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from govde_dogrula import olc
from kelime_say import kelime_say
from kaynak_kontrolu import bulgulari_kontrol_et, denetim_istegi

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = "https://api.openai.com/v1/responses"
TURLER = ("Haber", "Rehber", "Ürün içeriği")
REHBER_BASLIKLARI = {
    "Makale": "Makale",
    "Duygusal içerik": "Duygusal ve kişisel içerik",
    "Yerelleştirme": "Yerelleştirme",
    "Seslendirme": "Seslendirme metni",
    "Diyalog": "Diyalog",
    "Sosyal medya": "Sosyal medya",
    "Konuşma metni": "Konuşma metni",
    "Reklam metni": "Reklam metni",
    "Kampanya yazısı": "Kampanya yazısı",
    "Basın bülteni": "Basın bülteni",
}
ALANLAR = ("baslik", "govde", "editor_notu")
FORMAT = {
    "type": "json_schema",
    "name": "turkce_icerik",
    "strict": True,
    "schema": {
        "type": "object",
        "properties": {
            "baslik": {"type": "string", "description": "Yayın başlığı."},
            "govde": {"type": "string", "description": "Görünür gövde metni."},
            "editor_notu": {
                "type": "string",
                "description": "Brief izin veriyorsa editör notu. Yoksa boş metin.",
            },
        },
        "required": list(ALANLAR),
        "additionalProperties": False,
    },
}


def oku(dosya: Path) -> str:
    return dosya.read_text(encoding="utf-8-sig").strip()


def talimatlari_oku(tur: str | None = None, soz_varligi: bool = False,
                    *, uslup_profili: bool = False, dil_bilgisi: bool = False,
                    eski: bool = False) -> str:
    parcalar = re.split(r"(?m)^---\s*$", oku(ROOT / "SKILL.md"), maxsplit=2)
    if len(parcalar) != 3:
        raise ValueError("SKILL.md YAML üst bilgisi bulunamadı.")
    referans = ROOT / "references"
    if tur in REHBER_BASLIKLARI:
        bolumler = re.split(r"(?m)^## ([^\n]+)\n", oku(referans / "icerik-turleri.md"))
        rehber = dict(zip(bolumler[1::2], bolumler[2::2]))
        baslik = REHBER_BASLIKLARI[tur]
        yayin = "\n\n".join([bolumler[0].strip(), f"## {baslik}\n{rehber[baslik].strip()}",
                              f"## Son okuma\n{rehber['Son okuma'].strip()}"])
    elif tur in TURLER:
        yayin = oku(referans / "yayin-rehberi.md")
    else:
        yayin = None
    cekirdek = oku(ROOT / "evals" / "eski-skill.md") if eski else parcalar[2].strip()
    talimatlar = [cekirdek]
    if dil_bilgisi:
        talimatlar.append(oku(referans / "cumle-baglac-soru.md"))
        talimatlar.append(oku(referans / "anlam-ve-anlatim.md"))
    if yayin:
        talimatlar.append(yayin)
    if soz_varligi:
        talimatlar.append(oku(referans / "soz-varligi.md"))
    if uslup_profili:
        talimatlar.append(oku(referans / "uslup-profilleri.md"))
    return "\n\n".join(talimatlar)


def istek_verisi(model: str, brief: str, talimat: str | None) -> dict:
    veri = {
        "model": model,
        "input": brief,
        "text": {"format": FORMAT},
        "max_output_tokens": 2500,
        "store": False,
    }
    if talimat is not None:
        veri["instructions"] = talimat
    return veri


def yanit_jsonunu_oku(yanit: dict) -> dict:
    if yanit.get("status") != "completed":
        neden = (yanit.get("incomplete_details") or {}).get("reason", "bilinmiyor")
        raise ValueError(f"API yanıtı tamamlanmadı ({yanit.get('status')}, {neden}).")
    parcalar = [
        parca
        for oge in yanit.get("output", [])
        if oge.get("type") == "message"
        for parca in oge.get("content", [])
    ]
    if any(parca.get("type") == "refusal" for parca in parcalar):
        raise ValueError("Model brief için metin üretmeyi reddetti.")
    return json.loads("".join(
        parca["text"] for parca in parcalar if parca.get("type") == "output_text"
    ))


def yaniti_oku(yanit: dict) -> dict:
    cikti = yanit_jsonunu_oku(yanit)
    if (not isinstance(cikti, dict) or set(cikti) != set(ALANLAR)
            or any(not isinstance(cikti[alan], str) for alan in ALANLAR)
            or not cikti["baslik"].strip() or not cikti["govde"].strip()):
        raise ValueError("API çıktısında geçerli başlık, gövde ve editör notu alanları bekleniyor.")
    return cikti


def api_cagir(anahtar: str, veri: dict) -> dict:
    istek = Request(
        ENDPOINT,
        method="POST",
        data=json.dumps(veri, ensure_ascii=False).encode("utf-8"),
        headers={"Authorization": f"Bearer {anahtar}", "Content-Type": "application/json"},
    )
    try:
        with urlopen(istek, timeout=120) as yanit:
            return json.load(yanit)
    except HTTPError as exc:
        # Hata metni kimlik bilgisi içerebilir. Yalnızca bilinen kodları göster.
        try:
            ayrinti = (json.load(exc).get("error") or {})
            kod = ayrinti.get("code") or ayrinti.get("type")
        except (AttributeError, ValueError, OSError):
            kod = None
        bilinen_kodlar = (
            "insufficient_quota", "rate_limit_exceeded", "model_not_found",
            "invalid_api_key", "billing_hard_limit_reached", "credit_balance_exhausted",
        )
        ek = f" ({kod})" if kod in bilinen_kodlar else ""
        bekleme = exc.headers.get("Retry-After", "")
        if re.fullmatch(r"[0-9]{1,6}", bekleme):
            ek += f" Yeniden denemeden önce {bekleme} saniye bekleyin."
        raise RuntimeError(f"OpenAI API HTTP {exc.code} döndürdü{ek}.") from None
    except (URLError, TimeoutError) as exc:
        raise RuntimeError(f"OpenAI API bağlantısı kurulamadı veya kesildi ({type(exc).__name__}).") from None


def kaydet_yaniti(yanit: dict, brief: dict) -> dict:
    cikti = yaniti_oku(yanit)
    alt, ust = brief["alt"], brief["ust"]
    olcum = (olc(cikti["govde"], alt, ust) if alt is not None and ust is not None
             else {"kelime": kelime_say(cikti["govde"]), "aralikta": None})
    return {
        "yanit_id": yanit.get("id"),
        "model": yanit.get("model"),
        "kullanim": yanit.get("usage"),
        **olcum,
        "cikti": cikti,
    }


def api_ile_iletisim(anahtar: str, veri: dict, kota_tekrar: int) -> dict:
    for deneme in range(kota_tekrar + 1):
        try:
            return api_cagir(anahtar, veri)
        except RuntimeError as exc:
            if deneme == kota_tekrar or "credit_balance_exhausted" not in str(exc):
                raise
            print(f"Bakiye hatası. Aynı aşama yeniden denenecek ({deneme + 1}/{kota_tekrar}).", flush=True)
            time.sleep(8)


def api_yaniti_al(anahtar: str, veri: dict, brief: dict, kota_tekrar: int) -> dict:
    return kaydet_yaniti(api_ile_iletisim(anahtar, veri, kota_tekrar), brief)


def kaynagi_denetle(anahtar: str, model: str, brief: str, cikti: dict,
                    kota_tekrar: int, caba: str | None = None) -> dict:
    yanit = api_ile_iletisim(anahtar, denetim_istegi(model, brief, cikti, caba), kota_tekrar)
    return {
        "yanit_id": yanit.get("id"),
        "model": yanit.get("model"),
        "kullanim": yanit.get("usage"),
        "bulgular": bulgulari_kontrol_et(yanit_jsonunu_oku(yanit), brief, cikti),
    }
