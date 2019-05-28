#-*-coding:utf-8-*-


'''Leer dos números enteros de dos dígitos y determinar si la suma de los dos números origina un número par'''



try:
	numero1 = int(raw_input("Digite un numero de dos digitos :"))
	numero2 = int(raw_input("Digite otro numero de dos digitos :"))


	if numero1>9 and numero1<=99 and numero2>9 and numero2<=99:


		if numero1%2 ==0 and numero2%2 ==0:
			print " la suma de los 2 numeros origina un numero par "



		else: 
			print " La suma de los 2 numero no origina un numero par "




















except ValueError: 
	print " la cantidad ingresada debe ser un valor numerico"