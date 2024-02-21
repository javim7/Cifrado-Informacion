import random
import string

def main():
    plainText = 'HELLO'
    key = keyStreamGenerator(len(plainText))
    xOr_rep, binaryKey = encrypt(plainText, key)
    decryptedText = decrypt(xOr_rep, binaryKey)
    print('Original text : ' + plainText)
    print('Key           : ' + ''.join(key))
    print('Encrypted text: ' + xOr_rep)
    print('Decrypted text: ' + decryptedText)
    
def encrypt(text, key):
    binaryText = textToBinary(text)
    binaryKey = textToBinary(key)
    xOr_rep = xOr(binaryText, binaryKey)
    # print('XOR        : ' + xOr_rep)
    return xOr_rep, binaryKey

def decrypt(xOr_rep, binaryKey):
    decriptedBinary = xOr(xOr_rep, binaryKey)
    decriptedTxt = binaryToAscii(decriptedBinary)
    # print('Decripted text : ' + decriptedTxt)
    return decriptedTxt

def xOr(binary_word, binary_key):
    xOr_rep = ''
    for i in range(len(binary_word)):
        xOr_rep += str(int(binary_word[i]) ^ int(binary_key[i]))
    return xOr_rep

def binaryToAscii(binary_string):
    ascii_string = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))
    ascii_string = ascii_string.rstrip('\0')
    return ascii_string

def textToBinary(text):
    binary = ''
    for letter in text:
        ascii_val = getAsciiFromLetter(letter)
        binary += getBinaryFromNumber(ascii_val)
    return binary

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

def keyStreamGenerator(length):
    characters = string.printable.replace(' ', '').replace('\n', '')
    key = [random.choice(characters) for _ in range(length)]
    return key

if __name__ == '__main__':
    main()