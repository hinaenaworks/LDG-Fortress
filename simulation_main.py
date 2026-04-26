import json
import sys
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.exceptions import InvalidSignature

def verify_ldg():
    try:
        with open('public_key.pem', 'rb') as f:
            public_key = serialization.load_pem_public_key(f.read())
        
        with open('policy.json', 'rb') as f:
            policy_data = f.read()
            
        with open('policy.json.sig', 'rb') as f:
            signature = f.read()

        public_key.verify(signature, policy_data)
        print("[+] Verification Success.")
        return json.loads(policy_data)
    except (InvalidSignature, FileNotFoundError):
        print("[Critical] Integrity Failure. Halting System.")
        sys.exit(1)

if __name__ == "__main__":
    policy = verify_ldg()
    print(f"Executing: {policy['action']}")
