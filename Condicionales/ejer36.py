 #-*-coding:utf-8-*-


'''Leer un número entero de 4 dígitos y determinar si tiene más dígitos pares o impares'''


try:
	numero = int(raw_input("Digite un numero de 4 digitos: "))
  	if numero>999 and numero<=9999:
		digito1 = numero/1000
		digito2 = (numero%1000)/100
		digito3 = (numero%100) /10
		digito4 = numero%10


		if digito1%2==0 and digito2%2==0 and digito3%2==0 and digito4%2==0:
			print "Todos los digitos son pares"

		elif digito1%2!=0 and digito2%2!=0 and digito3%2==0 and digito4%2==0:
			print "Hay la misma cantidad de pares como de impares"

		elif digito1%2==0 and digito2%2!=0 and digito3%2!=0 and digito4%2!=0:
			print "hay mas 3 impares y tan solo uno es par"

		elif digito1%2==0 and digito2%2!=0 and digito3%2==0 and digito4%2==0:
			print "hay mas 3 pares y tan solo uno es impar"

		elif digito1%2==0 and digito2%2==0 and digito3%2!=0 and digito4%2!=0:
			print "Hay la misma cantidad de pares como de impares"

		elif digito1%2==0 and digito2%2==0 and digito3%2==0 and digito4%2!=0:
			print "Solo hay un digito impar"

		elif digito1%2==0 and digito2%2==0 and digito3%2!=0 and digito4%2==0:
			print "Solo hay un digito impar"

		elif digito1%2!=0 and digito2%2==0 and digito3%2==0 and digito4%2==0:
			print "Solo hay un digito impar"

		elif digito1%2!=0 and digito2%2!=0 and digito3%2!=0 and digito4%2==0:
			print "Solo hay digito par"

		elif digito1%2!=0 and digito2%2==0 and digito3%2!=0 and digito4%2==0:
			print "hay la misma cantidad de pares como de impares"

		elif digito1%2!=0 and digito2%2==0 and digito3%2==0 and digito4%2!=0:
			print "hay la misma cantidad de pares como de impares"

		elif digito1%2==0 and digito2%2!=0 and digito3%2==0 and digito4%2!=0:
			print "hay la misma cantidad de pares como de impares"

		elif digito1%2==0 and digito2%2!=0 and digito3%2!=0 and digito4%2==0:
			print "Hay la misma Cantidad de pares como de impares"






		else:
			print "Todos los digitos son impares"



except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"





