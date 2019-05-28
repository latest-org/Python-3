#-*-coding:utf-8-*-


'''Leer un número entero y determinar a cuánto
 es igual la suma de sus dígitos pares'''



try:
 	numero = int(raw_input("Ingrese un numero: "))
 	
 	suma =0 

 	while numero>0:
 		digito = numero%10
 		numero = numero/10
 


 		if digito%2==0:
 			suma = suma + digito

 	if suma==0:
 		"ninguno de los digitos es par"

 	else:
 		print "La suma de los digitos es %d"%suma



except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"


