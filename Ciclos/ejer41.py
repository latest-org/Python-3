#-*-coding:utf-8-*-

'''Determinar a cuánto es igual la suma de los elementos de la serie de Fibonacci entre 0 y 100'''

try:
	numero=1
	ultimo=1
	anterior=0
	suma=0

	for contador in range(0,10):
		print (str(contador) + "=" + str(numero))
		anterior=ultimo
		ultimo=numero
		numero=anterior+ultimo
		suma+=ultimo
	print("La suma de los elementos de la serie Fibonacci es : %d"%suma)
	print(numero)	
	

except ValueError:
	print("El valor digitado debe ser numerico")	