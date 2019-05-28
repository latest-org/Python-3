#-*-coding:utf-8-*-




'''leer un numero y determinar cuantos digitos tiene'''


try:
	 numero = int(raw_input("Ingrese un numero: "))

	 indicador = 0
	 while numero> 0:
	 	numero = numero/10
	 	indicador= indicador +1 
	 print  "el numero de digitos es " + "%d"%indicador 

except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"