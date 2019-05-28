#-*-conding:utf-8-*-

'''36.	Leer dos matrices 4x6 enteras y determinar si el mayor número almacenado en una de ellas que pertenezca a la Serie de Fibonacci es igual al mayor número almacenado en la otra matriz que pertenezca a la Serie de Fibonacci'''

try:
    matriz=[]
    matriz2=[]

    for a in range(3):
        fila=[]
        for b in range(3):
            numeros=int(input("Digite un numero para la primera lista: "))
            fila.append(numeros)
        matriz.append(fila)

    print(" ")

    for c in range(3):
        fila2=[]
        for d in range(3):
            numeros2=int(input("Digite un numero para la segunda lista: "))
            fila2.append(numeros2)
        matriz2.append(fila2)

    numero1=0
    numero2=1
    numero3=0

    lista=[0]

    for e in range(0,20):
        numero3=numero2
        numero2=numero1
        numero1=numero3+numero2

        lista.append(numero1)

    lista3=[]
    for f in range(len(matriz)):
        for g in range(len(matriz[f])):
            numero=matriz[f][g]

            for h in range(len(lista)):
                numero2=lista[h]

                if numero==numero2:
                    lista3.append(numero)

    mayor=0

    for i in range(len(lista3)):
        if lista3[i]>mayor:
            mayor=lista3[i]



    lista4=[]
    for j in range(len(matriz2)):
        for k in range(len(matriz2[j])):
            numero3=matriz2[j][k]

            for l in range(len(lista)):
                numero4=lista[l]

                if numero4==numero3:
                    lista4.append(numero4)

    mayor2=0
    for m in range(len(lista4)):
        if lista4[m]>mayor2:
            mayor2=lista4[m]

    print(" ")        
    print("El mayor numero de la primera lista que pertenece a fibonacci :",mayor)
    print("El mayor numero de la segunda lista que pertenece a fibonacci :",mayor2)


    if mayor==mayor2:
        print("Los dos numeros mayores son iguales")

    else:
        print("Uno de los dos mayores es superior al otro")


except ValueError:
    print("El valor digitado debe ser numerico")
