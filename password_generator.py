#!/usr/bin/env python3
"""Generate cryptographically secure random passwords."""

import argparse
import secrets
import string


def generate_password(
    length: int = 16,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Generate a random password using ``secrets``.

    At least one character from every enabled set is guaranteed.
    """
    pools = []
    if use_uppercase:
        pools.append(string.ascii_uppercase)
    if use_lowercase:
        pools.append(string.ascii_lowercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append(string.punctuation)

    if not pools:
        raise ValueError("At least one character set must be enabled")
    if length < len(pools):
        raise ValueError(f"Length must be at least {len(pools)} for the selected character sets")

    chars = [secrets.choice(pool) for pool in pools]
    alphabet = "".join(pools)
    chars.extend(secrets.choice(alphabet) for _ in range(length - len(chars)))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument("-l", "--length", type=int, default=16,
                        help="Password length (default: 16)")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lowercase", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("-n", "--count", type=int, default=1,
                        help="Number of passwords to generate (default: 1)")
    args = parser.parse_args()

    try:
        for _ in range(args.count):
            print(generate_password(
                length=args.length,
                use_uppercase=not args.no_uppercase,
                use_lowercase=not args.no_lowercase,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols,
            ))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
