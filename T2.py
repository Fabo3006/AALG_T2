import random

# Crear matriz NxN
def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(random.randint(99, 999))
        matriz.append(fila)
    return matriz

# Mostrar matriz
def mostrar_matriz(matriz):
    print("\nMATRIZ GENERADA:\n")
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:4}", end=" ")
        print()

# Divide y vencerás para contar múltiplos en una fila
def contar_fila(fila, inicio, fin):
    if inicio == fin:
        if fila[inicio] % 5 == 0 or fila[inicio] % 7 == 0:
            return 1
        return 0

    medio = (inicio + fin) // 2

    izquierda = contar_fila(fila, inicio, medio)
    derecha = contar_fila(fila, medio + 1, fin)

    return izquierda + derecha

# Divide y vencerás para contar en la matriz
def contar_matriz(matriz, inicio_fila, fin_fila):
    if inicio_fila == fin_fila:
        return contar_fila(
            matriz[inicio_fila],
            0,
            len(matriz[inicio_fila]) - 1
        )

    medio = (inicio_fila + fin_fila) // 2

    superior = contar_matriz(matriz, inicio_fila, medio)
    inferior = contar_matriz(matriz, medio + 1, fin_fila)

    return superior + inferior

# Programa principal
def main():
    n = int(input("Ingrese el tamaño N de la matriz cuadrada NxN: "))

    matriz = crear_matriz(n)

    mostrar_matriz(matriz)

    cantidad = contar_matriz(matriz, 0, n - 1)

    print("\nCantidad de números múltiplos de 5 o 7:", cantidad)

main()