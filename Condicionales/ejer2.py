#-*-coding:utf-8-*-


''' Leer un numero entero y determinar si tiene 3 digitos'''


try: 
	 numero = int(raw_input("digite un numero"))

	 if numero >= 100 and numero <= 999:
	 	print "El numero ingresado o digitado tiene 3 digitos"


	 else:
	 	print "El numero ingresado no tiene 3 digitos"

	 	
except ValueError:
	print "El valor digitado debe ser un valor numerico"