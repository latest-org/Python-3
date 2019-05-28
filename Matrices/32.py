#-*-conding:utf-8-*-

'''32.	Leer una matriz 4x6 entera y determinar en qué posiciones están los menores primos por fila'''

try:
    matriz=[]
    fil=0
    columna=0


    for a in range(3):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero entero: "))
            fila.append(numeros)
        matriz.append(fila)

    lista2=[]
    lista3=[]
    for c in range(len(matriz)):
        menor=matriz[c][0]
        for d in range(len(matriz[c])):
            primo=matriz[c][d]

            cont=0
            for e in range(1,primo+1):
                if (primo%e)==0:
                    cont+=1

            if cont==2:
                primo=primo

                if primo<=menor:
                    menor=primo
                    fil=c
                    columna=d
        lista2.append(primo)
        lista3.append([fil,columna])

    print("La matriz es:",matriz)
    print("los primos menores de cada fila son:",lista2)
    print("Y estan en las posiciones",lista3)

except ValueError:
    print("El valor digitado debe ser numerico")
