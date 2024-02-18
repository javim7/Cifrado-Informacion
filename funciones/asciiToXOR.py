'''
CODIFICACION
'''
def asciiToXOR(word, key):
    word, key = checkLength(word, key)
    binary_word = ''
    binary_key = ''
    for letter in word:
        ascii_val = getAsciiFromLetter(letter)
        binary = getBinaryFromNumber(ascii_val)
        binary_word += binary
    for letter in key:
        ascii_val = getAsciiFromLetter(letter)
        binary = getBinaryFromNumber(ascii_val)
        binary_key += binary
    xOr_rep = xOr(binary_word, binary_key)
    return xOr_rep
    

def checkLength(word, key):
    if len(word) > len(key):
        key = key * (len(word) // len(key)) + key[:len(word) % len(key)]
    elif len(word) < len(key):
        word = word + '\0' * (len(key) - len(word))
    
    return word, key

def getAsciiFromLetter(letter):
    return ord(letter)

def getBinaryFromNumber(ascii):
    binaryNumber = ''
    while ascii > 0:
        binaryNumber = str(ascii % 2) + binaryNumber
        ascii = ascii // 2
    while len(binaryNumber) < 8:
        binaryNumber = '0' + binaryNumber
    return binaryNumber

def xOr(binary_word, binary_key):
    xOr_rep = ''
    for i in range(len(binary_word)):
        xOr_rep += str(int(binary_word[i]) ^ int(binary_key[i]))
    return xOr_rep

'''
DECODIFICACION
'''
def xOrToAscii(xOr_rep, key):
    key = checkBitLenght(xOr_rep, key)
    binary_key = ''
    for letter in key:
        ascii_val = getAsciiFromLetter(letter)
        binary = getBinaryFromNumber(ascii_val)
        binary_key += binary
    xOrRevert = xOr(xOr_rep, binary_key)
    asciiRepresentation = binaryToAscii(xOrRevert)
    return asciiRepresentation

def checkBitLenght(xOr_rep, key):
    charLength = len(xOr_rep) // 8

    if len(key) < charLength:
        key = key * (charLength // len(key)) + key[:charLength % len(key)]
    
    return key

def binaryToAscii(binary_string):
    # Convertir de binario a ASCII
    ascii_string = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))
    # Eliminar caracteres ficticios
    ascii_string = ascii_string.rstrip('\0')
    return ascii_string

'''
IMAGEN CON CLAVE
'''
def imageXOR(image, key):
    imageBytes = imageToBytes(image)
    key = checkKeyLength(imageBytes, key)
    binary_key = ''
    for letter in key:
        ascii_val = getAsciiFromLetter(letter)
        binary = getBinaryFromNumber(ascii_val)
        binary_key += binary
    xOr_rep = xOr(imageBytes, binary_key)
    newPath = bytesToImage(xOr_rep, './imagenes/imagen_xor2')
    return newPath

def imageToBytes(image):
   with open(image, 'rb') as f:
    contenido = f.read()

    binary_data = ['{:08b}'.format(byte) for byte in contenido]  
    return ''.join(binary_data)

def checkKeyLength(imageBytes, key):
    charLength = len(imageBytes) // 8

    if len(key) < charLength:
        key = key * (charLength // len(key)) + key[:charLength % len(key)]
    
    return key

def bytesToImage(binary_string, name):
    with open(name + '.png', 'wb') as f:
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            f.write(bytes([int(byte, 2)]))
    return name + '.png'

'''
DOS IMAGENES
'''
from PIL import Image

def imagesXOR(image1_path, image2_path, output_path):
    # Abrir ambas imágenes
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Asegurarse de que ambas imágenes tengan el mismo tamaño
    if image1.size != image2.size:
        raise ValueError("Las imágenes deben tener el mismo tamaño")

    # Convertir las imágenes a modo RGBA (para tener 4 canales: rojo, verde, azul y alfa)
    image1 = image1.convert("RGBA")
    image2 = image2.convert("RGBA")

    # Aplicar la operación XOR byte a byte
    xor_image = Image.alpha_composite(Image.blend(image1, image2, alpha=0.5), Image.blend(image2, image1, alpha=0.5))

    # Guardar la imagen resultante
    xor_image.save(output_path)

'''
MAIN
'''
def main():
    word = 'sun'
    key = 'ke'
    xor_rep = asciiToXOR(word, key)
    ascii_rep = xOrToAscii(xor_rep, key)
    print('XOR representation: ' + str(xor_rep))
    print('Ascii representation : ' + str(ascii_rep))

    image = './imagenes/imagen_xor.png'
    key = 'cifrados'
    imageXOR(image, key)

    image1 = './imagenes/view.png'
    image2 = './imagenes/dog.png'
    output_path = './imagenes/viewDogXor.png'
    imagesXOR(image1, image2, output_path)

if __name__ == "__main__":
    main()