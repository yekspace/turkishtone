"""Canlı karşılaştırmadan koşul adları gizlenmiş editör dosyası üret."""

import argparse
import json
import random
from pathlib import Path


def hazirla(kosu: dict) -> tuple[str, dict]:
    briefler = kosu["briefler"]
    sonuclar = kosu["sonuclar"]
    kosullar = set(kosu.get("kosullar", ("skillsiz", "skill-li")))
    if (not kosu["tamamlandi"] or not 2 <= len(kosullar) <= 26
            or len(sonuclar) != len(kosullar) * len(briefler)):
        raise ValueError("Kör değerlendirme için her brief'in tüm son metinleri gerekli.")
    satirlar = [
        "# Kör editör değerlendirmesi", "",
        "Her metni kendi brief’iyle değerlendir. Harflerin sırası brief’e göre değişebilir.",
        "Her metne aşağıdaki dört ölçütte 0–2 puan ver. 0 belirgin sorun, "
        "1 kısmen başarılı, 2 başarılı anlamına gelir.", "",
        "- Kaynak sadakati. Olgular, koşullar ve kesinlik korunmuş mu?",
        "- Üslup uyumu. Hitap, resmiyet ve sözcük seçimi brief’e uyuyor mu?",
        "- Doğallık. Türkçe akıcı mı, cümleler yerinde mi, gereksiz tekrar var mı?",
        "- Mecra ve amaç. Metin yapılacak işi, çağrıyı veya duyuruyu türüne uygun veriyor mu?",
        "",
        "Uzunluk ayrıca ölçüleceği için kelime sayısını bu dört puana katma. "
        "Her türde bütün metinlerin puanlarını, tercih veya beraberlik kararını ve "
        "her metinden bir somut örneği yaz.",
    ]
    anahtar = {}
    for tur, brief in briefler.items():
        cift = [sonuc for sonuc in sonuclar if sonuc["tur"] == tur]
        if len(cift) != len(kosullar) or {s["kosul"] for s in cift} != kosullar:
            raise ValueError(f"{tur} için her koşuldan bir sonuç gerekli.")
        random.SystemRandom().shuffle(cift)
        anahtar[tur] = {}
        satirlar.extend(["", f"## {tur}", "", "### Brief", "", brief["input"]])
        for i, sonuc in enumerate(cift):
            harf = chr(ord("A") + i)
            anahtar[tur][harf] = sonuc["kosul"]
            cikti = sonuc["cikti"]
            satirlar.extend(["", f"### Metin {harf}", "", f"**{cikti['baslik']}**",
                             "", cikti["govde"]])
            if cikti["editor_notu"]:
                satirlar.extend(["", "**Editör notu**", "", cikti["editor_notu"]])
    return "\n".join(satirlar) + "\n", anahtar


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sonuclar", type=Path)
    parser.add_argument("--metin", type=Path, required=True)
    parser.add_argument("--anahtar", type=Path, required=True)
    args = parser.parse_args()
    if args.metin.resolve() == args.anahtar.resolve():
        parser.error("Metin ve koşul anahtarı için ayrı dosyalar seç.")
    if args.metin.exists() or args.anahtar.exists():
        parser.error("Çıktılar için yeni dosya adları seç.")
    kosu = json.loads(args.sonuclar.read_text(encoding="utf-8"))
    metin, anahtar = hazirla(kosu)
    with args.metin.open("x", encoding="utf-8") as dosya:
        dosya.write(metin)
    with args.anahtar.open("x", encoding="utf-8") as dosya:
        json.dump(anahtar, dosya, ensure_ascii=False, indent=2)
        dosya.write("\n")


if __name__ == "__main__":
    main()
