#-*-coding:utf-8-*-

'''leer un numero entero de 2 digitos y determinar si los dos digitos son iguales'''


try: 
	numero = int(raw_input("Ingrese un numero entero de dos digitos :"))
	numero >9 and numero<=99
	digito1 = numero /10
	digito2 = numero %10

	


	if digito1 == digito2:
		print " Los digitos son iguales "

	elif  digito1 != digito2:
		print " los digitos no son iguales"


	else:
		print "el numero ingresado no tiene 2 digitos"

except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"