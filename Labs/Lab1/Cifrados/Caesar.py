class Caesar():
    def __init__(self, texto, llave, alfabeto):
        self.texto = texto.upper()
        self.llave = llave
        self.alfabeto = alfabeto
        self.mod = len(self.alfabeto)
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
        for letra in self.textoLimpio:
            if letra not in self.alfabeto:
                cypherText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice += self.llave
                indice = indice % self.mod
                cypherText += self.alfabeto[indice]

        self.cypherText = cypherText
        return cypherText
    
    def encrypt2(self, plainText):
        cypherText = ""
        for letra in plainText:
            if letra not in self.alfabeto:
                cypherText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice += self.llave
                indice = indice % self.mod
                cypherText += self.alfabeto[indice]

        return cypherText

    def decrypt(self):
        plainText = ""
        for letra in self.cypherText:
            if letra not in self.alfabeto:
                plainText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice -= self.llave
                indice = indice % self.mod
                plainText += self.alfabeto[indice]

        return plainText
    
    def decrypt2(self, cypherText, llave):
        plainText = ""
        for letra in cypherText:
            if letra not in self.alfabeto:
                plainText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice -= llave
                indice = indice % self.mod
                plainText += self.alfabeto[indice]

        return plainText
    
    def fuerzaBruta(self, sortedOg, sortedNew):
        firstOg = next(iter(sortedOg.keys()))
        firstNew = next(iter(sortedNew.keys()))

        key = (self.alfabeto.index(firstNew) - self.alfabeto.index(firstOg)) % self.mod
        print(firstOg, firstNew, key)

        dict = {}
        for i in range(key, key + self.mod):
            current_key = i % self.mod

            plainText = self.decrypt2(self.cypherText, current_key)
            dict[current_key] = plainText
            print("Key: {:2d} Text: {}".format(current_key, plainText))

        puedeSer = ''
        for key, value in dict.items():
            if value == self.textoLimpio:
                puedeSer = value
                # print("Key: {:2d} Text: {}".format(key, value))
                break

        if self.encrypt2(puedeSer) == self.cypherText:
            # print("Key: {:2d} Text: {}".format(key, value))
            print("Key: {:2d}".format(key))
            print("Text: {}".format(value))

        

