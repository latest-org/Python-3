#-*-coding:utf-8-*-




'''Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos primos'''




try:
	numero1 = int(raw_input("Ingrese un numero: "))
	numero2 = int(raw_input("Ingrese otro numero porfavor: "))


	cont1=0 
	cont2=0


	while numero1>0:
		digito1 = numero1%10
		numero1 = numero1/10
		if digito1 == 2 or digito1 == 3 or digito1 == 5 or digito1 ==7:
			cont1 = cont1 +1
	print "%d"%cont1 


	while numero2>0:
		digito2 = numero2%10
		numero2 = numero2/10
		if digito2 == 2 or digito2 == 3 or digito2 == 5 or digito2 ==7:
			cont2 = cont2 +1
	print "%d"%cont2



	if cont1>cont2:
		print "El primer numero ingresado tiene mas digitos primos que el segundo "


	if cont2 > cont1:
		print "El segundo numero ingresado tiene mas digitos primos que el primero"

	else:
		print "La cantidad ingresada debe ser un valor numerico" 


except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"