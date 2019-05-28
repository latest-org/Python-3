#-*-coding:utf-8-*-

'''Utilizando ciclos anidados generar las siguientes parejas de enteros'''

try:

	for i in range(1,10):
		for l in range(3):
			print(i,l)

except ValueError:
	print("El valor digitado debe ser numerico")			