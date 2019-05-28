#-*-conding:utf-8-*-

'''40.	Leer dos matrices 5x5 enteras y determinar si el promedio entero de los elementos de la diagonal de una matriz es igual al promedio de los elementos de la diagonal de la otra matriz'''


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
        for f in range(len(matriz)):
            numero=matriz[e][f]

            if [e]==[f]:
                lista.append(numero)

    lista2=[]
    for g in range(len(matriz2)):
        for h in range(len(matriz2)):
            numero2=matriz2[g][h]

            if [g]==[h]:
                lista2.append(numero2)

    suma=0
    promedio=0
    cont=0
    for i in range(len(lista)):
        suma+=lista[i]
        cont+=1
        promedio=suma//cont

    suma2=0
    promedio2=0
    cont2=0
    for j in range(len(lista2)):
        suma2+=lista2[j]
        cont2+=1
        promedio2=suma2//cont2

    print(" ")
    print("Matriz 1: ",matriz)
    print("Matriz 2: ",matriz2)
    print(" ")
    print("Elementos de la diagonal de la matriz 1: ",lista)
    print("Elementos de la diagonal de la matriz 2: ",lista2)
    print(" ")
    print("Promedio de los elementos de la diagonal matriz 1: ",promedio)
    print("Promedio de los elementos de la diagonal matriz 2: ",promedio2)
    print(" ")

    if promedio==promedio2:
        print("Ambos promedios son iguales")

    else:
        print("Los promedios son diferentes")


except ValueError:
    print("El valor digitado debe ser numerico")
