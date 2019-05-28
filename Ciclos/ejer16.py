#-*-coding:utf-8-*-


'''mostrar en pantalla el promedio entero de los n primeros multiplo de 3 para un numero n leido'''



try: 
	numero = int(raw_input("Ingrese un numero: "))
	suma =0 
	promedio=0 
	multiplo_3=0




	for a in range (1,numero+1):
		
		multiplo_3 = a *3 
		suma = suma + multiplo_3
		promedio = suma/numero
		print "%d"%multiplo_3
	print "el promedio es " + "%d"%promedio



except ValueError:
	print	"La cantidad ingresada debe ser un valor numerico"