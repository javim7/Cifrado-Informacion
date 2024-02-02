from Cifrados.Afin import *
from Cifrados.Caesar import *
from Cifrados.Vigenere import *
from Cifrados.Alfabeto import *
from Cifrados.Frecuencias import *

if __name__ == '__main__':

    # Caesar
    texto = "ATACAR AL AMANECER"
    llave = 3
    caesar = Caesar(texto, llave, alfabeto)
    print("Texto: " + texto)
    print("Llave: " + str(llave))
    print("Texto limpio: " + caesar.textoLimpio)
    print("Texto cifrado: " + caesar.encrypt())
    print("Texto descifrado: " + caesar.decrypt())
    frecuencias1 = Frecuencias(caesar.cypherText)
    frecuencias1.sortedFrecuencias()
    # print("Frecuencias: " + str(frecuencias1.frecuencias()))
    # print("Frecuencias ordenadas: " + str(frecuencias1.sortedNew))
    caesar.fuerzaBruta(frecuencias1.sortedOg, frecuencias1.sortedNew)
    print("")

    # Afin
    a = 5
    b = 8
    afin = Afin(texto, a, b, alfabeto)
    print("Texto: " + texto)
    print("a: " + str(a))
    print("b: " + str(b))
    print("Texto limpio: " + afin.textoLimpio)
    print("Texto cifrado: " + afin.encrypt())
    print("Texto descifrado: " + afin.decrypt())
    frecuencias2 = Frecuencias(afin.cypherText)
    frecuencias2.sortedFrecuencias()
    # print("Frecuencias: " + str(frecuencias2.frecuencias()))
    # print("Frecuencias ordenadas: " + str(frecuencias2.sortedNew))
    afin.fuerzaBruta(frecuencias2.sortedOg, frecuencias2.sortedNew)
    print("")

    # Vigenere
    llave = "CLAVE"
    vigenere = Vigenere(texto, llave, alfabeto)
    print("Texto: " + texto)
    print("Llave: " + llave)
    print("Texto limpio: " + vigenere.textoLimpio)
    print("Texto cifrado: " + vigenere.encrypt())
    print("Texto descifrado: " + vigenere.decrypt())
    frecuencias3 = Frecuencias(vigenere.cypherText)
    frecuencias3.sortedFrecuencias()
    # print("Frecuencias: " + str(frecuencias3.frecuencias()))
    # print("Frecuencias ordenadas: " + str(frecuencias3.sortedNew))
    print("")
