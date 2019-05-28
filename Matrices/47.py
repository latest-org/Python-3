#-*-conding:utf-8-*-

'''47.	Leer dos matrices 5x5 enteras y determinar si el promedio de los mayores números primos por cada fila de una matriz es igual al promedio de los mayores números primos por cada columna de la otra matriz'''

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

            cont1=0
            for g in range(1,numero+1):
                if (numero%g)==0:
                    cont1+=1
            if cont1==2:
                if numero<menor:
                    menor=numero
        lista.append(menor)


    lista2=[]
    for h in range(len(matriz2)):
        menor2=matriz2[h][0]
        for i in range(len(matriz2[h])):
            numero2=matriz2[h][i]

            cont2=0
            for j in range(1,numero2+1):
                if (numero2%j)==0:
                    cont2+=1
            if cont2==2:
                if numero2<menor2:
                    menor2=numero2
        lista2.append(menor2)


except ValueError:
    print("El valor digitado debe ser numerico")
