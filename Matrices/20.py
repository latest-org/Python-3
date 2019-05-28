#-*-conding:utf-8-*-

'''20.	Leer dos matrices 4x5 entera, luego leer un entero y determinar si cada uno de los elementos de una de las matrices es igual a cada uno de los elementos de la otra matriz multiplicado por el entero leído'''

try:
    matriz=[]
    matriz2=[]
    multi2=0
    multi=0

    for a in range(3):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero para la primera matriz: "))
            fila.append(numeros)
        matriz.append(fila)

    print(" ")

    for c in range(3):
        fila2=[]
        for d in range(3):
            numeros2=int(input("Digite un numero para la segunda matriz: "))
            fila2.append(numeros)
        matriz2.append(fila2)

    print(" ")
    leido=int(input("Digite el numero que multiplicara las matrices: "))

    lista=[]
    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            numero=matriz[e][f]
            multi=numero*leido
            lista.append(multi)
    lista2=[]
    for g in range(len(matriz2)):
        for h in range(len(matriz2[g])):
            numero2=matriz2[g][h]
            multi2=numero2*leido
            lista2.append(multi2)

    print(" ")
    print("Matriz original 1: ",matriz)
    print("Matriz original 2: ",matriz2)
    print(" ")
    print("Numero que multiplicara las matrices: ",leido)
    print(" ")
    print("Matriz 1 multiplicada por el numero leido: ",lista)
    print("Matriz 2 multiplicada por el numero leido: ",lista2)

    if lista==lista2:
        print("Las matrices multiplicadas son iguales: ")

    else:
        print("Las matrices multiplicadas no son iguales")        


except ValueError:
    print("El valor digitado debe ser numerico")
