#-*-conding:utf-8-*-

'''18.	Leer una matriz 5x5 entera y determinar en qué posición exacta se encuentra el mayor múltiplo de 8'''

try:
    matriz=[]

    for a in range(5):
        fila=[]
        for b in range(5):
            numeros=int(input("Digite un numero entero: "))
            fila.append(numeros)
        matriz.append(fila)

    mayor=0
    for c in range(len(matriz)):
        for d in range(len(matriz[c])):
            numero=matriz[c][d]

            if numero%8==0:
                if numero>mayor:
                    mayor=numero

    lista=[]
    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            numero2=matriz[e][f]

            if numero2==mayor:
                pos=e,f
                lista.append(pos)

    print(lista)

except ValueError:
    print("El valor digitado debe ser numerico")
