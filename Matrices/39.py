#-*-conding:utf-8-*-

'''39.	Leer dos matrices 4x6 enteras y determinar si el promedio de las “esquinas” de una matriz es igual al promedio de las “esquinas” de la otra matriz'''

try:
    matriz=[]
    matriz2=[]


    for a in range(3):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)

    print(" ")

    for c in range(len(matriz)):
        for d in range(len(matriz[c])):
            numero=matriz[c][d]

    print(matriz[0][0])
    print(matriz[c][3])

except ValueError:
    print("El valor digitado debe ser numerico")
