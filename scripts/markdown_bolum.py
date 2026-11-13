"""Markdown taslağında seçilen bölümün çevresindeki metni koru."""

import re
from dataclasses import dataclass

ATX = re.compile(r" {0,3}(#{1,6})(?:[ \t]+(.*)|$)")
SETEXT = re.compile(r" {0,3}(=+|-+)[ \t]*")
CIT = re.compile(r" {0,3}(`{3,}|~{3,})(.*)")
BLOK_BASLANGICI = re.compile(r" {0,3}(?:[><]|[-+*][ \t]|\d+[.)][ \t]|$)| {4}|\t")
YATAY_CIZGI = re.compile(r" {0,3}(?:(?:-[ \t]*){3,}|(?:\*[ \t]*){3,}|(?:_[ \t]*){3,})")


def basliklari_bul(satirlar: list[str]) -> tuple[list[tuple[int, int, int, str]], bool]:
    """Başlıkların satır aralığını, seviyesini ve metnini döndür."""
    basliklar = []
    acik_cit = ""
    paragraf = []
    for sira, ham in enumerate(satirlar):
        satir = ham.rstrip("\r\n")
        if sira == 0:
            satir = satir.removeprefix("\ufeff")
        cit = CIT.fullmatch(satir)
        if acik_cit:
            if (cit and cit[1][0] == acik_cit[0] and len(cit[1]) >= len(acik_cit)
                    and not cit[2].strip()):
                acik_cit = ""
            continue
        if cit and (cit[1][0] == "~" or "`" not in cit[2]):
            acik_cit = cit[1]
            paragraf.clear()
            continue
        atx = ATX.fullmatch(satir)
        setext = SETEXT.fullmatch(satir)
        if atx:
            ad = re.sub(r"(?:^|[ \t]+)#+[ \t]*$", "", (atx[2] or "").strip())
            basliklar.append((sira, sira + 1, len(atx[1]), ad))
            paragraf.clear()
        elif setext and paragraf:
            ad = " ".join(paragraf)
            basliklar.append((sira - len(paragraf), sira + 1, 1 if setext[1][0] == "=" else 2, ad))
            paragraf.clear()
        elif BLOK_BASLANGICI.match(satir) or YATAY_CIZGI.fullmatch(satir):
            paragraf.clear()
        else:
            paragraf.append(satir.strip())
    return basliklar, bool(acik_cit)


@dataclass(frozen=True)
class Bolum:
    baslik: str
    seviye: int
    govde: str
    oncesi: str
    sonrasi: str
    satir_sonu: str
    onceki_baglam: str
    sonraki_baglam: str

    def birlestir(self, govde: str) -> str:
        basliklar, acik_cit = basliklari_bul(govde.splitlines())
        if acik_cit or any(seviye <= self.seviye for _, _, seviye, _ in basliklar):
            raise ValueError("Düzenlenen gövde yeni bir üst başlık veya açık kod bloğu içeriyor.")
        yeni = govde.strip("\r\n").replace("\r\n", "\n").replace("\r", "\n")
        return self.oncesi + yeni.replace("\n", self.satir_sonu) + self.sonrasi


def bolumu_sec(taslak: str, baslik: str) -> Bolum:
    satirlar = taslak.splitlines(keepends=True)
    basliklar, _ = basliklari_bul(satirlar)
    eslesenler = [i for i, (_, _, _, ad) in enumerate(basliklar) if ad == baslik.strip()]
    if not eslesenler:
        raise ValueError(f"Markdown taslağında “{baslik}” başlığı bulunamadı.")
    if len(eslesenler) > 1:
        raise ValueError(f"Markdown taslağında “{baslik}” başlığı birden fazla yerde geçiyor.")
    sira = eslesenler[0]
    baslik_ilk, ilk, seviye, ad = basliklar[sira]
    sonraki_sira = next((i for i in range(sira + 1, len(basliklar))
                         if basliklar[i][2] <= seviye), len(basliklar))
    son = len(satirlar)
    sonraki = ""
    if sonraki_sira < len(basliklar):
        son, sonraki_govde, _, _ = basliklar[sonraki_sira]
        govde_sonu = (basliklar[sonraki_sira + 1][0]
                      if sonraki_sira + 1 < len(basliklar) else len(satirlar))
        baslik_metni = "".join(satirlar[son:sonraki_govde]).strip()
        ilk_paragraf = re.split(r"\r?\n[ \t]*\r?\n", "".join(satirlar[sonraki_govde:govde_sonu]).strip(),
                                maxsplit=1)[0]
        sonraki = f"{baslik_metni}\n\n{ilk_paragraf}" if ilk_paragraf else baslik_metni
    while ilk < son and not satirlar[ilk].strip():
        ilk += 1
    while son > ilk and not satirlar[son - 1].strip():
        son -= 1
    if ilk == son:
        raise ValueError(f"“{baslik}” bölümünün gövdesi boş.")

    ham_govde = "".join(satirlar[ilk:son])
    govde = ham_govde.rstrip("\r\n")
    satir_sonu = "\r\n" if satirlar[ilk].endswith("\r\n") else "\n"
    onceki = re.split(r"\r?\n[ \t]*\r?\n", "".join(satirlar[:baslik_ilk]).strip())[-1]
    return Bolum(ad, seviye, govde, "".join(satirlar[:ilk]),
                 ham_govde[len(govde):] + "".join(satirlar[son:]), satir_sonu, onceki, sonraki)
