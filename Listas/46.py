#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los
almacenados en dicha lista son primos y comienzan por 5.'''

try:
	lista=[]
	lista2=[]
	lista3=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		primo=lista[b]
		contador=0

		for c in range(1,primo+1):
			if (primo%c)==0:
				contador+=1

		if contador==2:
			lista2.append(primo)


	for c in range(len(lista2)):
		primo2=lista[c]

		while primo2>0:
			digito=primo2%10
			if primo2==5:
				lista3.append(primo2)
			primo2=primo2//10
			
	aumento=0		
	for d in range(len(lista3)):
		aumento+=1							

	if aumento>0:	
		print(aumento)

	else:
		print("No hay numeros primos que empiezen por 5")		

except ValueError:
	print("El valor digitado debe ser numerico")	