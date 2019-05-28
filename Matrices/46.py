#-*-conding:utf-8-*-

'''46.	Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números menores cada fila de una matriz corresponde a alguno de los datos almacenados en las “esquinas” de la otra matriz'''

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

    for c in range(3):
        fila2=[]
        for d in range(3):
            numeros2=int(input("Digite un numero para la segunda matriz: "))
            fila2.append(numeros2)
        matriz2.append(fila2)

    lista=[]
    for e in range(len(matriz)):
        menor=matriz[e][0]
        for f in range(len(matriz[e])):
            numero=matriz[e][f]

            if numero<menor:
                menor=numero
        lista.append(menor)


    lista2=[]
    for g in range(len(matriz2)):
        menor2=matriz2[g][0]
        for h in range(len(matriz2[g])):
            numero2=matriz2[g][h]

            if numero2<menor2:
                menor2=numero2
        lista2.append(menor2)

    suma1=0
    cont1=0
    promedio1=0
    for i in range(len(lista)):
        suma1+=lista[i]
        cont1+=1
        promedio1=suma1//cont1

    suma2=0
    cont2=0
    promedio2=0
    for l in range(len(lista2)):
        suma2+=lista2[l]
        cont2+=2
        promedio2=suma2//cont2

    print(" ")
    print("Matriz 1:",matriz)
    print("Matriz 2:",matriz2)
    print(" ")
    print("Menores matriz 1: ",lista)
    print("Menores matriz 2: ",lista2)
    print(" ")
    print("Promedio menores matriz 1: ",promedio1)
    print("Promedio menores matriz 2: ",promedio2)

except ValueError:
    print("El valor digitado debe ser numerico")
