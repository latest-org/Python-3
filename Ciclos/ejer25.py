#-*-coding:utf-8-*-

''''Leer un número entero y determinar a
cuánto es igual el promedio entero de sus dígitos.'''


try:
	numero = int(raw_input("Ingrese un numero: "))
	suma=0
	cont=0
	promedio=0 
	while numero>0:
 		digito = numero%10
 		suma = suma + digito
 		cont = cont +1
 		numero = numero/10
 		promedio = suma/ cont
 	print "%d"%promedio


 		
 		





except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"
 