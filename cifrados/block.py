from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import io

def encryptImageECB(key, imagePath, outputPath):
    with open(imagePath, "rb") as file:
        imageBytes = file.read()

    cipher = AES.new(key, AES.MODE_ECB)
    paddedImageBytes = pad(imageBytes, AES.block_size)
    encryptedImageBytes = cipher.encrypt(paddedImageBytes)

    with open(outputPath, "wb") as file:
        file.write(encryptedImageBytes)

def encryptImageCBC(key, imagePath, outputPath):
    with open(imagePath, "rb") as file:
        imageBytes = file.read()

    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    paddedImageBytes = pad(imageBytes, AES.block_size)
    encryptedImageBytes = cipher.encrypt(paddedImageBytes)

    with open(outputPath, "wb") as file:
        file.write(iv + encryptedImageBytes)

def main():
    key = get_random_bytes(16)
    input_image_path = 'input_image.jpg'
    
    encrypted_image_path_ecb = 'encrypted_image_ecb.enc'
    encryptImageECB(key, input_image_path, encrypted_image_path_ecb)

    encrypted_image_path_cbc = 'encrypted_image_cbc.enc'
    encryptImageCBC(key, input_image_path, encrypted_image_path_cbc)

if __name__ == "__main__":
    main()