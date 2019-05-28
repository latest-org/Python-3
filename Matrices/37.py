#-*-conding:utf-8-*-

'''37.	Leer dos matrices 4x6 enteras y determinar si el número mayor de una matriz se encuentra en la misma posición exacta en la otra matriz'''

try:
    matriz=[]
    matriz2=[]


    for a in range(2):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)

    print(" ")

    for c in range(2):
        fila2=[]
        for d in range(3):
            numeros2=int(input("Digite un numero para la segunda matriz: "))
            fila2.append(numeros2)
        matriz2.append(fila2)

    mayor1=0

    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            numero=matriz[e][f]

            if  numero>mayor1:
                mayor1=numero
                pos1=e,f

    mayor2=0
    for g in range(len(matriz2)):
        for h in range(len(matriz2[g])):
            numero2=matriz2[g][h]

            if numero2>mayor2:
                mayor2=numero2
                pos2=g,h
    print(" ")
    print("Primera matriz: ",matriz)
    print("Segunda matriz: ",matriz2)
    print(" ")
    print("El mayor de la primera lista es: " + "%d"%mayor1)
    print("El mayor de la segunda lista es: " + "%d"%mayor2)
    print(" ")
    if mayor1==mayor2 and pos1==pos2:
        print("Ambos mayores son iguales y se encuentran en posiciones iguales: ",pos1)

    if mayor1==mayor2 and pos1!=pos2:
        print("Ambos mayores son iguales pero se encuentran en posiciones diferentes")

    if mayor1!=mayor2:
        print("Los dos mayores no son iguales")


except ValueError:
    print("El valor digitado debe ser numerico")
