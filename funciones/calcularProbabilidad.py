'''
BITS
'''
def calcularDistProbBits(bits):
    total_bits = len(bits)
    frecuencia_bits = {'0': bits.count('0') / total_bits, '1': bits.count('1') / total_bits}
    return frecuencia_bits

'''
BIGRAMAS
'''
def calcularDistProbBigramas(bits):
    total_bigramas = len(bits) - 1
    frecuencia_bigramas = {}
    for i in range(total_bigramas):
        bigrama = bits[i:i+2]
        if bigrama not in frecuencia_bigramas:
            frecuencia_bigramas[bigrama] = bits.count(bigrama) / total_bigramas
    return frecuencia_bigramas

'''
TRIGRAMAS
'''
def calcularDistProbTrigramas(bits):
    total_trigramas = len(bits) - 2
    frecuencia_trigramas = {}
    for i in range(total_trigramas):
        trigram = bits[i:i+3]
        if trigram not in frecuencia_trigramas:
            frecuencia_trigramas[trigram] = bits.count(trigram) / total_trigramas
    return frecuencia_trigramas

'''
MOSTRAR PROBABILIDAD
'''
import matplotlib.pyplot as plt

def mostrar_histograma(frecuencia_dict, title):
    etiquetas = list(frecuencia_dict.keys())
    frecuencias = list(frecuencia_dict.values())

    plt.bar(etiquetas, frecuencias)
    plt.xlabel('Elementos')
    plt.ylabel('Frecuencia')
    plt.title(title)
    plt.show()

'''
MAIN
'''
def main():
    cadena_bits = '101010101010111000111000'

    # BITS
    frecuencia_bits = calcularDistProbBits(cadena_bits)
    print(frecuencia_bits)
    mostrar_histograma(frecuencia_bits, 'Distribución de probabilidad de bits')

    # BIGRAMAS
    frecuencia_bigramas = calcularDistProbBigramas(cadena_bits)
    print(frecuencia_bigramas)
    mostrar_histograma(frecuencia_bigramas, 'Distribución de probabilidad de bigramas')

    # TRIGRAMAS
    frecuencia_trigramas = calcularDistProbTrigramas(cadena_bits)
    print(frecuencia_trigramas)
    mostrar_histograma(frecuencia_trigramas, 'Distribución de probabilidad de trigramas')

if __name__ == "__main__":
    main()