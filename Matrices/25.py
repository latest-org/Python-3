#-*-conding:utf-8-*-

'''25.	Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las matrices es también el mayor número primo de la otra matriz'''

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
        for f in range(len(matriz)):
            primo=matriz[e][f]

            cont1=0
            for g in range(1,primo+1):
                if (primo%g)==0:
                    cont1+=1

            if cont1==2:
                if primo>mayor_matriz1:
                    mayor_matriz1=primo


    mayor_matriz2=0
    for h in range(len(matriz2)):
        for i in range(len(matriz2)):
            primo2=matriz2[h][i]

            cont2=0
            for j in range(1,primo2+1):
                if (primo2%j)==0:
                    cont2+=1

            if cont2==2:
                if primo2>mayor_matriz2:
                    mayor_matriz2=primo2

    print(" ")
    print("Primo mayor primera matriz",mayor_matriz1)
    print("Primo mayor segunda matriz",mayor_matriz2)
    print(" ")
        
    if mayor_matriz1==mayor_matriz2:
        print("El primo mayor de una matriz es tambien el mayor de la otra matriz")

    else:
        print("El primo mayor de una matriz no es el mayor de la otra matriz")

except ValueError:
    print("El valor digitado debe ser numerico")
