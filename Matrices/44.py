#-*-conding:utf-8-*-

'''44.	Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números terminados en 4 de una matriz se encuentra al menos 3 veces en la otra matriz'''

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


    suma1=0
    promedio1=0
    lista=[]
    cont1=0
    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            numero=matriz[e][f]

            if numero%10==4:
                cont1+=1
                suma1+=numero
                promedio1=suma1//cont1
                lista.append(numero)

    suma2=0
    promedio2=0
    lista2=[]
    cont2=0
    for h in range(len(matriz2)):
        for i in range(len(matriz2[h])):
            numero2=matriz2[h][i]

            if numero2%10==4:
                cont2+=1
                suma2+=numero2
                promedio2=suma2//cont2
                lista2.append(numero2)

    cont3=0
    for k in range(len(matriz)):
        for l in range(len(matriz[k])):
            numero3=matriz[k][l]

            if numero3==promedio2:
                cont3+=1


    cont4=0
    for m in range(len(matriz2)):
        for n in range(len(matriz2[m])):
            numero4=matriz2[m][n]

            if numero4==promedio1:
                cont4+=1

    print(" ")
    print("Matriz1: ",matriz)
    print("Matriz2: ",matriz2)
    print(" ")
    print("Numeros terminados en 4 matriz1: ",lista)
    print("Numeros terminados en 4 matriz2: ",lista2)
    print(" ")
    print("Promedio terminados en 4 matriz1: ",promedio1)
    print("Promedio terminados en 4 matriz2: ",promedio2)
    print(" ")

    if cont4>2:
        print("El promedio de los numeros terminados en 4 de la matriz 1 se encuentra por lo menos 3 veces en la matriz 2")

    if cont3>2:
        print("El promedio de los numeros terminados en 4 de la matriz 2 se encuentra por lo menos 3 veces en la matriz 1")


except ValueError:
    print("El valor digitado debe ser numerico")
