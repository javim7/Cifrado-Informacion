from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from PIL import Image
import numpy as np
import io

# ECB Mode Encryption
def ecb_encrypt(input_image_path, output_image_path, key):
    print(key)
    image = Image.open(input_image_path).convert('RGB')
    image_bytes = image.tobytes()
    padded_data = pad(image_bytes, AES.block_size)
    
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(padded_data)
    
    # Save encrypted data to a binary file
    with open(output_image_path, 'wb') as file:
        file.write(encrypted_data)

# ECB Mode Decryption
def ecb_decrypt(input_image_path, output_image_path, key):
    print(key)
    with open(input_image_path, 'rb') as file:
        encrypted_data = file.read()
    print(encrypted_data[:10])
    #width, height = get_image_dimensions_from_file(input_image_path)
    #print(width, height)

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    
    # save decrypted data as binary file
    with open(output_image_path, 'wb') as file:
        file.write(decrypted_data)

    print(decrypted_data[:10])
    width, height = get_image_dimensions(decrypted_data)
    print(width, height)

    # Save binary as image
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
    
    # Save encrypted data along with IV to a binary file
    with open(output_image_path, 'wb') as file:
        file.write(iv + encrypted_data)

# CBC Mode Decryption
def cbc_decrypt(input_image_path, output_image_path, key):
    with open(input_image_path, 'rb') as file:
        data = file.read()
    
    iv = data[:AES.block_size]
    encrypted_data = data[AES.block_size:]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    
    with open(output_image_path, 'wb') as file:
        file.write(decrypted_data)

def get_image_dimensions(image_data):
    try:
        image = Image.open(io.BytesIO(image_data))
        width, height = image.size
        return width, height
    except Exception as e:
        print("Error:", str(e))
        return None, None
    
def main():

    key = get_random_bytes(32)  # 256-bit key

    # foto
    input_image_path = "./images/foto.jpeg"
    output_ecb_image_path = "./images/fotoECB.jpeg"
    output_ecb_decrypted = "./images/fotoECB_decrypted.jpeg"

    ecb_encrypt(input_image_path, output_ecb_image_path, key)
    ecb_decrypt(output_ecb_image_path, output_ecb_decrypted, key)

    output_cbc_image_path = "./images/fotoCBC.jpeg"
    #cbc_encrypt(input_image_path, output_cbc_image_path, key)


    # increbile
    with open('./keys/mr-increible.key', 'rb') as f:
        increibleKey = f.read()
    input_image_path = 'images/mr-increible_encrypted_image.jpeg'
    output_ecb = 'images/mr-increible_decrypted_image.jpeg'

    ecb_decrypt(input_image_path, output_ecb, increibleKey)
    
    # tux
    input_image_path = "./images/tux.ppm"
    output_ecb_image_path = "./images/tuxECB.ppm"
    output_ecb_decrypted = "./images/tuxECB_decrypted.ppm"

    #ecb_encrypt(input_image_path, output_ecb_image_path, key)
    #ecb_decrypt(output_ecb_image_path, output_ecb_decrypted, key)

    output_cbc_image_path = "./images/tuxCBC.ppm"
    # cbc_encrypt(input_image_path, output_cbc_image_path, key)

if __name__ == "__main__":
    main()