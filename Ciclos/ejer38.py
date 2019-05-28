#-*-coding:utf-8-*-





''' Leer un número entero y mostrar en pantalla su tabla de multiplicar. '''



try: 
	numero = int(raw_input("Ingrese un numero: "))

	if numero>0:

		a=1

		while a<=10:
			print "%d"%numero, "por" , "%d"%a, "es igual a:", numero*a


			a+=1


	else:
		print  "el numero ingresado no se puede multiplicar"



except ValueError:
	print "la cantidad ingresada debe ser un valor numerico"