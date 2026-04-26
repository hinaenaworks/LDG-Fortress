# LDG-Fortress
# Logical Defense Grid (LDG)

## Concept
A security framework where the system remains non-functional unless a valid physical signature is verified.

## Usage
1. Generate assets (Offline): `python tools/generate_assets.py`
2. Build container: `docker build -t ldg-fortress .`
3. Run with Read-Only: `docker run --rm --read-only ldg-fortress`

## Security Note
Never commit `private_key.pem`.
