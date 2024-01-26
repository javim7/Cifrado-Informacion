from Cifrados.Afin import *
from Cifrados.Caesar import *
from Cifrados.Vigenere import *
from Cifrados.Frecuencias import *

if __name__ == '__main__':
    # Frecuencias 
    frecuencias = Frecuencias()

    # Caesar
    texto = "ATACAR AL AMANECER"
    llave = 3
    caesar = Caesar(texto, llave)
    print("Texto: " + texto)
    print("Llave: " + str(llave))
    print("Texto limpio: " + caesar.textoLimpio)
    print("Texto cifrado: " + caesar.encrypt())
    print("Texto descifrado: " + caesar.decrypt())
    print("Frecuencias: " + str(frecuencias.frecuencias(caesar.cypherText)))
    print("Cifrado sustituido: " + str(frecuencias.sustituir_letras(frecuencias.nuevas_frecuencias, caesar.cypherText)))
    print("")

    # Afin
    a = 5
    b = 8
    afin = Afin(texto, a, b)
    print("Texto: " + texto)
    print("a: " + str(a))
    print("b: " + str(b))
    print("Texto limpio: " + afin.textoLimpio)
    print("Texto cifrado: " + afin.encrypt())
    print("Texto descifrado: " + afin.decrypt())
    print("Frecuencias: " + str(frecuencias.frecuencias(afin.cypherText)))
    print("")

    # # Vigenere
    # texto = "hola mundo"
    # llave = "llave"
    # vigenere = Vigenere(texto, llave)
    # print("Texto: " + texto)
    # print("Llave: " + llave)
    # print("Texto limpio: " + vigenere.textoLimpio)
    # print("Texto cifrado: " + vigenere.encrypt())
    # print("Texto descifrado: " + vigenere.decrypt(vigenere.encrypt()))
    # print("")