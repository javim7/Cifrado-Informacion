class Caesar():
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
    
    def encrypt(self, texto, clave):
        textoLimpiado = self.limpiarTexto(texto)
        cypherText = ""
        for letra in textoLimpiado:
            if letra not in self.alfabeto:
                cypherText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice += clave
                indice = indice % len(self.alfabeto)
                cypherText += self.alfabeto[indice]

        return cypherText
    
    def decrypt(self, cypherText, clave):
        plainText = ""
        for letra in cypherText:
            if letra not in self.alfabeto:
                plainText += letra
            else:
                indice = self.alfabeto.index(letra)
                indice -= clave
                indice = indice % len(self.alfabeto)
                plainText += self.alfabeto[indice]

        return plainText
    
    def fuerzaBruta(self, texto, sortedOg, sortedNew, output=None):
        firstOg = next(iter(sortedOg.keys()))
        firstNew = next(iter(sortedNew.keys()))

        key = (self.alfabeto.index(firstNew) - self.alfabeto.index(firstOg)) % len(self.alfabeto)
        # print(firstOg, firstNew, key)

        dict = {}
        for i in range(key, key + len(self.alfabeto)):
            current_key = i % len(self.alfabeto)

            plainText = self.decrypt(texto, current_key)
            dict[current_key] = plainText
            # print("Key: {:2d} Text: {}".format(current_key, plainText))

        if output is None:
            output = 'Labs/Lab1/Textos/caesar.txt'
        
        output_file_path = output
        try:
            with open(output_file_path, 'w') as output_file:
                for key, value in dict.items():
                    output_file.write("{} : {}\n".format(key, value))
            print(f"Resultados escritos en: '{output_file_path}'.")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")