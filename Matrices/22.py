#-*-conding:utf-8-*-

'''22.	Leer dos matrices 4x5 enteras y determinar si el número mayor almacenado en la primera está en la segunda'''

try:
    matriz=[]
    matriz2=[]

    for a in range(4):
        fila=[]
        for b in range(5):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)

    mayor=0
    for c in range(len(matriz)):
        for d in range(len(matriz)):
            numero=matriz[c][d]

            if numero>mayor:
                mayor=numero

    print(" ")

    for e in range(4):
        fila2=[]
        for f in range(5):
            numeros2=int(input("Digite un numero para la segunda matriz: "))
            fila2.append(numeros2)
        matriz2.append(fila2)

    cont=0
    for g in range(len(matriz2)):
        for h in range(len(matriz2)):
            numero2=matriz2[g][h]

            if numero2==mayor:
                cont+=1

    print(mayor)

    if cont>0:
        print("El numero mayor de la primera matriz esta en la segunda")

    else:
        print("El numero mayor de la primera matriz no esta en la segunda")

except ValueError:
    print("El valor digitado debe ser numerico")
