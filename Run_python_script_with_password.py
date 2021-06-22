from passlib.hash import sha256_crypt


password = '$5$rounds=80000$zvpXD3gCkrt7tw.1$QqeTSolNHEfgryc5oMgiq1o8qCEAcmye3FoMSuvgToC'


def check_passowrd():
    secret_word = input("Enter the secret word: ")
    hash = sha256_crypt.encrypt("secret_word")
    if hash == password:
        # do someething
    else:
        break


hash = sha256_crypt.encrypt("mysecretword")
print(hash)
# '$5$rounds=80000$zvpXD3gCkrt7tw.1$QqeTSolNHEfgryc5oMgiq1o8qCEAcmye3FoMSuvgToC'

# verifying 
print(sha256_crypt.verify("mysecretword", hash))
# True
print(sha256_crypt.verify("anyword", hash))
# False

# or
import hashlib


print(hashlib.md5(b"mysecretword").hexdigest())
# '5a105e8b9d40e1329780d62ea2265d8a'


if __name__ == '__main__':
    check_passowrd()
    
