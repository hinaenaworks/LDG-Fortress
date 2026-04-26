import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519

# 1. Key Generation
private_key = ed25519.Ed25519PrivateKey.generate()
public_key = private_key.public_key()

# 2. Save Keys
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

# 3. Sign Policy
with open("policy.json", "rb") as f:
    policy_data = f.read()

signature = private_key.sign(policy_data)

with open("policy.json.sig", "wb") as f:
    f.write(signature)

print("[Success] Keys and Signature generated.")
