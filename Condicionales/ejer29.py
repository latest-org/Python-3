#-*-coding:utf-8-*-


'''Leer un número entero de cinco dígitos y determinar si es un número capicúo. Ej. 15651, 59895. '''





try:
	 numero = int(raw_input("Digite un numero de cinco digitos :"))


	 if numero >9999 and numero <=99999:
	 	digito1 = numero/10000 
	 	digito2 = (numero%10000)/1000
	 	digito3 = numero%1000 /100
	 	digito4 = numero%100 /10
	 	digito5 = numero%10


	 	print "%d"%digito1
		print "%d"%digito2
		print "%d"%digito3
		print "%d"%digito4
		print "%d"%digito5

		if digito1== digito5 and digito2== digito4:
			print "El numero ingresado es capicuo "


		else:
			print "El numero ingresado no es capicuo"


	 else: 
		 print "El numero ingresado debe tener 5 digitos"





except ValueError:
	print "El valor ingresado debe ser un valor numerico"

