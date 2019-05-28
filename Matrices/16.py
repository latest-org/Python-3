#-*-conding:utf-8-*-

'''16.	Leer una matriz 5x4 entera y determinar cuántos números almacenados en ella tienen un solo dígito'''

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

            if numero <=9:
                cont+=1

    if cont>0:
        print("hay " + "%d"%cont + " numeros con un solo digito")

    else:
        print("No hay numeros con un solo digito")

except ValueError:
    print("El valor digitado debe ser numerico")
