#-*-conding:utf-8-*-

'''13.	Leer una matriz 5x3 entera y determinar en qué columna está el mayor número que comienza con el dígito 4'''

try:
    matriz=[]

    for a in range(5):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero entero: "))
            fila.append(numeros)
        matriz.append(fila)

    mayor=0
    for c in range(len(matriz)):
        for d in range(len(matriz[c])):
            numero=matriz[c][d]

            while numero>0:
                digito=numero%10
                if numero==4:
                    if matriz[c][d]>mayor:
                        mayor=matriz[c][d]
                numero=numero//10
    lista=[]
    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            numero2=matriz[e][f]

            while numero2>0:
                digito=numero2%10
                if numero2==mayor:
                    pos=f
                    lista.append(pos)
                numero2=numero2//10

    print(lista)
    print(matriz)

except ValueError:
    print("El valor digitado debe ser numerico")
