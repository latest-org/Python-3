#-*-conding:utf-8-*-

'''19.	Leer dos matrices 4x5 entera y determinar si sus contenidos son exactamente iguales'''

try:
    matriz=[]
    matriz2=[]

    for a in range(4):
        fila=[]
        for b in range(5):
            numeros=int(input("Digite un numero para la primera matriz: "))
            fila.append(numeros)
        matriz.append(fila)

    print(" ")

    for c in range(4):
        fila2=[]
        for d in range(5):
            numeros2=int(input("Digite un numero para la segunda matriz: "))
            fila2.append(numeros2)
        matriz2.append(fila2)

    print(" ")

    if matriz==matriz2:
        print("Las dos matrices son exactamente iguales")

    else:
        print("Las dos matrices no son exactamente iguales")

except ValueError:
    print("El valor digitado debe ser numerico")
