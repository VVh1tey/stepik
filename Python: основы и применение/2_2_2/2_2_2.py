from simplecrypt import DecryptionException, decrypt

encrypted = open("encrypted.bin", "rb").read()
psws = open("passwords.txt").readlines()
for password in psws:
    password = password.strip()
    try:
        print(decrypt(password, encrypted).decode('utf8'))
    except DecryptionException:
        continue
    else:
        print(password, 'is correct')