#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números
terminan en dígito primo'''

try:
	lista=[]
	lista2=[]

	for i in range(10):
		numero=int(input("Digite un numero entero: "))
		lista.append(numero)

	aumento=0	
	for n in range(len(lista)):
		if lista[n]%10==2 or lista[n]%10==3 or lista[n]%10==5 or lista[n]%10==7:
			aumento+=1

	if aumento>0:		
		print("Hay %d"%aumento + " numeros que terminan en digito primo")
	
	else:
		print("No hay numeros que terminen en digito primo")
		
except ValueError:
	print("El valor digitado debe ser numerico")			    	