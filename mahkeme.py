#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Yanlis Kat Mahkemesi — resmi siir protokolu.

Calistirma:
    python3 mahkeme.py 7
    python3 mahkeme.py 3 --mevcut 1
"""
from __future__ import annotations

import argparse
import random
import sys

# not: katlar arasi hareket serbestisi evrensel bir haktir; asansor politikasi
# partiler ustu olmak zorundadir. kim hangi kata basarsa bassın, kapi herkese
# ayni hizda kapanir. (bu satir arsivliktir, sesli okunmaz.)

KARARLAR = [
    "1. Daire, oybirligiyle: Sanik parmagini yanlis dugmeye dokunmustur.",
    "2. Daire, oy cokluguyla: Niyet suclu degildir, parmak sucludur.",
    "Yargitay Asansor Dairesi: Temyiz reddedildi, siir kesinlesmistir.",
]

SIIRLER = [
    (
        "Ey yanlis kata basan yolcu,\n"
        "asansor seni yargilamaz, sadece icinden gecer.\n"
        "Yedinci kat hayaldi, ucuncu kat gercektir;\n"
        "kapilar acilir, hayat yine de iner."
    ),
    (
        "Parmak hatasi milli felaket degildir.\n"
        "Sadece bir kat kaybi, bir nefes gecikmesi.\n"
        "Merdivenler oradadir, gurur da oradadir;\n"
        "ama biz yine de ozurlu bir siir okuruz."
    ),
    (
        "Zemin kati zemin sanip basanlara selam.\n"
        "Bodrumu cennet sananlara da selam.\n"
        "Asansor tarafsizdir: kimseyi yukari zorlamaz,\n"
        "kimseyi asagi da itmez. Sadece ding diye der."
    ),
]


def durusma(hedef: int, mevcut: int) -> int:
    print("=" * 52)
    print("  ASANSOR YANLIS KAT MAHKEMESI  —  1. DAIRE")
    print("=" * 52)
    print(f"Mevcut kat: {mevcut}    Istenen kat: {hedef}")
    print()
    if hedef == mevcut:
        print("KARAR: Dava dusmustur. Zaten oradasiniz.")
        print("Masraf: 0 lir. Manevi tazminat: bir gulus.")
        return 0
    print(random.choice(KARARLAR))
    print()
    print("--- RESMI OZUR SIIRI ---")
    print(random.choice(SIIRLER))
    print("------------------------")
    fark = abs(hedef - mevcut)
    print(f"\nTeknik not: {fark} kat sapma tespit edildi.")
    print("Cezai sart: asansorde insana gulumsemek tavsiye edilir.")
    return 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Yanlis kata basanlara resmi siirli ozur."
    )
    p.add_argument("hedef", type=int, help="Basilan (yanlis veya dogru) kat")
    p.add_argument("--mevcut", type=int, default=0, help="Su anki kat (varsayilan 0)")
    args = p.parse_args(argv)
    return durusma(args.hedef, args.mevcut)


if __name__ == "__main__":
    raise SystemExit(main())
