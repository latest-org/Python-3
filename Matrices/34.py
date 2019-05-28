#-*-conding:utf-8-*-

'''34.	Leer una matriz 4x6 entera y determinar cuántos de los números almacenados en ella pertenecen a los 100 primeros elementos de la serie de Fibonacci'''

try:
    matriz=[]

    for a in range(3):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)

    numero1=0
    numero2=1
    numero3=0

    lista=[0]
    for c in range(0,100):

        numero3=numero2
        numero2=numero1
        numero1=numero3+numero2

        lista.append(numero1)
    print(lista)
    cont=0
    for d in range(len(matriz)):
        for e in range(len(matriz[d])):
            numero=matriz[d][e]

            for f in range(len(lista)):
                numero2=lista[f]


                if numero2==numero:
                    cont+=1

    print(matriz)
    print("Hay %d"%cont + " elementos de la matriz que pertenecen a los 100 primeros elementos de la serie fibonacci")


except ValueError:
    print("El valor digitado debe ser numerico")
