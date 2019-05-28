#-*-coding:utf-8-*-



''' Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5.'''



try:
	numero =1
	cont = 0 
	suma =0 
	promedio =0

	while numero!=0:
		numero = int(raw_input("Ingrese un numero: "))
		if numero%10 == 5:
			suma= suma + numero
			cont= cont+1
			promedio= suma / cont

	if numero%10==0:
		print "el promedio de los numeros terminados es 5 es igual a: %d"%promedio

except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"