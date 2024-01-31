class Frecuencias:
    def __init__(self, cypherText):
        self.cypherText = cypherText
        self.alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        self.porcentajes_letras = {
            'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86, 'E': 13.68,
            'F': 0.69, 'G': 1.01, 'H': 0.70, 'I': 6.25, 'J': 0.44,
            'K': 0.02, 'L': 4.97, 'M': 3.15, 'N': 6.71, 'Ñ': 0.31,
            'O': 8.68, 'P': 2.51, 'Q': 0.88, 'R': 6.87, 'S': 7.98,
            'T': 4.63, 'U': 3.93, 'V': 0.90, 'W': 0.01, 'X': 0.22,
            'Y': 0.90, 'Z': 0.52
        }
        self.nuevas_frecuencias = None
        self.sortedOg = None
        self.sortedNew = None

    def frecuencias(self):
        frecuencias = {letra : 0 for letra in self.alfabeto}
        largo = 0
        for letra in self.cypherText.replace(" ", ""):
            if letra in self.alfabeto:
                if frecuencias[letra] != 0:
                    frecuencias[letra] += 1
                    largo += 1
                else:
                    frecuencias[letra] = 1
                    largo += 1

        for letra in frecuencias:
            frecuencias[letra] = frecuencias[letra] / largo * 100

        self.nuevas_frecuencias = frecuencias
        return frecuencias
    
    def sortedFrecuencias(self):
        self.sortedNew = dict(sorted(self.frecuencias().items(), key=lambda x: x[1], reverse=True))
        self.sortedOg = dict(sorted(self.porcentajes_letras.items(), key=lambda x: x[1], reverse=True))
        return self.sortedNew, self.sortedOg
