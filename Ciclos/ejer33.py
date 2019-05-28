#-*-coding:utf-8-*-

'''Si 32768 es el tope superior para los números entero cortos, determinar cuál es el
número primo más cercano por debajo de él'''

try:

	total=32768
	suma=0
	contador=0
	aumento=0
	valor=0
	total2=0

	for i in range(1,total+1,1):
		if (total % i) ==0:
			aumento+=1

	if aumento==2:
		if total2 > i:
			total2=i 
	print(i)		

except ValueError:
	print("El valor digitado debe ser numerico")				