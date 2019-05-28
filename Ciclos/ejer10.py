#-*-coding:utf-8-*-



'''leer un numero entero y determinar  a cuanto es la suma de todos de todos 
los enteros comprendidos entre 1 y el numero leido'''



try: 
	numero = int(raw_input("Ingrese un numero: "))
	suma =0


	for a in range (1, numero+1):
		suma +=a 
	print "la suma de los numeros comprendidos entre 1 y %d"%numero  + " es %d"%suma



except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"