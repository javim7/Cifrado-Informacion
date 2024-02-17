class Frecuencias():
    def __init__(self):
        self.alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        self.frecuenciasTeoricas = {
            'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86, 'E': 13.68,
            'F': 0.69, 'G': 1.01, 'H': 0.70, 'I': 6.25, 'J': 0.44,
            'K': 0.02, 'L': 4.97, 'M': 3.15, 'N': 6.71, 'Ñ': 0.31,
            'O': 8.68, 'P': 2.51, 'Q': 0.88, 'R': 6.87, 'S': 7.98,
            'T': 4.63, 'U': 3.93, 'V': 0.90, 'W': 0.01, 'X': 0.22,
            'Y': 0.90, 'Z': 0.52
        }

    def obtenerFrecuencias(self, texto):
        frecuencias = {letra : 0 for letra in self.alfabeto}
        largo = 0
        for letra in texto.replace(" ", ""):
            if letra in self.alfabeto:
                if frecuencias[letra] != 0:
                    frecuencias[letra] += 1
                    largo += 1
                else:
                    frecuencias[letra] = 1
                    largo += 1

        for letra in frecuencias:
            frecuencias[letra] = frecuencias[letra] / largo * 100

        return frecuencias
    
    def ordenarFrecuencias(self, frecuenciasExp):
        sortedExp = dict(sorted(frecuenciasExp.items(), key=lambda x: x[1], reverse=True))
        sortedTeo = dict(sorted(self.frecuenciasTeoricas.items(), key=lambda x: x[1], reverse=True))
        return sortedExp, sortedTeo
    
    def compararFrecuencias(self, pathViejo, pathNuevo):
        textosDecriptados = []
        with open(pathViejo, 'r') as file:
            textosDecriptados = [line.strip() for line in file]

        similitudes = []
        for line in textosDecriptados:
            key, value = line.split(" : ")
            frecuenciasDict = self.calcularFrecuencias(value)
            similitud = self.calcularSimilitud(frecuenciasDict)
            similitudes.append((key, similitud, value))

        textosSorteados = sorted(similitudes, key=lambda x: x[1])

        try:
            with open(pathNuevo, 'w') as file:
                for key, similitud, value in textosSorteados:
                    file.write("({}) : {}\n".format(key, value))
                print(f"Resultados escritos en: '{pathNuevo}'.")
        except Exception as e:
            print("Ha ocurrido un error: ", e)

    def calcularFrecuencias(self, texto):
        frecuenciasDict = {letra: texto.count(letra) / len(texto) for letra in self.alfabeto}
        return frecuenciasDict
    
    def calcularSimilitud(self, frecuenciasDict):
        similitud = sum((frecuenciasDict[letra] - self.frecuenciasTeoricas[letra])**2 for letra in self.alfabeto)
        return similitud
