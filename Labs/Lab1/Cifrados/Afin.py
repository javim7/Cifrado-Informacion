class Afin:
    def __init__(self, texto, a, b):
        self.texto = texto.lower()
        self.a = a
        self.b = b
        self.alfabeto = "abcdefghijklmnñopqrstuvwxyz"
        self.mod = len(self.alfabeto)
        self.textoLimpio = self.limpiarTexto()
        self.cypherText = None

    def limpiarTexto(self):
        textoLimpio = ""
        for letra in self.texto:
            if letra == " ":
                textoLimpio += " "
            elif letra in self.alfabeto:
                textoLimpio += letra.lower()
            elif letra.lower() in ['á', 'é', 'í', 'ó', 'ú']:
                # Reemplazar letras con tilde
                letra_sin_tilde = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}[letra.lower()]
                textoLimpio += letra_sin_tilde
        return textoLimpio
    
    def encrypt(self):
        cypherText = ""
        for letra in self.textoLimpio:
            if letra == " ":
                cypherText += " "
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
            if letra == " ":
                plainText += " "
            else:
                indice = self.alfabeto.index(letra)
                indice = inverse_a * (indice - self.b) % self.mod
                plainText += self.alfabeto[indice]

        return plainText