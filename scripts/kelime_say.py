"""Skill ve API karşılaştırması için aynı düz metin kelime ölçümü."""

import argparse
import sys
from pathlib import Path


def kelime_say(metin: str) -> int:
    """Boşlukla ayrılan ve harf veya onluk rakam içeren parçaları say."""
    return sum(any(harf.isalpha() or harf.isdecimal() for harf in parca)
               for parca in metin.split())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dosya", nargs="?", type=Path, help="UTF-8 dosya. Boşsa stdin.")
    parser.add_argument("--min", type=int, default=0, dest="alt")
    parser.add_argument("--max", type=int, dest="ust")
    args = parser.parse_args()
    if args.alt < 0 or (args.ust is not None and args.ust < args.alt):
        parser.error("Kelime aralığı geçersiz.")
    try:
        metin = (args.dosya.read_text(encoding="utf-8-sig") if args.dosya
                 else sys.stdin.buffer.read().decode("utf-8-sig"))
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Metin okunamadı: {exc}\n")
    sayi = kelime_say(metin)
    print(sayi)
    return int(sayi < args.alt or (args.ust is not None and sayi > args.ust))


if __name__ == "__main__":
    sys.exit(main())
