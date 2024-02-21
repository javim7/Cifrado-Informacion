import random
import string

def main():
    plainText = 'HELLO'
    key = keyStreamGenerator(len(plainText))
    print('Original text : ' + plainText)
    print('Key           : ' + key)

    xOr_rep, binaryKey = encrypt(plainText, key)
    print('Encrypted text: ' + xOr_rep)
    
    decryptedText = decrypt(xOr_rep, binaryKey)
    print('Decrypted text: ' + decryptedText)
    
def encrypt(plainText, key):
    binaryText = textToBinary(plainText)
    binaryKey = textToBinary(key)
    print('Binary text   : ' + binaryText)
    print('Binary key    : ' + binaryKey)
    xOr_rep = xOr(binaryText, binaryKey)
    # print('XOR        : ' + xOr_rep)
    return xOr_rep, binaryKey

def decrypt(cipherText, binaryKey):
    decriptedBinary = xOr(cipherText, binaryKey)
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
        ascii_val = letterToAscii(letter)
        binary += numberToBinary(ascii_val)
    return binary

def letterToAscii(letter):
    return ord(letter)

def numberToBinary(ascii):
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
    return ''.join(key)

if __name__ == '__main__':
    main()