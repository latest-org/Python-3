#-*-conding:utf-8-*-

'''50.	Leer una matriz 5x5 y determinar si el promedio de los elementos que se encuentran en su diagonal está almacenado en ella. Mostrar en pantalla en qué posiciones exactas se encuentra dicho dato'''

try:
    matriz=[]
    matriz2=[]


    for a in range(3):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)

    lista=[]
    for c in range(len(matriz)):
        for d in range(len(matriz)):
            numero=matriz[c][d]

            if [c]==[d]:
                lista.append(numero)

    suma=0
    promedio=0
    cont=0
    for e in range(len(lista)):
        suma+=lista[e]
        cont+=1
        promedio=suma//cont

    cont2=0
    for f in range(len(matriz)):
        for g in range(len(matriz)):
            numero2=matriz[f][g]

            if numero2==promedio:
                pos=f,g
                cont2+=1
    print(" ")
    print("Matriz: ",matriz)
    print(" ")
    print("Elementos de la diagonal: ",lista)
    print("Promedio de la diagonal: ",promedio)
    print(" ")

    if cont2>0:
        print("El promedio de la diagonal se encuentra en la matriz y esta en las posiciones: ",pos)

    else:
        print("El promedio de la diagonal no se encuentra en la matriz")


except ValueError:
    print("El valor digitado debe ser numerico")
