class Afin():
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
    
    def encrypt(self, texto, a, b):
        textoLimpiado = self.limpiarTexto(texto)
        cypherText = ""
        for letra in textoLimpiado:
            if letra not in self.alfabeto:
                cypherText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice = (a * indice + b) % len(self.alfabeto)
                cypherText += self.alfabeto[indice]

        return cypherText
    
    def inverso(self, a):
        for i in range(len(self.alfabeto)):
            if (a * i) % len(self.alfabeto) == 1:
                return i
        return -1

    def decrypt(self, cypherText, a, b):
        plainText = ""
        inverse_a = self.inverso(a)
        if inverse_a == -1:
            pass
        for letra in cypherText:
            if letra not in self.alfabeto:
                plainText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice = (inverse_a * (indice - b)) % len(self.alfabeto)
                plainText += self.alfabeto[indice]

        return plainText
    
    def fuerzaBruta(self, texto, sortedTeo, sortedExp, output=None):
        firstTeo = next(iter(sortedTeo.keys()))
        secondTeo = next(iter(sortedTeo.keys()))

        firstExp = next(iter(sortedExp.keys()))
        secondExp = next(iter(sortedExp.keys()))

        aKey = (self.alfabeto.index(firstExp) - self.alfabeto.index(firstTeo)) % len(self.alfabeto)
        bKey = (self.alfabeto.index(secondExp) - self.alfabeto.index(secondTeo)) % len(self.alfabeto)

        dictionary = {}
        for i in range(aKey, aKey + len(self.alfabeto)):
            current_a = i % len(self.alfabeto)
            for j in range(bKey, bKey + len(self.alfabeto)):
                current_b = j % len(self.alfabeto)
                plainText = self.decrypt(texto, current_a, current_b)
                # print(current_a, current_b, plainText[:20])
                dictionary[(current_a, current_b)] = plainText
        
        if output is None:
            output = "Labs/Lab1/Textos/afin.txt"
        output_file_path = output
        try:
            with open(output_file_path, 'w') as file:
                for key, value in dictionary.items():
                    file.write("({:2d},{:2d}) : {}\n".format(key[0], key[1], value))
                print(f"Resultados escritos en: '{output_file_path}'.")
        except Exception as e:
            print("Ha ocurrido un error: ", e)