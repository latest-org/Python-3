#-*-conding:utf-8-*-

'''38.	Leer dos matrices 4x6 enteras y determinar si el mayor número primo de una matriz está repetido en la otra matriz'''

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

    mayor=0
    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            numero=matriz[e][f]

            cont=0
            for g in range(1,numero+1):
                if (numero%g)==0:
                    cont+=1

            if cont==2:
                if numero>mayor:
                    mayor=numero

    mayor1=0

    for h in range(len(matriz2)):
        for i in range(len(matriz2[h])):
            numero2=matriz2[h][i]

            cont1=0
            for j in range(1,numero2+1):
                if (numero2%j)==0:
                    cont1+=1

            if cont1==2:
                if numero2>mayor1:
                    mayor1=numero2



    cont2=0
    for k in range(len(matriz)):
        for l in range(len(matriz[k])):
            numero3=matriz[k][l]
            if numero3==mayor1:
                cont2+=1

    cont3=0
    for m in range(len(matriz2)):
        for n in range(len(matriz2[m])):
            numero4=matriz2[m][n]

            if numero4==mayor:
                cont3+=1

    print(" ")
    print("Matriz 1: ",matriz)
    print("Matriz 2: ",matriz2)
    print(" ")
    print("Primo mayor matriz 1: ",mayor)
    print("Primo mayor matriz 2: ",mayor1)
    print(" ")
    
    if cont3>0:
        print("El mayor de la primera matriz esta repetido en la segunda")

    elif cont2>0:
        print("El mayor primo de la segunda matriz esta repetido en la primera matriz")

    else:
        print("Ninguno de los dos primos mayores esta ubicado en la otra matriz")

except ValueError:
    print("El valor digitado debe ser numerico")
