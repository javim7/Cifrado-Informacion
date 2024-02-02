class Vigenere:
    def __init__(self, texto, llave, alfabeto):
        self.texto = texto.upper()
        self.alfabeto = alfabeto
        self.llave = llave.upper()
        self.mod = len(self.alfabeto)
        self.n = len(self.llave)
        self.cypherText = None
        self.textoLimpio = self.limpiarTexto()

    def limpiarTexto(self):
        textoLimpio = ""
        for letra in self.texto:
            if letra not in self.alfabeto:
                textoLimpio += letra
            elif letra in self.alfabeto:
                textoLimpio += letra.upper()
            elif letra.upper() in ['á', 'é', 'í', 'ó', 'ú']:
                letra_sin_tilde = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}[letra.upper()]
                textoLimpio += letra_sin_tilde
        return textoLimpio

    def encrypt(self):
        cypherText = ""
        llave_indice = 0 
        for i in range(len(self.textoLimpio)):
            letra = self.textoLimpio[i]
            if letra not in self.alfabeto:
                cypherText += letra
            elif letra in self.alfabeto:
                indice_letra = self.alfabeto.index(letra)
                indice_llave = self.alfabeto.index(self.llave[llave_indice])
                indice = (indice_letra + indice_llave) % self.mod
                cypherText += self.alfabeto[indice].upper() if letra.isupper() else self.alfabeto[indice]
                llave_indice = (llave_indice + 1) % len(self.llave) 

        self.cypherText = cypherText
        return cypherText

    def decrypt(self):
        plainText = ""
        llave_indice = 0 
        for i in range(len(self.cypherText)):
            letra = self.cypherText[i]
            if letra not in self.alfabeto:
                plainText += letra
            elif letra in self.alfabeto:
                indice_letra = self.alfabeto.index(letra)
                indice_llave = self.alfabeto.index(self.llave[llave_indice])
                indice = (indice_letra - indice_llave) % self.mod
                plainText += self.alfabeto[indice].upper() if letra.isupper() else self.alfabeto[indice]
                llave_indice = (llave_indice + 1) % len(self.llave) 

        return plainText
    
    def fuerzaBruta(self, sortedOg, sortedNew):
        pass