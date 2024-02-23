from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encryptAES(key, plainText):
    cipher = AES.new(key, AES.MODE_CBC, iv=get_random_bytes(16))
    # Revisar si plainText es un string o bytes
    if not isinstance(plainText, bytes):
        plainText = plainText.encode()
    padded_plainText = pad(plainText, AES.block_size)
    encrypted_plainText = cipher.encrypt(padded_plainText)
    return encrypted_plainText, cipher.iv

def decryptAES(key, encrypted_plainText, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_padded_plainText = cipher.decrypt(encrypted_plainText)
    decrypted_plainText = unpad(decrypted_padded_plainText, AES.block_size)
    return decrypted_plainText

def ogAES(plainText):
    print("Plain text:", plainText)
    
    key = get_random_bytes(16)
    print("Key:", key.hex())

    encrypted_text, iv = encryptAES(key, plainText)
    print("\nEncrypted text:", encrypted_text.hex())

    decrypted_text = decryptAES(key, encrypted_text, iv)
    print("Decrypted text:", decrypted_text.decode())

if __name__ == "__main__":
    plainText = b"Hello, World!"
    ogAES(plainText)
