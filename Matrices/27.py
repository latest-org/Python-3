#-*-conding:utf-8-*-

'''27.	Leer dos matrices 4x5 enteras y determinar si la cantidad de números primos almacenados en una matriz es igual a la cantidad de números primos almacenados en la otra matriz'''

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

    primos_matriz1=[]
    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            primo=matriz[e][f]

            cont1=0
            for g in range(1,primo+1):
                if (primo%g)==0:
                    cont1+=1

            if cont1==2:
                primos_matriz1.append(primo)

    primos_matriz2=[]
    for h in range(len(matriz2)):
        for i in range(len(matriz2[h])):
            primo2=matriz2[h][i]

            cont2=0
            for j in range(1,primo2+1):
                if (primo2%j)==0:
                    cont2+=1

            if cont2==2:
                primos_matriz2.append(primo2)

    cont3=0
    for k in range(len(primos_matriz1)):
        cont3+=1

    cont4=0
    for l in range(len(primos_matriz2)):
        cont4+=1

    print(" ")
    print("Cantidad de primos primera matriz: ",cont3)
    print("Cantidad de primos segunda matriz: ",cont4)
    print(" ")

    if cont3==cont4:
        print("Ambas matrices tienen la misma cantidad de numeros primos")

    else:
        print("Las matrices no tienen la misma cantidad de numeros primos")
except ValueError:
    print("El valor digitado debe ser numerico")
