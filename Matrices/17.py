#-*-conding:utf-8-*-

'''17.	Leer una matriz 5x4 entera y determinar cuántos múltiplos de 5 hay almacenados en ella'''

try:
    matriz=[]

    for a in range(5):
        fila=[]
        for b in range(4):
            numeros=int(input("Digite un numero entero: "))
            fila.append(numeros)
        matriz.append(fila)

    cont=0
    for c in range(len(matriz)):
        for d in range(len(matriz[c])):
            numero=matriz[c][d]

            if numero%5==0:
                cont+=1

    if cont>0:
        print("Hay " + "%d"%cont + " numeros multiplos de 5")

    else:
        print("No hay numeros multiplos de 5")

except ValueError:
    print("El valor digitado debe ser numerico")                     
