"""Aynı brief'leri Responses API'de skill'li ve skillsiz çalıştır."""

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from editor_api import (TURLER, api_ile_iletisim, api_yaniti_al, istek_verisi, kaynagi_denetle,
                        oku, talimatlari_oku, yanit_jsonunu_oku, yaniti_oku)
from govde_dogrula import duzeltme_girdisi

YENI_TURLER = ("Makale", "Duygusal içerik", "Seslendirme", "Sosyal medya")
USLUP_TURLERI = ("Konuşma metni", "Reklam metni", "Kampanya yazısı", "Basın bülteni")
def briefleri_oku(yeni: bool = False, *, uslup: bool = False) -> dict:
    if uslup:
        dosya, beklenen = "uslup-briefleri.md", USLUP_TURLERI
    elif yeni:
        dosya, beklenen = "yeni-tur-briefleri.md", YENI_TURLER
    else:
        dosya, beklenen = "briefler.md", TURLER
    bolumler = re.split(r"(?m)^## ([^\n]+)\n", oku(ROOT / "evals" / dosya))
    briefler = dict(zip(bolumler[1::2], bolumler[2::2]))
    if tuple(briefler) != beklenen:
        raise ValueError(f"Brief başlıkları beklenen sırada olmalı: {', '.join(beklenen)}.")
    sonuc = {}
    for tur, metin in briefler.items():
        aralik = re.search(r"(\d+)[–-](\d+) kelimelik", metin)
        if not aralik:
            raise ValueError(f"{tur} brief'inde kelime aralığı bulunamadı.")
        alt, ust = map(int, aralik.groups())
        if alt > ust:
            raise ValueError(f"{tur} brief'inde kelime aralığı geçersiz.")
        sonuc[tur] = {
            "input": "Yalnızca brief’teki bilgileri kullan.\n\n" + metin.strip(),
            "alt": alt,
            "ust": ust,
        }
    return sonuc


def duzeltme_istegi(model: str, brief: dict, ilk: dict, talimat: str | None,
                     caba: str | None = None) -> dict:
    alt, ust, sayi = brief["alt"], brief["ust"], ilk["kelime"]
    girdi = duzeltme_girdisi(brief["input"], ilk["cikti"], alt, ust, sayi)
    if caba:
        olcum = (f"alt sınırdan {alt - sayi} kelime kısa" if sayi < alt
                 else f"üst sınırdan {sayi - ust} kelime uzun")
        girdi = (
            f"Önceki gövde {olcum}. "
            "Önce brief'teki bağımsız bilgi birimlerini belirle. Gövdeyi bunların "
            "etrafında yeniden kur. Her cümlenin kelimelerini ayrı ayrı say, "
            "gövdenin toplamını kontrol et ve sadece son metni döndür.\n\n"
            + girdi
        )
    istek = istek_verisi(model, girdi, talimat)
    if caba:
        istek["reasoning"] = {"effort": caba}
    return istek


def json_yaz(dosya: Path, veri: dict) -> None:
    with dosya.open("x", encoding="utf-8") as hedef:
        json.dump(veri, hedef, ensure_ascii=False, indent=2)
        hedef.write("\n")


def rapor_yaz(dosya: Path, kosu: dict) -> None:
    satirlar = [
        "# Responses API karşılaştırması", "",
        f"Model isteği: `{kosu['model']}`", "",
        f"Tamamlanan içerik sayısı: {len(kosu['sonuclar'])}/{len(kosu.get('kosullar', ('skillsiz', 'skill-li'))) * len(kosu['briefler'])}", "",
        "| Tür | Koşul | İlk gövde | Son gövde | Hedef | Son durum |",
        "|---|---|---:|---:|---:|---|",
    ]
    for sonuc in kosu["sonuclar"]:
        tur, kosul = sonuc["tur"], sonuc["kosul"]
        brief = kosu["briefler"][tur]
        durum = "Aralıkta" if sonuc["aralikta"] else "Sınır dışında"
        satirlar.append(
            f"| {tur} | {kosul} | {sonuc.get('ilk_taslak', sonuc)['kelime']} | {sonuc['kelime']} | "
            f"{brief['alt']}–{brief['ust']} | {durum} |"
        )
    for sonuc in kosu["sonuclar"]:
        satirlar += ["", f"## {sonuc['tur']} · {sonuc['kosul']}"]
        asamalar = [("İlk taslak", sonuc.get("ilk_taslak", sonuc))]
        if sonuc.get("duzeltildi"):
            asamalar.append(("Düzeltilen taslak", sonuc))
        for asama, kayit in asamalar:
            cikti = kayit["cikti"]
            satirlar += ["", f"### {asama} · {kayit['kelime']} kelime", "",
                         f"**{cikti['baslik']}**", "", cikti["govde"]]
            if cikti["editor_notu"]:
                satirlar += ["", "**Editör notu**", "", cikti["editor_notu"]]
        if "kaynak_kontrolu" in sonuc:
            bulgular = sonuc["kaynak_kontrolu"]["bulgular"]
            satirlar += ["", "### Kaynak kontrolü"]
            if not bulgular:
                satirlar += ["", "Denetim çağrısı bulgu bildirmedi."]
            for bulgu in bulgular:
                odak = {
                    "etkinligin_gerceklesmesi": "etkinliğin gerçekleşmesi",
                    "baslangic_tarihi": "başlangıç tarihi",
                }.get(bulgu.get("odak"))
                etiket = f"{bulgu['kategori']} · {odak}" if odak else bulgu["kategori"]
                satirlar += ["", f"- **{etiket}** · {bulgu['aciklama']}"]
                for alan in ("kaynak_alintisi", "metin_alintisi"):
                    if bulgu[alan]:
                        satirlar.append(f"  - {alan.replace('_', ' ').capitalize()} · “{bulgu[alan]}”")
                if not bulgu["alinti_eslesti"]:
                    satirlar.append("  - Alıntı bire bir eşleşmedi. Editör doğrulaması gerekli.")
        if sonuc.get("editor_incelemesi"):
            nedenler = []
            if not sonuc["aralikta"]:
                nedenler.append("gövde uzunluğu")
            if sonuc.get("kaynak_kontrolu", {}).get("bulgular"):
                nedenler.append("kaynak bulgusu")
            satirlar += ["", f"**Editör incelemesi gerekiyor** · {', '.join(nedenler)}"]
    dosya.write_text("\n".join(satirlar) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="Structured Outputs destekleyen model kimliği.")
    parser.add_argument("--hazirlik", action="store_true", help="İlk istekleri oluşturur ve API'ye göndermez.")
    brief_grubu = parser.add_mutually_exclusive_group()
    brief_grubu.add_argument("--yeni-turler", action="store_true", help="Dört yeni türün brief'lerini kullan.")
    brief_grubu.add_argument("--uslup-turleri", action="store_true", help="Dört üslup brief'ini kullan.")
    brief_grubu.add_argument("--rehber-etkisi", action="store_true",
                             help="Aynı dört üslup brief'ini dört rehber koşulunda çalıştır.")
    brief_grubu.add_argument("--surum-karsilastirmasi", action="store_true",
                             help="Eski sürümü, sade çekirdeği ve skillsiz koşulu karşılaştır.")
    brief_grubu.add_argument("--sade-karsilastirmasi", action="store_true",
                             help="Önceki ve güncel sade sürümü aynı dört brief ile karşılaştır.")
    parser.add_argument("--kaynak-kontrolu", action="store_true", help="Her son metni ayrı API çağrısıyla denetle.")
    parser.add_argument("--denetim-caba", choices=("low", "medium", "high"),
                        help="Destekleyen modellerde yalnızca kaynak denetiminin akıl yürütme düzeyi.")
    parser.add_argument("--duzeltme-caba", choices=("low", "medium", "high"),
                        help="Destekleyen modellerde kelime açığına odaklanan düzeltmenin akıl yürütme düzeyi.")
    parser.add_argument("--kota-tekrar", type=int, choices=range(5), default=0,
                        help="Aralıklı bakiye hatasında aynı aşama için ek bağlantı denemeleri.")
    args = parser.parse_args()
    if args.denetim_caba and not args.kaynak_kontrolu:
        parser.error("--denetim-caba için --kaynak-kontrolu gerekir.")
    if args.sade_karsilastirmasi:
        briefler = briefleri_oku(uslup=True)
        onceki = json.loads(oku(ROOT / "evals" / "onceki-sade-talimatlar.json"))
        if set(onceki) != set(briefler):
            raise ValueError("Arşivlenmiş talimatlar dört üslup brief'iyle eşleşmeli.")
        kosul_talimatlari = {
            tur: {"onceki_sade": onceki[tur], "guncel_sade": talimatlari_oku(tur)}
            for tur in briefler
        }
    elif args.surum_karsilastirmasi:
        briefler = briefleri_oku(uslup=True)
        kosul_talimatlari = {
            tur: {
                "eski_surume_gore": talimatlari_oku(tur, soz_varligi=True, uslup_profili=True,
                                                    dil_bilgisi=True, eski=True),
                "sade_cekirdek": talimatlari_oku(tur),
                "skillsiz": None,
            }
            for tur in briefler
        }
    elif args.rehber_etkisi:
        briefler = briefleri_oku(uslup=True)
        ekler = {
            "cekirdek": (False, False),
            "uslup": (True, False),
            "soz_varligi": (False, True),
            "iki_rehber": (True, True),
        }
        kosul_talimatlari = {
            tur: {ad: talimatlari_oku(tur, soz_varligi=soz, uslup_profili=uslup,
                                     dil_bilgisi=False)
                  for ad, (uslup, soz) in ekler.items()}
            for tur in briefler
        }
    elif args.uslup_turleri:
        briefler = briefleri_oku(uslup=True)
        talimatlar = {tur: talimatlari_oku(tur, soz_varligi=True, uslup_profili=True)
                      for tur in briefler}
    elif args.yeni_turler:
        briefler = briefleri_oku(True)
        talimatlar = {tur: talimatlari_oku(tur) for tur in briefler}
    else:
        briefler = briefleri_oku()
        talimatlar = dict.fromkeys(briefler, talimatlari_oku("Haber"))
    if not (args.rehber_etkisi or args.surum_karsilastirmasi or args.sade_karsilastirmasi):
        kosul_talimatlari = {tur: {"skillsiz": None, "skill-li": talimat}
                             for tur, talimat in talimatlar.items()}
    kosullar = list(next(iter(kosul_talimatlari.values())))
    istekler = [
        (tur, kosul, istek_verisi(args.model, brief["input"], ek))
        for tur, brief in briefler.items()
        for kosul, ek in kosul_talimatlari[tur].items()
    ]
    if args.hazirlik:
        print(f"{len(istekler)} istek hazır. Canlı API çağrısı yapılmadı.")
        return 0

    anahtar = os.environ.get("OPENAI_API_KEY", "").strip()
    if not anahtar:
        parser.exit(2, "OPENAI_API_KEY bulunamadı. Ortam değişkenini ayarlayıp tekrar çalıştırın.\n")

    baslangic = datetime.now(timezone.utc)
    kosu_dizini = ROOT / "evals" / "runs" / baslangic.strftime("%Y%m%dT%H%M%S%fZ")
    kosu_dizini.mkdir(parents=True, exist_ok=False)
    kosu = {
        "model": args.model,
        "baslangic_utc": baslangic.isoformat(),
        "talimat_sha256": ({
            tur: {ad: hashlib.sha256(talimat.encode("utf-8")).hexdigest() if talimat else None
                  for ad, talimat in secenekler.items()}
            for tur, secenekler in kosul_talimatlari.items()
        } if args.rehber_etkisi or args.surum_karsilastirmasi or args.sade_karsilastirmasi else {
            tur: hashlib.sha256(talimat.encode("utf-8")).hexdigest()
            for tur, talimat in talimatlar.items()
        }),
        "kosullar": kosullar,
        "kaynak_kontrolu": args.kaynak_kontrolu,
        "denetim_caba": args.denetim_caba,
        "duzeltme_caba": args.duzeltme_caba,
        "briefler": briefler,
        "tamamlandi": False,
        "sonuclar": [],
    }
    sonuc_dosyasi = kosu_dizini / "sonuclar.json"
    json_yaz(kosu_dizini / "deney.json", kosu)
    print(f"Kayıt dizini: {kosu_dizini}", flush=True)
    for tur, kosul, veri in istekler:
        brief = briefler[tur]
        sira = len(kosu["sonuclar"]) + 1
        try:
            ilk = api_yaniti_al(anahtar, veri, brief, args.kota_tekrar)
            json_yaz(kosu_dizini / f"{sira:02d}-ilk.json", ilk)
            son = ilk
            if not ilk["aralikta"]:
                caba = (None if args.sade_karsilastirmasi and kosul == "onceki_sade"
                        else args.duzeltme_caba)
                duzeltme = duzeltme_istegi(args.model, brief, ilk, veri.get("instructions"), caba)
                son = api_yaniti_al(anahtar, duzeltme, brief, args.kota_tekrar)
                json_yaz(kosu_dizini / f"{sira:02d}-duzeltme.json", son)
            kontrol = None
            if args.kaynak_kontrolu:
                kontrol = kaynagi_denetle(anahtar, args.model, brief["input"],
                                          son["cikti"], args.kota_tekrar, args.denetim_caba)
        except (RuntimeError, ValueError) as exc:
            kosu["hata"] = {"tur": tur, "kosul": kosul, "mesaj": str(exc)}
            json_yaz(sonuc_dosyasi, kosu)
            rapor_yaz(kosu_dizini / "karsilastirma.md", kosu)
            print(f"{tur} / {kosul}: {exc}", file=sys.stderr)
            return 1
        sonuc = {
            "tur": tur,
            "kosul": kosul,
            **son,
            "ilk_taslak": ilk,
            "duzeltildi": son is not ilk,
            "editor_incelemesi": not son["aralikta"] or bool(kontrol and kontrol["bulgular"]),
        }
        if kontrol is not None:
            sonuc["kaynak_kontrolu"] = kontrol
        json_yaz(kosu_dizini / f"{len(kosu['sonuclar']) + 1:02d}.json", sonuc)
        kosu["sonuclar"].append(sonuc)
        print(f"{tur} / {kosul}: {ilk['kelime']} → {son['kelime']} kelime", flush=True)
    kosu["tamamlandi"] = True
    json_yaz(sonuc_dosyasi, kosu)
    rapor_yaz(kosu_dizini / "karsilastirma.md", kosu)
    return 0


if __name__ == "__main__":
    sys.exit(main())
