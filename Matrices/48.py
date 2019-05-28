#-*-conding:utf-8-*-

'''48.	Leer dos matrices 5x5 entera y determinar si el promedio de los mayores elementos que pertenecen a la serie de Fibonacci de cada fila de una matriz es igual al promedio de los mayores elementos que pertenecen a la serie de Fibonacci de cada fila de la otra matriz'''

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

    numero1=0
    numero2=1
    numero3=0

    lista=[0]
    for e in range(0,10):
        numero3=numero2
        numero2=numero1
        numero1=numero3+numero2

        lista.append(numero1)

    print(lista)

    lista2=[]
    for f in range(len(matriz)):
        mayor=0
        for g in range(len(matriz[f])):
            numero=matriz[f][g]

            for h in range(len(lista)):
                numero2=lista[h]

                if numero==numero2:
                    if numero>mayor:
                        mayor=numero
        lista2.append(mayor)

    lista3=[]
    for i in range(len(matriz2)):
        mayor2=0
        for j in range(len(matriz2[i])):
            numero3=matriz2[i][j]

            for k in range(len(lista)):
                numero4=lista[k]

                if numero3==numero4:
                    if numero3>mayor2:
                        mayor2=numero3
        lista3.append(mayor2)


    suma=0
    promedio=0
    cont=0
    for l in range(len(lista2)):
        suma+=lista2[l]
        cont+=1
        promedio=suma//cont

    suma2=0
    promedio2=0
    cont2=0
    for m in range(len(lista3)):
        suma2+=lista3[m]
        cont2+=1
        promedio2=suma2//cont2

    print(" ")
    print("Matriz 1: ",matriz)
    print("Matriz 2: ",matriz2)
    print(" ")
    print("Serie Fibonacci")
    print("Mayores de cada fila de la matriz 1 que pertenecen a fibonaci: ",lista2)
    print("Mayores de cada fila de la matriz 2 que pertenecen a fibonaci: ",lista3)
    print(" ")
    print("Promedio de mayores matriz 1: ",promedio)
    print("Promedio de mayores matriz 2: ",promedio2)
    print(" ")

    if promedio==promedio2:
        print("Ambos promedios son iguales")

    else:

        print("Los promedios no son iguales")


except ValueError:
    print("El valor digitado debe ser numerico")
