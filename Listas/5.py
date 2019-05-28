#-*-coding:utf-8-*-

'''Almacenar en una lista de 10 posiciones los 10 números primos comprendidos entre 100 y 300. Luego mostrarlos en pantalla'''

try:

	lista=[]

	for a in range(100,300,1):
		numero=a

		contador=0

		for b in range(1,numero+1):
			if (numero%b)==0:
				contador+=1

		if contador==2:
			lista.append(numero)

	print(" ")		
	print("Los 10 primeros numeros primos entre 100 y 300 son :")
	print(" ")
	print(lista[:10])		

except ValueError:
	print("El valor digitado debe ser numerico")					 