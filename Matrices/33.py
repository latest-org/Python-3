#-*-conding:utf-8-*-

'''33.	Leer una matriz 4x6 entera y determinar en qué posiciones están los menores pares por fila'''

try:

    matriz=[]
    fil=0
    columna=0

    for a in range(4):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero entero: "))
            fila.append(numeros)
        matriz.append(fila)


    lista=[]
    lista2=[]
    for c in range(len(matriz)):
        menor=matriz[c][0]
        for d in range(len(matriz[c])):
            par=matriz[c][d]

            if par%2==0:
                if par<menor:
                    menor=par
                    pos=c,

        lista2.append(menor)

    print(matriz)
    print(lista2)


except ValueError:
    print("El valor digitado debe ser numerico")
