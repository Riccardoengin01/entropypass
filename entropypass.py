#!/usr/bin/env python3
"""
EntropyPass v0.3 — by Riccardo Righini
Generatore di password sicure + calcolo entropia
License: MIT
"""

import secrets
import string
import math
import argparse
import sys

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

def entropy(length: int, charset_len: int) -> float:
    """Stima stile Shannon: lunghezza × log2(|charset|)"""
    return round(length * math.log2(charset_len), 1)

def ask_length(min_len: int = 8, max_len: int = 64, default_len: int = 16) -> int:
    """Chiede all'utente la lunghezza della password. ENTER = default."""
    while True:
        response = input(f"Quanti caratteri? ({min_len}–{max_len}) [default {default_len}]: ").strip()
        if response == "":
            return default_len
        try:
            val = int(response)
            if min_len <= val <= max_len:
                return val
            else:
                print(f"❌  Inserisci un numero tra {min_len} e {max_len}.")
        except ValueError:
            print("❌  Solo numeri o ENTER per usare il default.")

def main():
    parser = argparse.ArgumentParser(description="EntropyPass — genera password ad alta entropia")
    parser.add_argument("--no-upper", action="store_true", help="escludi MAIUSCOLE")
    parser.add_argument("--no-digits", action="store_true", help="escludi cifre")
    parser.add_argument("--no-symbols", action="store_true", help="escludi simboli")
    args = parser.parse_args()

    length = ask_length()

    charset = build_charset(
        not args.no_upper,
        not args.no_digits,
        not args.no_symbols,
    )

    pwd = generate_pwd(length, charset)
    ent = entropy(length, len(charset))

    print("\n🔐  Password:", pwd)
    print(f"🧮  Entropia stimata: {ent} bit "
          f"(len={length}, charset={len(charset)} caratteri)\n")

if __name__ == "__main__":
    main()
