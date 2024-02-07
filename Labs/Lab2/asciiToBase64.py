def main():
    word = 'Hola'
    base64_rep = asciiToBase64(word)
    print('Base64 representation: ' + base64_rep)

def asciiToBase64(word):
    binary_representation = ''
    for letter in word:
        ascii_val = getAsciiFromWord(letter)
        binary = getBinaryFromWord(ascii_val)
        binary_representation += binary
    groups_of_6 = separateIntoGroupsOf6(binary_representation)
    base64_rep = getBase64FromChunks(groups_of_6)
    return base64_rep

def getAsciiFromWord(letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    return alphabet.index(letter)

def getBinaryFromWord(ascii):
    binaryNumber = ''
    while ascii > 0:
        binaryNumber = str(ascii % 2) + binaryNumber
        ascii = ascii // 2
    while len(binaryNumber) < 7:  # Adjusted to 7 bits
        binaryNumber = '0' + binaryNumber
    return binaryNumber

def separateIntoGroupsOf6(binary):
    while len(binary) % 6 != 0:
        binary += '0'
    groups_of_6 = [binary[i:i+6] for i in range(0, len(binary), 6)]
    return groups_of_6

def getBase64FromChunks(groups_of_6):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base64 = ''
    for chunk in groups_of_6:
        decimal = getDecimalFromBinary(chunk)
        base64 += alphabet[decimal]
    return base64

def getDecimalFromBinary(binary):
    decimal = 0
    for i, bit in enumerate(reversed(binary)):
        decimal += int(bit) * (2 ** i)
    return decimal

if __name__ == "__main__":
    main()
