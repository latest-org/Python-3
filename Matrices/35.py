#-*-conding:utf-8-*-

'''35.	Leer dos matrices 4x6 enteras y determinar cuál es el mayor dato almacenado en ella que pertenezca a la Serie de Fibonacci'''

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

    for q in range(3):
        fila2=[]
        for r in range(3):
            numeros2=int(input("Digite un numero para la segunda lista: "))
            fila2.append(numeros2)
        matriz2.append(fila2)

    numero1=0
    numero2=1
    numero3=0

    lista=[0]

    for c in range(0,10):
        numero3=numero2
        numero2=numero1
        numero1=numero3+numero2

        lista.append(numero1)

    cont=0
    lista2=[]
    mayor1=0
    for d in range(len(matriz)):
        for e in range(len(matriz[d])):
            numero=matriz[d][e]

            for f in range(len(lista)):
                numero2=lista[f]

                if numero==numero2:
                    if numero>mayor1:
                        mayor1=numero

    cont2=0
    lista3=[]
    mayor2=0
    for z in range(len(matriz2)):
        for x in range(len(matriz2[z])):
            numero3=matriz2[z][x]

            for l in range(len(lista)):
                numero4=lista[l]

                if numero3==numero4:
                    if numero3>mayor2:
                        mayor2=numero3

    print(" ")
    print("Matriz 1: ",matriz)
    print("Matriz 2: ",matriz2)
    print(" ")
    print("Serie fibonacci: ",lista)
    print(" ")
    print("Numero mayor perteneciente a fibonacci de la matriz 1: ",mayor1)
    print("Numero mayor pertenenciente a fibonacci de la matriz 2: ",mayor2)
    print(" ")

except ValueError:
    print("El valor digitado debe ser numerico")
