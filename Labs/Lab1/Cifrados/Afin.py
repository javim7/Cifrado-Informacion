class Afin:
    def __init__(self, texto, a, b, alfabeto):
        self.texto = texto.upper()
        self.a = a
        self.b = b
        self.alfabeto = alfabeto
        self.mod = len(self.alfabeto)
        self.textoLimpio = self.limpiarTexto()
        self.cypherText = None

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
        for letra in self.textoLimpio:
            if letra not in self.alfabeto:
                cypherText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice = (self.a * indice + self.b) % self.mod
                cypherText += self.alfabeto[indice]

        self.cypherText = cypherText
        return cypherText
    
    def inverso(self):
        for i in range(self.mod):
            if (self.a * i) % self.mod == 1:
                return i
        return None

    def decrypt(self):
        plainText = ""
        inverse_a = self.inverso()
        for letra in self.cypherText:
            if letra not in self.alfabeto:
                plainText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice = inverse_a * (indice - self.b) % self.mod
                plainText += self.alfabeto[indice]

        return plainText