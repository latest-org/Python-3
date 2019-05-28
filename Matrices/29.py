#-*-conding:utf-8-*-

'''29.	Leer una matriz 4x6 entera y determinar si alguno de sus números está repetido al menos 3 veces'''


try:
    matriz=[]
    lista=[]

    for a in range(2):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)

    for c in range(len(matriz)):
        for d in range(len(matriz[c])):
            numero=matriz[c][d]

            cont=0
            for f in range(len(matriz)):
                for g in range(len(matriz[f])):
                    if matriz[f][g]==numero:
                        cont+=1

            if cont>3:
                lista.append(matriz[f][g])
                print(cont)


    if len(lista)==0:
        print("No hay ni un numero que este repetido al menos 3 veces en la matriz")


    else:
        print("Hay al menos un numero repetido 3 veces en la matriz")


except ValueError:
    print("El valor digitado debe ser numerico")
