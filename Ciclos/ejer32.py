#-*-coding:utf-8-*-




'''Leer números hasta que digiten 0 y determinar a cuanto es igual el promedio entero de los número primos leídos'''



try: 
	numero =1
	cont = 0 
	cont2=0
	suma =0 
	promedio =0

	while numero!=0:
		numero = int(raw_input("Ingrese un numero: "))
		cont =0
		for a in range (1,numero+1):


			if numero%a ==0:
				cont+=1


		if cont==2:
			suma+= numero
			cont2+=1



	if suma==0:
		print "No se ingresaron numeros primos"


	else:

		promedio = suma / cont2 
		print "El promedio de los numeros primos ingresados es de %d"%promedio





except ValueError:
	print "la cantidad ingresada debe ser un valor numerico"



except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"

