#-*-coding:utf-8-*-

'''Leer dos números enteros y almacenar en una lista los 10 primeros números primos comprendidos entre el menor y el mayor. 
Luego mostrarlos en pantalla'''

try:
	lista=[]
	lista2=[]


	numero1=int(input("Digite el primer numero entero: "))
	numero2=int(input("Digite el segundo numero entero: "))


	if numero1 > numero2:

		for a in range(numero2,numero1+1):
			primo=a
			contador=0

			for b in range(1,primo+1):
				if (primo%b)==0:
					contador+=1

			if contador==2:
				lista.append(primo)

		print(lista[:10])			
	

	if numero2>numero1:

		for c in range(numero1,numero2+1):
			primo2=c
			contador2=0

			for d in range(1,primo2+1):
				if (primo2%d)==0:
					contador2+=1

			if contador2==2:
				lista2.append(primo2)

		print(lista2[:10])					


except ValueError:
	print("El valor digitado debe ser numerico")
