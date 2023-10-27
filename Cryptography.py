# Cryptography is a package which provides cryptographic recipes and primitives to Python developers.

# https://pypi.org/project/cryptography/


from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
print(token)
# b'...'
# f.decrypt(token)
# b'A really secret message. Not for prying eyes.'
