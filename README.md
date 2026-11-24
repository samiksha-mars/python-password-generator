# Python Password Generator

A small command-line tool that generates cryptographically secure random passwords
using the standard library `secrets` module. No external dependencies.

## Features

- Configurable length
- Toggle uppercase, lowercase, digits and symbols on/off
- Generate multiple passwords at once
- Guarantees at least one character from every enabled set
- Cryptographically secure (uses `secrets`, not `random`)

## Usage

```bash
# Default: 16 characters, all sets enabled
python3 password_generator.py

# 20 characters
python3 password_generator.py --length 20

# Digits and symbols only
python3 password_generator.py --no-uppercase --no-lowercase

# Generate 5 passwords
python3 password_generator.py --count 5
```

## Tests

```bash
python3 -m unittest test_password_generator.py
```
