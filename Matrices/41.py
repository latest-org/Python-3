#-*-conding:utf-8-*-

'''41.	Leer dos matrices 5x5 enteras y determinar si el promedio entero de todos los elementos que no están en la diagonal de una matriz es igual al promedio entero de todos los elementos que no están en la diagonal de la otra matriz'''

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


    suma=0
    cont=0
    promedio=0
    for e in range(len(matriz)):
        for f in range(len(matriz)):
            numero=matriz[e][f]

            if [e]!=[f]:
                suma+=numero
                cont+=1
                promedio=suma//cont


    suma2=0
    cont2=0
    promedio2=0
    for g in range(len(matriz2)):
        for h in range(len(matriz2)):
            numero2=matriz2[g][h]

            if [g]!=[h]:
                suma2+=numero2
                cont2+=1
                promedio2=suma2//cont2

    print(" ")
    print("matriz 1: ",matriz)
    print("Matriz 2: ",matriz2)
    print(" ")
    print("Promedio de los elementos que no estan en la diagonal de la matriz 1: ",promedio)
    print("Promedio de los elementos que no estan en la diagonal de la matriz 2: ",promedio2)
    print(" ")

    if promedio==promedio2:
        print("Ambos promedios son iguales")

    else:
        print("Los promedios son diferentes")


except ValueError:
    print("El valor digitado debe ser numerico")
