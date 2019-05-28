#-*-conding:utf-8-*-

'''49.	Leer una matriz 3x3 entera y determinar si el promedio de todos los datos almacenados en ella se encuentra también almacenado'''

try:
    matriz=[]

    for a in range(3):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)

    suma=0
    promedio=0
    cont=0
    for c in range(len(matriz)):
        for d in range(len(matriz[c])):
            numero=matriz[c][d]

            suma+=numero
            cont+=1
            promedio=suma//cont

    cont2=0
    for e in range(len(matriz)):
        for d in range(len(matriz[e])):
            numero2=matriz[e][d]

            if numero2==promedio:
                cont2+=1

    print("Matriz :",matriz)
    print(" ")
    print("Promedio de los datos de la matriz: ",promedio)
    print(" ")

    if cont2>0:
        print("El promedio esta en la matriz")
    else:
        print("El promedio no esta en la matriz")    
except ValueError:
    print("El valor digitado debe ser numerico")
