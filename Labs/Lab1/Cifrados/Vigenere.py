import math
import statistics
from tqdm import tqdm
from itertools import product

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
    
    def obtenerLongitud(self, cypherText):
        coincidenciasDict = {}
        coincidenciasList = []
        spaces = ' '
        # print(cypherText)
        for i in range(1, len(cypherText)):
            newText = spaces * i + cypherText[:-i]
            # print(newText)
            cuentaCoincidencias = 0
            for j in range(len(cypherText)):
                if cypherText[j] == newText[j]:
                    cuentaCoincidencias += 1
            coincidenciasDict[newText] = cuentaCoincidencias
            coincidenciasList.append(cuentaCoincidencias)
        
        # print(len(coincidenciasList))
        # print(coincidenciasList)
        minVal, maxVal, meanVal, medianVal = min(coincidenciasList), max(coincidenciasList), statistics.mean(coincidenciasList), statistics.median(coincidenciasList)
        # print(f'Min: {minVal}, Max: {maxVal}, Mean: {meanVal}, Median: {medianVal}')

        saltos = []
        numeroGrande = maxVal * 0.666
        saltosDados = 0
        for i in range(len(coincidenciasList)):
            saltosDados += 1
            if coincidenciasList[i] > numeroGrande:
                saltos.append(saltosDados)
                saltosDados = 0
        
        # print(saltos)
        sinOutliers = self.quitarOutliers(saltos)
        # print(sinOutliers)
        meanVal = statistics.mean(sinOutliers)
        # print(meanVal)
        return math.floor(meanVal)

    def quitarOutliers(self, lista):
        # calcular el primer y tercer cuartil
        q1 = statistics.median(lista[:len(lista)//2])
        q3 = statistics.median(lista[len(lista)//2:])

        # Calcular el rango intercuartil
        iqr = q3 - q1

        # Definir los límites
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # filtrar los datos
        filtered_lista = [num for num in lista if lower_bound <= num <= upper_bound]

        return filtered_lista
    
    def fuerzaBruta(self, cypherText, longitud, output=None):
        combinaciones = product(self.alfabeto, repeat=longitud)
        
        dict = {}
        for llave in tqdm(combinaciones, desc="Progreso", total=len(self.alfabeto) ** longitud):
            llave = ''.join(llave)
            plainText = self.decrypt(cypherText, llave)
            dict[llave] = plainText

        if output is None:
            output = "Labs/Lab1/Textos/vigenere.txt"
        output_file_path = output
        try:
            with open(output_file_path, 'w') as file:
                for key, value in dict.items():
                    file.write("({}) : {}\n".format(key, value))
                print(f"Resultados escritos en: '{output_file_path}'.")
        except Exception as e:
            print("Ha ocurrido un error: ", e)
    
    def fuerzaBruta2(self, cypherText, longitud, output=None):
        primerasLetras = 'BE'
        longitudRes = longitud - len(primerasLetras)

        combinacionesRes = product(self.alfabeto, repeat=longitudRes)
        
        dict = {}
        for llave in tqdm(combinacionesRes, desc="Progreso", total=len(self.alfabeto) ** longitudRes):
            llave = primerasLetras + ''.join(llave)
            plainText = self.decrypt(cypherText, llave)
            dict[llave] = plainText

        if output is None:
            output = "Labs/Lab1/Textos/vigenere.txt"
        output_file_path = output
        try:
            with open(output_file_path, 'w') as file:
                for key, value in dict.items():
                    file.write("({}) : {}\n".format(key, value))
                print(f"Resultados escritos en: '{output_file_path}'.")
        except Exception as e:
            print("Ha ocurrido un error: ", e)

            

        
       