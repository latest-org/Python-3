
#-*-coding:utf-8-*-


'''leer un numero entero y determinar si es primo'''


try: 
	numero = int(raw_input("Ingrese un numero: "))
	contador=0

	for a in range (1,numero+1):
		if (numero%a)==0:
			contador=contador+1

	if contador==2:
		print "El numero es primo"

	else:
		print "el numero no es primo"





except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"