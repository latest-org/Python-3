#-*-coding:utf-8-*-

'''Determinar a cuánto es igual el promedio entero de los elementos de la serie de Fibonacci entre 0 y 1000'''

try:

	numero1=1
	numero2=1
	numero3=0
	suma=0
	promedio=0
	contador=0

	for contador in range(0,15):
		print(str(contador)+ "=" + str(numero1) )
		numero3=numero2
		numero2=numero1
		numero1=numero2+numero3
		contador+=1
		suma+= numero2
		promedio=suma//contador
	print("La suma de los elementos de la serie fibonacci es: %d"%suma)
	print("Y su promedio es: %d"%promedio)
	
except ValueError:
	print("El valor difgitado debe ser numerico")		