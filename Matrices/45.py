#-*-conding:utf-8-*-

'''45.	Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números mayores de cada fila de una matriz es igual al promedio de los números mayores de cada fila de la otra matriz'''

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

    mayor=0
    lista=[]
    for e in range(len(matriz)):
        for f in range(len(matriz[d])):
            numero=matriz[e][d]

            if numero>mayor:
                mayor=numero

        lista.append(mayor)

    mayor2=0
    lista2=[]
    for g in range(len(matriz[2])):
        for h in range(len(matriz[2])):
            numero2=matriz2[g][h]

            if numero2>mayor2:
                mayor2=numero2
        lista2.append(mayor2)

    suma1=0
    promedio1=0
    cont1=0
    for i in range(len(lista)):
        suma1+=lista[i]
        cont1+=1
        promedio1=suma1//cont1

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
    print("Mayores de cada fila matriz 1: ",lista)
    print("Mayores de cada fila matriz 2: ",lista2)
    print(" ")
    print("Promedio mayores matriz 1: ",promedio1)
    print("Promedio mayores matriz 2: ",promedio2)
    print(" ")

    if promedio1==promedio2:
        print("Ambos promedios son iguales:")

    else:
        print("Los dos promedios no son iguales")

except ValueError:
    print("El valor digitado debe ser numerico")
