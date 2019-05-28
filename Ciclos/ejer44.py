#-*-coding:utf-8-*-


'''Leer un número y calcularle su factorial'''

try:
	numero=int(input("Digite un numero entero: "))

	var=1

	for i in range(1,numero+1):
		var=var*i
	print(var)

except ValueError:
	print("El valor digitado debe ser numerico")

