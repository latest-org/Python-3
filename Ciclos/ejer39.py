#-*-coding:utf-8-*-

'''Se define la serie de Fibonacci como la serie que comienza con los dígitos 1 y 0 y va sumando progresivamente 
los dos últimos elementos de la serie, así: 0 1 1 2 3 5 8 13 21 34.......

Utilizando el concepto de ciclo generar la serie de Fibonacci hasta llegar o sobrepasas el número 10000-'''

try:
	numero=1
	ultimo=1
	anterior=0

	for contador in range(0,19):
		print (str(contador) + "=" + str(numero))
		anterior=ultimo
		ultimo=numero
		numero=anterior+ultimo

except ValueError:
	print("El valor digitado debe ser numerico")		
		

