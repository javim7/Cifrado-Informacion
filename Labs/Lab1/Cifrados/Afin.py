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
    
    def encrypt3(self, plainText, a, b):
        cypherText = ""
        for letra in plainText:
            if letra not in self.alfabeto:
                cypherText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice = (a * indice + b) % self.mod
                cypherText += self.alfabeto[indice]

        self.cypherText = cypherText
        return cypherText
    
    def encrypt2(self, plainText, a ,b):
        cypherText = ""
        for letra in plainText:
            if letra not in self.alfabeto:
                cypherText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice = (a * indice + b) % self.mod
                cypherText += self.alfabeto[indice]

        return cypherText
    
    def inverso(self):
        for i in range(self.mod):
            if (self.a * i) % self.mod == 1:
                return i
        return -1

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
    
    def inverso2(self, a):
        for i in range(self.mod):
            if (a * i) % self.mod == 1:
                return i
        return -1

    def decrypt2(self, cypherText, a, b):
        plainText = ""
        inverse_a = self.inverso2(a)
        if inverse_a == -1:
            pass
        for letra in cypherText:
            if letra not in self.alfabeto:
                plainText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice = inverse_a * (indice - b) % self.mod
                plainText += self.alfabeto[indice]

        return plainText
    
    def fuerzaBruta(self, texto, sortedOG, sortedNew):
        firstOg = next(iter(sortedOG.keys()))
        secondOg = next(iter(sortedOG.keys()))

        firstNew = next(iter(sortedNew.keys()))
        secondNew = next(iter(sortedNew.keys()))

        aKey = (self.alfabeto.index(firstNew) - self.alfabeto.index(firstOg)) % self.mod
        bKey = (self.alfabeto.index(secondNew) - self.alfabeto.index(secondOg)) % self.mod

        dictionary = {}
        for i in range(aKey, aKey + self.mod):
            current_a = i % self.mod
            for j in range(bKey, bKey + self.mod):
                current_b = j % self.mod
                plainText = self.decrypt2(texto, current_a, current_b)
                # print(current_a, current_b, plainText[:20])
                dictionary[(current_a, current_b)] = plainText
        
        for key, value in dictionary.items():
            print("a: " + str(key[0]) + " b: " + str(key[1]) + " Texto: " + value[:20])
