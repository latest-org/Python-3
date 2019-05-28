#-*-conding:utf-8-*-

'''24.	Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las matrices también se encuentra en la otra matriz'''

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

    mayor_matriz1=0
    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            primo=matriz[e][f]

            cont=0
            for g in range(1,primo+1):
                if (primo%g)==0:
                    cont+=1

            if cont==2:
                if primo>mayor_matriz1:
                    mayor_matriz1=primo


    mayor_matriz2=0
    for h in range(len(matriz2)):
        for i in range(len(matriz2[h])):
            primo2=matriz2[h][i]

            cont2=0
            for j in range(1,primo2+1):
                if (primo2%j)==0:
                    cont2+=1

            if cont2==2:
                if primo2>mayor_matriz2:
                    mayor_matriz2=primo2


    cont3=0
    for k in range(len(matriz)):
        for l in range(len(matriz[k])):
            numero=matriz[k][l]

            if numero==mayor_matriz2:
                cont3+=1
    cont4=0
    for m in range(len(matriz2)):
        for n in range(len(matriz2)):
            numero2=matriz2[m][n]

            if numero2==mayor_matriz1:
                cont4+=1

    print(" ")
    print("Primo mayor primera matriz: ",mayor_matriz1)
    print("Primo mayor segunda matriz: ",mayor_matriz2)
    print(" ")

    if cont4>0:
        print("El primo mayor de la primera matriz esta en la segunda")

    if cont4==0:
        print("El primo mayor de la primera matriz no esta en la segunda")

    if cont3>0:
        print("El primo mayor de la segunda matriz esta en la primera matriz")

    if cont3==0:
        print("El primo mayor de la segunda matriz no esta en la primera matriz")


except ValueError:
    print("El valor digitado debe ser numerico")
