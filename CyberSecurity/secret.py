import os
from cryptography.fernet import Fernet

# Generate secret key
key = Fernet.generate_key()
f = Fernet(key)

# 'b' string indicates python should interpret string as bytes
token = f.encrypt(b"Deepest darkest secrets.")

print(f"Secret Token: {token}")  # It's encrypted
print(f"Decrypted string: {f.decrypt(token)}")
print()
print(f"Generated Key: {key}")
print(f"OS Random Bytestring: {os.urandom(32)}")
