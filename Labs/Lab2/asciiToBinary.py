def main():
    word = 'hola'
    binaryRep = asciiToBinary(word)
    asciiRep = binaryToAscii(binaryRep)
    print('Binary representation: ' + binaryRep)
    print('Ascii representation: ' + asciiRep)

def asciiToBinary(word):
    binaryRepresentation = ''
    for letter in word:
        ascii = getAsciiFromWord(letter)
        binary = getBinaryFromWord(ascii)
        binaryRepresentation += str(binary)
        binaryRepresentation += ' '
    # print(binaryRepresentation)
    return binaryRepresentation

def getAsciiFromWord(letter):
    return ord(letter)

def getBinaryFromWord(ascii):
    binaryNumber = ''
    while ascii > 0:
        binaryNumber = str(ascii % 2) + binaryNumber
        ascii = ascii // 2
    while len(binaryNumber) < 8:
        binaryNumber = '0' + binaryNumber
    return binaryNumber

def binaryToAscii(binaryRep):
    asciiRepresentation = ''
    binaryNumbers = binaryRep.split(' ')
    for binary in binaryNumbers:
        decimal = getDecimalFromBinary(binary)
        asciiRepresentation += getAsciiFromDecimal(decimal)
    return asciiRepresentation

def getDecimalFromBinary(binary):
    decimal = 0
    for i, bit in enumerate(reversed(binary)):
        decimal += int(bit) * (2 ** i)
    return decimal

def getAsciiFromDecimal(decimal):
    return chr(decimal)

if __name__ == "__main__":
    main()