#-*-conding:utf-8-*-

'''21.	Leer dos matrices 4x5 enteras y determinar cuántos datos tienen en común'''

try:
    matriz=[]
    matriz2=[]

    for a in range(4):
        fila=[]
        for b in range(5):
            numeros=int(input("Digite un numero para la primera lista"))
            fila.append(numeros)
        matriz.append(fila)


    for c in range(4):
        fila2=[]
        for d in range(5):
            numeros2=int(input("Digite un numero para la primera lista"))
            fila2.append(numeros2)
        matriz2.append(fila2)

    for e in range(len(matriz)):
        for f in range(len(matriz[e])):
            numero=matriz[e][f]

            for g in range(len(matriz2)):
                for h in range()
