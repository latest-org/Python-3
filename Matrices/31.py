#-*-conding:utf-8-*-

'''31.	Leer una matriz 4x6 entera y determinar en qué posiciones están los menores por fila'''

matriz=[]
fil=0
columna=0

try:

    for a in range(3):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)


    lista=[]
    lista2=[]
    for c in range(len(matriz)):
        menor=matriz[c][0]
        for d in range(len(matriz[c])):
            numero=matriz[c][d]

            if numero<=menor:
                menor=numero
                fil=c
                columna=d
                pos=fil,columna

        lista.append([fil,columna])
        lista2.append(menor)

    print("matriz",matriz)
    print("menores",lista2)
    print("posicion de cada uno",lista)

except ValueError:
    print("El valor digitado debe ser numerico")
