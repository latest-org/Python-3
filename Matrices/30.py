#-*-conding:utf-8-*-

'''30.	Leer una matriz 4x6 entera y determinar cuántas veces está en ella el número menor'''

try:
    matriz=[]

    for a in range(2):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)


    for c in range(len(matriz)):
        menor=matriz[0][0]
        for d in range(len(matriz[c])):
            numero=matriz[c][d]

            if numero<menor:
                menor=numero

    cont=0
    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            numero2=matriz[e][f]

            if numero2==menor:
                cont+=1

    print(cont)

except ValueError:
    print("El valor digitado debe ser numerico")
