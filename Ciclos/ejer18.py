#-*-coding:utf-8-*-


'''leer dos numeros entero y mostrar todos los
multiplos de 5
comprendidos entre el menor y el mayor'''




try: 
	n1 = int(raw_input("Ingrese un numero: "))
	n2 = int (raw_input("Ingrese otro numero: "))

	for a in range (n1,n2+1):
		if a%5==0:
			print a 

	for a in range (n2,n1+1):
		if a%5==0:
			print a









except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"