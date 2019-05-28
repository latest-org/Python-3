#-*-conding:utf-8-*-

'''28.	Leer una matriz 4x6 entera y determinar en qué posiciones se encuentran los números cuyo penúltimo dígito sea el 5'''

try:
    matriz=[]

    for a in range(2):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)

    lista=[]
    cont=0
    for c in range(len(matriz)):
        for d in range(len(matriz[c])):
            numero=matriz[c][d]

            numero=numero//10
            digito=numero%10
            if digito==5:
                pos=c,d
                lista.append(pos)
                cont+=1

    print(" ")

    if cont>0:
        print(lista)

    else:
        print("No hay numeros que tengan de penultimo digito el 5")

except ValueError:
    print("El valor digitado deber ser numerico")
