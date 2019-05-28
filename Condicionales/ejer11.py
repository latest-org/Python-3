#-*-coding:utf-8-*-


'''Leer dos números enteros y determinar cuál es el mayor'''


try:
	numero1 = int(raw_input("Digite un numero :"))
 	numero2 = int(raw_input("Digite otro numero :"))

 	if numero1 == numero2:
 		print "los numeros ingresados son iguales"

 	elif numero1> numero2:
 		print " el primer numero ingresado es mayor que el segundo numero ingresado"


 	elif numero2> numero1:
 		print "el segundo numero ingresado es mayor que el primer numero ingresado"


 	else:
 		print "el numero ingresado tiene valores no correspondientes"












except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"