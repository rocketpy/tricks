# Cryptography is a package which provides cryptographic recipes and primitives to Python developers.

# https://pypi.org/project/cryptography/

# pip install cryptography


from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
print(token)
# b'...'
# f.decrypt(token)
# b'A really secret message. Not for prying eyes.'


from cryptography.fernet import Fernet, MultiFernet

key1 = Fernet(Fernet.generate_key())
key2 = Fernet(Fernet.generate_key())
f = MultiFernet([key1, key2])
token = f.encrypt(b"Secret message!")
f.decrypt(token)
# b'Secret message!'
