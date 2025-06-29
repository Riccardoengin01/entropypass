#!/usr/bin/env python3
"""
EntropyPass v0.1 - by Riccardo Righini
Generatore di password sicure + calcolo entropia
License: MIT
"""

import secrets
import string
import math
import argparse

ALPHABET = {
    "lower": string.ascii_lowercase,
    "upper": string.ascii_uppercase,
    "digits": string.digits,
    "symbols": "!@#$%&*?"
}

def build_charset(use_upper: bool, use_digits: bool, use_symbols: bool) -> str:
    charset = ALPHABET["lower"]
    if use_upper:
        charset += ALPHABET["upper"]
    if use_digits:
        charset += ALPHABET["digits"]
    if use_symbols:
        charset += ALPHABET["symbols"]
    return charset

def generate_pwd(length: int, charset: str) -> str:
    return ''.join(secrets.choice(charset) for _ in range(length))

def entropy(bits: int, charset_len: int) -> float:
    return math.log2(charset_len) * bits

def main():
    parser = argparse.ArgumentParser(description="Genera password ad alta entropia")
    parser.add_argument("-l", "--length", type=int, default=16, help="lunghezza password (default 16)")
    parser.add_argument("--no-upper", action="store_true", help="escludi MAIUSCOLE")
    parser.add_argument("--no-digits", action="store_true", help="escludi cifre")
    parser.add_argument("--no-symbols", action="store_true", help="escludi simboli")
    args = parser.parse_args()

    charset = build_charset(not args.no_upper, not args.no_digits, not args.no_symbols)
    pwd = generate_pwd(args.length, charset)
    ent = entropy(args.length, len(charset))

    print(f"\n🔐  Password: {pwd}")
    print(f"🧮  Entropia stimata: {ent:.1f} bit\n")

if __name__ == "__main__":
    main()
