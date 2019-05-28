#-*-coding:utf-8-*-



'''Leer tres números enteros y mostrarlos ascendentemente'''


try:
	numero1 = int(raw_input("digite el primer numero entero :"))
	numero2 = int(raw_input("Digite el segundo numero entero : "))
	numero3 = int (raw_input("Digite el tercer numero entero : "))


	if numero1 > numero2 and numero2>numero3:
		print "%d ,"%numero3 + "%d ,"%numero2 + "%d ,"%numero1

	elif numero1 < numero2 and numero1 < numero3:
		print "%d ,"%numero2 + "%d ,"%numero3 +"%d ,"%numero1

	elif numero1 > numero2 and numero1 < numero3:
		print "%d,"%numero3 + "%d,"%numero1 + "%d,"%numero2



except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"