#-*-coding:utf-8-*-

'''Leer un número de dos dígitos y determinar si pertenece a la serie de Fibonacci'''

try:
	numero=int(input("Digite un numero entero de dos digitos:"))

	while numero >=10 and numero <=99:

		print("El numero digitado pertenece a la serie fibonacci")	

		if numero ==89 or numero ==55 or numero ==34 or numero==21 or numero==13:
			
			break
		else:
			print("El numero digitado no pertenece a la serie Fibonacci")
			break
			
except ValueError:
	print("El valor digitado debe ser numerico")					
