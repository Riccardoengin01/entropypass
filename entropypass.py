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
from typing import Final

# --- Configurazione ---
DEFAULT_LENGTH: Final[int] = 16
MIN_LENGTH: Final[int] = 8
MAX_LENGTH: Final[int] = 64

ALPHABET: Final[dict[str, str]] = {
    "lower": string.ascii_lowercase,
    "upper": string.ascii_uppercase,
    "digits": string.digits,
    "symbols": "!@#$%&*?_+-="  # Set di simboli "sicuri"
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

def ask_length() -> int:
    """Chiede all'utente la lunghezza della password. ENTER = default."""
    while True:
        response = input(f"Quanti caratteri? ({MIN_LENGTH}–{MAX_LENGTH}) [default {DEFAULT_LENGTH}]: ").strip()
        if response == "":
            return DEFAULT_LENGTH
        try:
            val = int(response)
            if MIN_LENGTH <= val <= MAX_LENGTH:
                return val
            else:
                print(f"❌  Inserisci un numero tra {MIN_LENGTH} e {MAX_LENGTH}.")
        except ValueError:
            print("❌  Solo numeri o ENTER per usare il default.")

def main():
    parser = argparse.ArgumentParser(description="EntropyPass — genera password ad alta entropia")
    parser.add_argument("--no-upper", action="store_true", help="escludi MAIUSCOLE")
    parser.add_argument("--no-digits", action="store_true", help="escludi cifre")
    parser.add_argument("--no-symbols", action="store_true", help="escludi simboli")
    parser.add_argument(
        "length",
        nargs="?",
        type=int,
        default=None,
        help=f"lunghezza della password (default: {DEFAULT_LENGTH}). Se non specificato, verrà chiesto."
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="stampa solo la password, senza altre informazioni")
    args = parser.parse_args()

    if args.length is not None:
        if not (MIN_LENGTH <= args.length <= MAX_LENGTH):
            # Scrive su stderr per non inquinare l'output in caso di pipe
            print(
                f"❌ Errore: la lunghezza deve essere tra {MIN_LENGTH} e {MAX_LENGTH}.",
                file=sys.stderr
            )
            sys.exit(1)
        length = args.length
    else:
        length = ask_length()

    charset = build_charset(
        not args.no_upper,
        not args.no_digits,
        not args.no_symbols,
    )

    pwd = generate_pwd(length, charset)
    ent = entropy(length, len(charset))

    if args.quiet:
        print(pwd)
    else:
        print("\n🔐  Password:", pwd)
        print(f"🧮  Entropia stimata: {ent} bit "
              f"(len={length}, charset={len(charset)} caratteri)\n")

if __name__ == "__main__":
    main()
