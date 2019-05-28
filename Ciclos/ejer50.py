#-*-coding:utf-8-*-

'''Leer un número entero y determinar a cuánto es igual el primero de sus dígitos'''

try:
	numero=int(input("Digite un numero entero:"))

	mayor=0

	while numero >0:
		digito = numero % 10	
		numero = numero /10	
	print(digito)
	
	
except ValueError:
	print("El valor digitado debe ser numerico")