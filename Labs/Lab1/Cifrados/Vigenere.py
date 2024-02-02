class Vigenere():
    def __init__(self):
        self.alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    def limpiarTexto(self, texto):
        textoLimpio = ""
        for letra in texto:
            if letra not in self.alfabeto:
                textoLimpio += letra
            elif letra in self.alfabeto:
                textoLimpio += letra.upper()
            elif letra.upper() in ['á', 'é', 'í', 'ó', 'ú']:
                letra_sin_tilde = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}[letra.upper()]
                textoLimpio += letra_sin_tilde
        return textoLimpio
    
    def encrypt(self, texto, llave):
        textoLimpiado = self.limpiarTexto(texto)
        cypherText = ""
        llave_indice = 0 
        for i in range(len(textoLimpiado)):
            letra = textoLimpiado[i]
            if letra not in self.alfabeto:
                cypherText += letra
            elif letra in self.alfabeto:
                indice_letra = self.alfabeto.index(letra)
                indice_llave = self.alfabeto.index(llave[llave_indice])
                indice = (indice_letra + indice_llave) % len(self.alfabeto)
                cypherText += self.alfabeto[indice].upper() if letra.isupper() else self.alfabeto[indice]
                llave_indice = (llave_indice + 1) % len(llave) 

        return cypherText
    
    def decrypt(self, cypherText, llave):
        plainText = ""
        llave_indice = 0 
        for i in range(len(cypherText)):
            letra = cypherText[i]
            if letra not in self.alfabeto:
                plainText += letra
            elif letra in self.alfabeto:
                indice_letra = self.alfabeto.index(letra)
                indice_llave = self.alfabeto.index(llave[llave_indice])
                indice = (indice_letra - indice_llave) % len(self.alfabeto)
                plainText += self.alfabeto[indice].upper() if letra.isupper() else self.alfabeto[indice]
                llave_indice = (llave_indice + 1) % len(llave) 

        return plainText