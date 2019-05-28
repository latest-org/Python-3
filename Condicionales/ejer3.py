#-*-coding:utf-8-*-


''' leer un numero entero y determinar si es negativo'''


try: 
	 numero = int(raw_input("Digite un numero entero:"))

	 if numero<0:
	 	print "el numero digitado es negativo"

	 else:
	 	print "el numero digitado no es negativo"


except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"