from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from PIL import Image
import struct

# ECB Mode Encryption
def ecb_encrypt(input_image_path, output_image_path, key):
    image = Image.open(input_image_path).convert('RGB')
    width, height = image.size
    image_bytes = image.tobytes()
    original_size = len(image_bytes)
    padded_data = pad(image_bytes, AES.block_size)
    
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(padded_data)
    
    with open(output_image_path, 'wb') as f:
        # Write the width, height, and original size as 4-byte integers
        f.write(struct.pack('<III', width, height, original_size))
        f.write(encrypted_data)

# ECB Mode Decryption
def ecb_decrypt(input_image_path, output_image_path, key):
    with open(input_image_path, 'rb') as f:
        # Read the width, height, and original size
        width, height, original_size = struct.unpack('<III', f.read(12))
        encrypted_data = f.read()
    
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    decrypted_data = decrypted_data[:original_size]  # Trim to original size
    
    with Image.frombytes('RGB', (width, height), decrypted_data) as im_ecb:
        im_ecb.save(output_image_path)

# CBC Mode Encryption
def cbc_encrypt(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image_bytes = image.tobytes()
    padded_data = pad(image_bytes, AES.block_size)
    
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(padded_data)
    
    with Image.frombytes('RGB', image.size, encrypted_data) as im_cbc:
        im_cbc.save(output_image_path)

# CBC Mode Decryption
def cbc_decrypt(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    encrypted_data = image.tobytes()
    
    iv = encrypted_data[:AES.block_size]
    encrypted_data = encrypted_data[AES.block_size:]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    
    with Image.frombytes('RGB', image.size, decrypted_data) as im_cbc:
        im_cbc.save(output_image_path)

def main():

    key = get_random_bytes(32)  # 256-bit key

    # logo
    input_image_path = "./images/logo.webp"
    output_ecb_image_path = "./images/logoECB.webp"
    output_cbc_image_path = "./images/logoCBC.webp"

    ecb_encrypt(input_image_path, output_ecb_image_path, key)
    cbc_encrypt(input_image_path, output_cbc_image_path, key)

    ecb_decrypt(output_ecb_image_path, "./images/logoECBDec.webp", key)

    # # tux
    # input_image_path = "./images/tux.ppm"
    # output_ecb_image_path = "./images/tuxECB.ppm"
    # output_cbc_image_path = "./images/tuxCBC.ppm"

    # ecb_encrypt(input_image_path, output_ecb_image_path, key)
    # cbc_encrypt(input_image_path, output_cbc_image_path, key)

    # # foto
    # input_image_path = "./images/foto.jpeg"
    # output_ecb_image_path = "./images/fotoECB.jpeg"
    # output_cbc_image_path = "./images/fotoCBC.jpeg"

    # ecb_encrypt(input_image_path, output_ecb_image_path, key)
    # cbc_encrypt(input_image_path, output_cbc_image_path, key)

if __name__ == "__main__":
    main()

