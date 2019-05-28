#-*-conding:utf-8-*-

'''15.	Leer una matriz 5x4 entera y determinar cuántos números almacenados en ella terminan en 34'''

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

            if numero%100==34:
                cont+=1

    if cont>1:
        print("Hay " + "%d"%cont + " numeros terminados en 34")

    else:
        print("No hay numeros terminados en 34")

except ValueError:
    print("El valor digitado debe ser numerico")
