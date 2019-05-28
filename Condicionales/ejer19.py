#-*-coding:utf-8-*-

'''Leer tres números enteros y determinar cuál es el mayor.
 Usar solamente dos variables'''



try:
	numero1 = int(raw_input("Digite un numero entero :"))
	numero2 = int (raw_input("Digite otro numero entero :"))

	numero1  = numero1 * 100
	numero1 = numero1 + numero2

	numero2 = int(raw_input("Digite un numero entero: "))

	if (numero1/100>numero1%100) and (numero1/100>numero2):
		print "el primer numero es mayor"

	elif (numero1/100>numero1/100) and (numero1%100>numero2):
		print "el segundo numero es mayor"

	elif (numero2>numero1/100) and (numero2>numero1%100):
		print "el tercer numero es mayor"

	else:
		print "los numeros son iguales"
 


except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"






















	
