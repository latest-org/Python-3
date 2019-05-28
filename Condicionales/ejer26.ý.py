 #-*-coding:utf-8-*-



'''Leer un número entero de cuatro dígitos y determinar a cuanto es igual la suma de sus dígitos'''


try:
	numero = int(raw_input("Digite un numero de cuatro digitos :"))
	digito1 = numero/1000
	digito2 = (numero%1000) /100
	digito3 = numero%100
	digito4 = numero%10

	 print "1: %d"%digito1
	 print "2: %d"%digito2
	 print "3: %d"%digito3
	 print "4: %d"%digito4
	 