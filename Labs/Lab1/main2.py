from Cifrados.Afin import *
from Cifrados.Caesar import *
from Cifrados.Vigenere import *
from Cifrados.Frecuencias import *

def parteA():
    print("\n---------PARTE A---------")

    # Caesar
    print('\n\t[1] CAESAR')
    texto = "ATACAR AL AMANECER"
    clave = 3
    caesar = Caesar()
    print("Texto: " + texto)
    cypherText = caesar.encrypt(texto, clave)
    print("Texto cifrado: " + cypherText)
    plainText = caesar.decrypt(cypherText, clave)
    print("Texto descifrado: " + plainText)
    frecuenciasCaesar = Frecuencias()
    frecuenciasExp = frecuenciasCaesar.obtenerFrecuencias(cypherText)
    frecuenciasExpSort, frecuenciasTeoSort = frecuenciasCaesar.ordenarFrecuencias(frecuenciasExp)
    print(frecuenciasExpSort)
    print()

    # Afin
    print('\n\t[2] AFIN')
    a = 5
    b = 8
    afin = Afin()
    print("Texto: " + texto)
    cypherText = afin.encrypt(texto, a, b)
    print("Texto cifrado: " + cypherText)
    plainText = afin.decrypt(cypherText, a, b)
    print("Texto descifrado: " + plainText)
    frecuenciasAfin = Frecuencias()
    frecuenciasExp = frecuenciasAfin.obtenerFrecuencias(cypherText)
    frecuenciasExpSort, frecuenciasTeoSort = frecuenciasAfin.ordenarFrecuencias(frecuenciasExp)
    print(frecuenciasExpSort)
    print()

    # Vigenere
    print('\n\t[3] VIGENERE')
    llave = "CLAVE"
    vigenere = Vigenere()
    print("Texto: " + texto)
    cypherText = vigenere.encrypt(texto, llave)
    print("Texto cifrado: " + cypherText)
    plainText = vigenere.decrypt(cypherText, llave)
    print("Texto descifrado: " + plainText)
    frecuenciasVigenere = Frecuencias()
    frecuenciasExp = frecuenciasVigenere.obtenerFrecuencias(cypherText)
    frecuenciasExpSort, frecuenciasTeoSort = frecuenciasVigenere.ordenarFrecuencias(frecuenciasExp)
    print(frecuenciasExpSort)

def parteB():
    print("\n---------PARTE B---------")

    # Caesar
    print('\n\t[1] CAESAR')
    with open('Labs/Lab1/Textos/cipher1.txt', 'r') as file:
        textoCaesar = file.read()
    
    caesar = Caesar()
    frecuenciasCaesar = Frecuencias()
    frecuenciasExp = frecuenciasCaesar.obtenerFrecuencias(textoCaesar)
    frecuenciasExpSort, frecuenciasTeoSort = frecuenciasCaesar.ordenarFrecuencias(frecuenciasExp)
    caesar.fuerzaBruta(textoCaesar, frecuenciasTeoSort, frecuenciasExpSort)

    # Afin
    print('\n\t[2] AFIN')
    with open('Labs/Lab1/Textos/cipher2.txt', 'r') as file:
        textoAfin = file.read()

    afin = Afin()
    frecuenciasAfin = Frecuencias()
    frecuenciasExp = frecuenciasAfin.obtenerFrecuencias(textoAfin)
    frecuenciasExpSort, frecuenciasTeoSort = frecuenciasAfin.ordenarFrecuencias(frecuenciasExp)
    afin.fuerzaBruta(textoAfin, frecuenciasTeoSort, frecuenciasExpSort)

    # Vigenere
    print('\n\t[3] VIGENERE')
    with open('Labs/Lab1/Textos/cipher3.txt', 'r') as file:
        textoVigenere = file.read()
    
    vigenere = Vigenere()
    frecuenciasVigenere = Frecuencias()
    frecuenciasExp = frecuenciasVigenere.obtenerFrecuencias(textoVigenere)
    frecuenciasExpSort, frecuenciasTeoSort = frecuenciasVigenere.ordenarFrecuencias(frecuenciasExp)
    longitud = vigenere.obtenerLongitud(textoVigenere)
    vigenere.fuerzaBruta2(textoVigenere, longitud)

if __name__ == '__main__':
    parteA()
    parteB()
    