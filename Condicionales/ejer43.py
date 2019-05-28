#-*-coding:utf-8-*-


'''Leer dos números enteros y determinar
si la diferencia entre los dos es un número 
divisor exacto de alguno de los dos números'''



try: 
	numero1 = int(raw_input("Digite un numero entero"))
	numero2 = int(raw_input("Digite un numero entero"))
	resultado1 = numero1 - numero2
	resultado2 = numero2 - numero1

	if numero1%resultado1==0:
		print "La diferencia que hay entre los numeros es un divisor exacto del primer numero"

	elif numero2%resultado2==0:
		print "La diferencia que hay entre los numeros es un divisor exacto del segundo numero"


	else:
		print "la diferencia no es un divisor del numero"





except ValueError:
	print "La candidad ingresada debe ser un valor numerico"