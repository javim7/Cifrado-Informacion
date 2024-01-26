class Caesar():
    def __init__(self, texto, llave):
        self.texto = texto.upper()
        self.llave = llave
        self.alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        self.mod = len(self.alfabeto)
        self.textoLimpio = self.limpiarTexto()
        self.cypherText = None

    def limpiarTexto(self):
        textoLimpio = ""
        for letra in self.texto:
            if letra == " ":
                textoLimpio += " "
            elif letra in self.alfabeto:
                textoLimpio += letra.upper()
            elif letra.upper() in ['á', 'é', 'í', 'ó', 'ú']:
                # Reemplazar letras con tilde
                letra_sin_tilde = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}[letra.upper()]
                textoLimpio += letra_sin_tilde
        return textoLimpio

    def encrypt(self):
        cypherText = ""
        for letra in self.textoLimpio:
            if letra == " ":
                cypherText += " "
            else:
                indice = self.alfabeto.index(letra)
                indice += self.llave
                indice = indice % self.mod
                cypherText += self.alfabeto[indice]

        self.cypherText = cypherText
        return cypherText

    def decrypt(self):
        plainText = ""
        for letra in self.cypherText:
            if letra == " ":
                plainText += " "
            else:
                indice = self.alfabeto.index(letra)
                indice -= self.llave
                indice = indice % self.mod
                plainText += self.alfabeto[indice]

        return plainText