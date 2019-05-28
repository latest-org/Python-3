#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista comienzan en dígito primo'''

try:
	lista=[]
	lista2=[]

	for i in range(10):
		numero=int(input("Digite un numero entero: "))
		lista.append(numero)

	for p in range(len(lista)):
		primo=lista[p]

		while primo>0:
			digito=primo%10
			if primo==2 or primo==3 or primo==5 or primo==7:
				lista2.append(primo)

			primo=primo//10
			
	aumento=0
	for f in range(len(lista2)):
		aumento+=1

	if aumento>0:	
		print("Hay %d"%aumento + " numeros que empiezan por digito primo")	

	else:
		print("No hay numeros que empiezen por digito primo")	

except ValueError:
	print("El valor digitado debe ser numerico")					