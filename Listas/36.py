#-*-coding:utf-8-*-

'''Leer 10 números enteros, almacenarlos en una lista y determinar cuántos dígitos primos
hay en los números leídos'''

try:

	lista=[]
	lista2=[]

	for a in range(10):
		numeros=int(input("Digite un numero entero: "))
		lista.append(numeros)

	for b in range(len(lista)):
		primo=lista[b]

		while primo>0:
			digito=primo%10
			if digito==2 or digito==3 or digito==5 or digito==7:
				lista2.append(digito)
			primo=primo//10

	contador=0		
	for c in range(len(lista2)):
		contador+=1

	if contador>0:	
		print("Hay %d"%contador + " digitos primos en la lista")	

	else:
		print("No hay digitos primos en la lista")	

except ValueError:
	print("El valor digitado debe ser numerico")