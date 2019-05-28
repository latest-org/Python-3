#-*-conding:utf-8-*-

'''42.	Leer dos matrices 5x5 enteras y determinar si el promedio entero de los números primos de una matriz se encuentra almacenado en la otra matriz'''

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


    suma1=0
    promedio1=0
    lista=[]
    cont2=0
    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            numero=matriz[e][f]

            cont1=0
            for g in range(1,numero+1):
                if (numero%g)==0:
                    cont1+=1
            if cont1==2:
                cont2+=1
                suma1+=numero
                promedio1=suma1//cont2
                lista.append(numero)


    suma2=0
    promedio2=0
    lista2=[]
    cont4=0
    for h in range(len(matriz2)):
        for i in range(len(matriz2[h])):
            numero2=matriz2[h][i]

            cont3=0
            for j in range(1,numero2+1):
                if (numero2%j)==0:
                    cont3+=1
            if cont3==2:
                cont4+=1
                suma2+=numero2
                promedio2=suma2//cont4
                lista2.append(numero2)

    cont5=0
    for k in range(len(matriz)):
        for l in range(len(matriz[k])):
            numero3=matriz[k][l]

            if numero3==promedio2:
                cont5+=1


    cont6=0
    for m in range(len(matriz2)):
        for n in range(len(matriz2[m])):
            numero4=matriz2[m][n]

            if numero4==promedio1:
                cont6+=1

    print(" ")
    print("matriz1: ",matriz)
    print("matriz2: ",matriz2)
    print(" ")
    print("Promedio de primos matriz1: ",promedio1)
    print("Promedio de primos matriz2: ",promedio2)
    print(" ")

    if cont6>0 and cont5>0:
        print("El promedio entero de los primos de ambas matrices se encuentran en la otra")

    elif cont5>0:
        print("El promedio entero de los primos de la segunda matriz se encuentra en la primera")

    elif cont6>0:
        print("El  promedio entero de los primos de la primera matriz se encuentra en la segunda")


    else:
        print("Ninguno de los dos promedios de los primos se encuentra en la otra lista")

except ValueError:
    print("El valor digitado debe ser numerico")
