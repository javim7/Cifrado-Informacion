class Caesar():
    def __init__(self, texto, llave):
        self.texto = texto.lower()
        self.llave = llave
        self.alfabeto = "abcdefghijklmnñopqrstuvwxyz"
        self.mod = len(self.alfabeto)
        self.textoLimpio = self.limpiarTexto()
        self.cypherText = None
        self.porcentajes_letras = {
            'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86, 'E': 13.68,
            'F': 0.69, 'G': 1.01, 'H': 0.70, 'I': 6.25, 'J': 0.44,
            'K': 0.02, 'L': 4.97, 'M': 3.15, 'N': 6.71, 'Ñ': 0.31,
            'O': 8.68, 'P': 2.51, 'Q': 0.88, 'R': 6.87, 'S': 7.98,
            'T': 4.63, 'U': 3.93, 'V': 0.90, 'W': 0.01, 'X': 0.22,
            'Y': 0.90, 'Z': 0.52
        }
        self.nuevas_frecuencias = None

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
    
    def frecuencias(self):
        frecuencias = {}
        largo = 0
        for letra in self.cypherText:
            if letra in self.alfabeto:
                if letra in frecuencias:
                    frecuencias[letra] += 1
                    largo += 1
                else:
                    frecuencias[letra] = 1
                    largo += 1

        print(largo)
        for letra in frecuencias:
            frecuencias[letra] = frecuencias[letra] / largo * 100

        self.nuevas_frecuencias = frecuencias
        return frecuencias