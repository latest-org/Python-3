#-*-coding:utf-8-*-



''' Leer tres números enteros de tres dígitos y determinar si el penúltimo dígito de los tres números es igual'''


try:
	numero1 = int(raw_input("Digite un numero entero: "))
	numero2 = int(raw_input("Digite un numero entero: "))
	numero3 = int(raw_input("Digite un numero entero: "))


	if numero1>99 and numero1<=999 and numero2>99 and numero2<=999 and numero3>99 and numero3<=999:
		digito1 = (numero1%100) /10
		digito2 =  (numero2%100) /10
		digito3 = (numero3%100) /10
		print "%d"%digito1
		print "%d"%digito2
		print "%d"%digito3

		if digito1==digito2 and digito1==digito3:
			print "Los penultimos digitos son iguales"


		else:
			print "Ningun numero tiene digitos iguales"


except ValueError:
	print " la cantidad ingresada debe ser un valor numerico"