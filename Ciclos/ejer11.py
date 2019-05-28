#-*-coding:utf-8-*-


''' leer un numero entero de dos digitos y mostrar en pantalla todos los enteros entre un digito y el otro'''



try: 
	numero = int(raw_input("Ingrese un numero: "))
	digito1 = numero/10
	digito2 = numero%10

	print "los numeros comprendidos son "


	for a in range (digito1,digito2+1):
		print a


	for a in range (digito2,digito1+1):
		print a













except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"