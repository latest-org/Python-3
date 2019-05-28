#-*-conding:utf-8-*-

'''23.	Leer dos matrices 4x5 enteras y determinar si el número mayor de una de las matrices es igual al número mayor de la otra matriz'''

try:
    matriz=[]
    matriz2=[]

    for a in range(4):
        fila=[]
        for b in range(5):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)

    print(" ")

    for c in range(4):
        fila2=[]
        for d in range(5):
            numeros2=int(input("Digite un numero para la segunda matriz: "))
            fila2.append(numeros2)
        matriz2.append(fila2)

    mayor1=0
    for e in range(len(matriz)):
        for f in range(len(matriz)):
            numero=matriz[e][f]

            if numero>mayor1:
                mayor1=numero

    mayor2=0
    for g in range(len(matriz2)):
        for h in range(len(matriz2)):
            numero2=matriz2[g][h]

            if numero2>mayor2:
                mayor2=numero2

    print(mayor1)
    print(mayor2)            

    if mayor1==mayor2:
        print("Los numeros mayores de ambas listas son iguales")

    else:
        print("Los numeros mayores de ambas listas no son iguales")

except ValueError:
    print("El valor digitado debe ser numerico")
