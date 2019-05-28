#-*-coding:utf-8-*-


'''leer dos numero y mostrar todos los enteros comprendidos entre ellos'''


try:
	numero1 = int(raw_input("Ingrese un numero: "))
	

	for a in range (numero1+1):
		print "%d"%a

	numero2 = int (raw_input("Ingrese otro numero: ")) 




	for b in range (numero2+1):
		print "%d"%b





except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"