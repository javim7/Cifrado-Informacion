from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encryptDes(key, plainText):
    cipher = DES.new(key, DES.MODE_ECB)
    # Check if plainText is already bytes, if not, encode it
    if not isinstance(plainText, bytes):
        plainText = plainText.encode()
    padded_plainText = pad(plainText, DES.block_size)
    encrypted_plainText = cipher.encrypt(padded_plainText)
    return encrypted_plainText

def decryptDes(key, encrypted_plainText):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded_plainText = cipher.decrypt(encrypted_plainText)
    # Remover el padding
    decrypted_plainText = unpad(decrypted_padded_plainText, DES.block_size)
    return decrypted_plainText

def ogDES():
    # La llave debe ser de 8 bytes
    key = get_random_bytes(8)
    print("Key:", key.hex())
    plainText = "Hello, this is some sensitive information."

    encrypted_plainText = encryptDes(key, plainText)
    print("Encrypted plainText:", encrypted_plainText.hex())

    decrypted_plainText = decryptDes(key, encrypted_plainText)
    print("Decrypted plainText:", decrypted_plainText.decode())

def tripDES():
    key1 = get_random_bytes(8)
    key2 = get_random_bytes(8)
    key3 = get_random_bytes(8)

    plainText = "Hello, this is some sensitive information."
    
    encrypted_text = encryptTDEA(key1, key2, key3, plainText)
    print("Encrypted plainText:", encrypted_text.hex())

    decrypted_text = decryptTDEA(key1, key2, key3, encrypted_text)
    print("Decrypted plainText:", decrypted_text.decode())

def encryptTDEA(key1, key2, key3, plainText):
    encrypted_S1 = encryptDes(key1, plainText)
    encrypted_S2 = encryptDes(key2, encrypted_S1)
    encrypted_S3 = encryptDes(key3, encrypted_S2)

    return encrypted_S3 

def decryptTDEA(key1, key2, key3, encrypted_text):
    decrypted_S3 = decryptDes(key3, encrypted_text)
    decrypted_S2 = decryptDes(key2, decrypted_S3)
    decrypted_S1 = decryptDes(key1, decrypted_S2)

    return decrypted_S1

if __name__ == "__main__":
    print("\nDES")
    ogDES()

    print("\nTriple DES")
    tripDES()
