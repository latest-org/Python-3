#-*-coding:utf-8-*-


'''leer un numero entero de tres digito y determinar si tiene el digito 1'''



try:
	numero = int(raw_input ("Ingrese un numero de tres digitos: "))

	if  numero >99 and numero <=999:
		digito1 = numero/100
		digito2 = (numero%100) /10
		digito3	=numero%10


		while digito1==1 or digito2==1 or digito3==1:
			print "El numero ingresado tiene digito(s) 1"
			
			

			break





	else:
		print "El numero debe estar en el rango requerido"



except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"
