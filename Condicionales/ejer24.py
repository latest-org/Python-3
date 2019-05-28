#-*-coding:utf-8-*-



'''Leer un número entero de tres dígitos y determinar cuántos dígitos pares tiene'''


try:
 	numero = int(raw_input("Digite un numero de tres digitos :"))
 	digito1 = numero/100
 	digito2 =  (numero%100) /10
 	digito3 =  numero%10

 	if numero>99 and numero<=999:


 		if digito1%2 ==0 and digito2%2==0 and digito3%2!=0:
 			print "El digito uno y el digito dos son pares"


 		elif  digito1%2!=0 and digito2%2==0 and digito3==0:
 			print "el digito dos y el digito tres son pares"

 		elif  digito1%2==0 and digito2%2!=0 and digito3==0:
 			print "el digito uno y el digito tres son pares"


 		else:
 			print "ninguno de los digitos es par"


 	else:
 		print " el numero debe ser de tres digitos"














except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"


