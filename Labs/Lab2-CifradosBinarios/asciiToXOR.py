def main():
    word = 'sun'
    key = 'ke'
    xor_rep = asciiToXOR(word, key)
    ascii_rep = xOrToAscii(xor_rep, key)
    print('XOR representation: ' + str(xor_rep))
    print('Ascii representation : ' + str(ascii_rep))

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

if __name__ == "__main__":
    main()