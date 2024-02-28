from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from PIL import Image

# ECB Mode Encryption
def ecb_encrypt(input_image_path, output_image_path, key):
    image = Image.open(input_image_path).convert('RGB')
    image_bytes = image.tobytes()
    padded_data = pad(image_bytes, AES.block_size)
    
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(padded_data)
    
    with Image.frombytes('RGB', image.size, encrypted_data) as im_ecb:
        im_ecb.save(output_image_path)

# ECB Mode Decryption
def ecb_decrypt(input_image_path, output_image_path, key):
    # Asegúrar de que la clave sea de 16 bytes
    key = bytes.fromhex(key)
    if len(key) != 16:
        raise ValueError("La clave debe ser de 16 bytes")

    with open(input_image_path, 'rb') as f:
        encrypted_data = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    with open(output_image_path, 'wb') as f:
        f.write(decrypted_data)

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

    with open(input_image_path, 'rb') as file:
        data = file.read()

    iv = data[:AES.block_size]
    encrypted_data = data[AES.block_size:]

    key = bytes.fromhex(key)
    
    if len(key) != 16:
        raise ValueError("La clave debe ser de 16 bytes")

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    with open(output_image_path, 'wb') as file:
        file.write(decrypted_data)

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

    # Decrypt
    # increbile
    with open('./keys/mr-increible.key', 'r') as f:
        increibleKey = f.read()
    
    input_image_path = 'images/mr-increible_encrypted_image.jpeg'
    output_ecb = 'images/mr-increible_decrypted_image.jpeg'

    ecb_decrypt(input_image_path, output_ecb, increibleKey)

    # ayno
    with open('./keys/ayno.key', 'r') as f:
        aynoKey = f.read()

    input_image_path = 'images/ayno_encrypted_image.jpeg'
    output_cbc = 'images/ayno_decrypted_image.jpeg'

    cbc_decrypt(input_image_path, output_cbc, aynoKey)

if __name__ == "__main__":
    main()

