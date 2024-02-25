from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from PIL import Image

# ECB Mode Encryption
def ecb_encrypt(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image_bytes = image.tobytes()
    padded_data = pad(image_bytes, AES.block_size)
    
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(padded_data)
    
    with Image.frombytes('RGB', image.size, encrypted_data) as im_ecb:
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

def main():

    key = get_random_bytes(32)  # 256-bit key

    # logo
    input_image_path = "./images/logo.webp"
    output_ecb_image_path = "./images/logoECB.webp"
    output_cbc_image_path = "./images/logoCBC.webp"

    ecb_encrypt(input_image_path, output_ecb_image_path, key)
    cbc_encrypt(input_image_path, output_cbc_image_path, key)

    # tux
    input_image_path = "./images/tux.ppm"
    output_ecb_image_path = "./images/tuxECB.ppm"
    output_cbc_image_path = "./images/tuxCBC.ppm"

    ecb_encrypt(input_image_path, output_ecb_image_path, key)
    cbc_encrypt(input_image_path, output_cbc_image_path, key)

    # foto
    input_image_path = "./images/foto.jpeg"
    output_ecb_image_path = "./images/fotoECB.jpeg"
    output_cbc_image_path = "./images/fotoCBC.jpeg"

    ecb_encrypt(input_image_path, output_ecb_image_path, key)
    cbc_encrypt(input_image_path, output_cbc_image_path, key)

if __name__ == "__main__":
    main()

