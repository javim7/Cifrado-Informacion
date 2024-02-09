def main():
    word = 'Sun'
    base64_rep = asciiToBase64(word)
    ascii_rep = base64ToAscii(base64_rep)
    print('Base64 representation: ' + base64_rep)
    print('Ascii representation : ' + ascii_rep)

'''
CODIFICACION
'''
def asciiToBase64(word):
    binary_representation = ''
    for letter in word:
        ascii_val = getAsciiFromLetter(letter)
        # print(ascii_val)
        binary = getBinaryFromNumber(ascii_val)
        binary_representation += binary
    # print(binary_representation)
    groups_of_6 = separateIntoGroupsOf6(binary_representation)
    # print(groups_of_6)
    base64_rep = getBase64FromChunks(groups_of_6)
    return base64_rep

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

def separateIntoGroupsOf6(binary):
    groups_of_6 = []
    while len(binary) > 6:
        groups_of_6.append(binary[:6])
        binary = binary[6:]
    if len(binary) < 6:
        binary = binary + '0' * (6 - len(binary))
    groups_of_6.append(binary)
    return groups_of_6

def getBase64FromChunks(groups_of_6):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base64 = ''
    for chunk in groups_of_6:
        decimal = getDecimalFromBinary(chunk)
        # print(decimal)
        base64 += alphabet[decimal]
    return base64

def getDecimalFromBinary(binary):
    decimal = 0
    for i, bit in enumerate(reversed(binary)):
        decimal += int(bit) * (2 ** i)
    return decimal
'''
DECODIFICACION
'''
def base64ToAscii(base64):
    binary_representation = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    for letter in base64:
        decimal = alphabet.index(letter)
        # print(decimal)
        binary = getBinaryFromNumber2(decimal)
        binary_representation += binary
    # print(binary_representation)
    groups_of_8 = separateIntoGroupsOf8(binary_representation)
    # print(groups_of_8)
    ascii_rep = getAsciiFromChunks(groups_of_8)
    return ascii_rep

def getBinaryFromNumber2(ascii):
    binaryNumber = ''
    while ascii > 0:
        binaryNumber = str(ascii % 2) + binaryNumber
        ascii = ascii // 2
    while len(binaryNumber) < 6:
        binaryNumber = '0' + binaryNumber
    return binaryNumber

def separateIntoGroupsOf8(binary):
    groups_of_8 = []
    while len(binary) > 8:
        groups_of_8.append(binary[:8])
        binary = binary[8:]
    if len(binary) < 8:
        binary = '0' * (8 - len(binary)) + binary
    groups_of_8.append(binary)
    return groups_of_8

def getAsciiFromChunks(groups_of_8):
    ascii = ''
    for chunk in groups_of_8:
        decimal = getDecimalFromBinary(chunk)
        # print(decimal)
        ascii += chr(decimal)
        # print(ascii)
    return ascii

if __name__ == "__main__":
    main()
