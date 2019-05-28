#-*-conding:utf-8-*-

'''14.	Leer una matriz 5x5 entera y determinar cuántos números almacenados en ella tienen mas de 3 dígitos'''

try:

    matriz=[]

    for a in range(5):
        fila=[]
        for b in range(5):
            numeros=int(input("Digite un numero entero: "))
            fila.append(numeros)
        matriz.append(fila)

    cont=0    
    for c in range(len(matriz)):
        for d in range(len(matriz[c])):
            numero=matriz[c][d]

            if numero>999:
                cont+=1

    if cont>0:
        print("hay " + "%d"%cont + " numeros que tienen mas de 3 digitos")

    else:
        print("No hay numeros con mas de 3 digitos")

except ValueError:
    print("El valor digitado debe ser numerico")
