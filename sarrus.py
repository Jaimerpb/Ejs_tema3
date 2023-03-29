#Para la implementación iterativa
#podemos utilizar la misma idea y fórmulas de la regla de Sarrus
#pero aplicando una optimización conocida como "eliminación gaussiana" para convertir la matriz en una matriz triangular superior
#lo que facilita el cálculo del determinante

def detSarrusIter(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(i+1, n):
            factor = matriz[j][i] / matriz[i][i]
            for k in range(i, n):
                matriz[j][k] -= factor * matriz[i][k]
    det = 1
    for i in range(n):
        det *= matriz[i][i]
    return det

