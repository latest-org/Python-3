#-*-conding:utf-8-*-

'''26.	Leer dos matrices 4x5 enteras y determinar si la cantidad de números pares almacenados en una matriz es igual a la cantidad de números pares almacenados en la otra matriz'''


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

    cont1=0
    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            numero=matriz[e][f]

            if numero%2==0:
                cont1+=1

    cont2=0
    for g in range(len(matriz2)):
        for h in range(len(matriz2[g])):
            numero2=matriz2[g][h]

            if numero2%2==0:
                cont2+=1
    print(" ")
    print("Pares primera matriz: ",cont1)
    print("Pares segunda matriz: ",cont2)
    print(" ")

    if cont1==cont2:
        print("Ambas matrices tienen la misma cantidad de numeros pares")

    else:
        print("Las matrices tienen diferente cantidad de numeros pares")

except ValueError:
    print("El valor digitado debe ser numerico")
