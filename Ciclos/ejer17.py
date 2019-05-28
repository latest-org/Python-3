#-*-coding:utf-8-*-



'''promediar los x primeros multiplos de 2 y determinar si ese
promedio es mayor que los primeros multiplos de 5 para valores de x y y leidos'''


try:
 	x = int(raw_input("Ingrese un numero: "))
 	y = int (raw_input("Ingrese otro numero: "))
 	multiplos_2 = 0
 	multiplos_5 = 0
 	suma =0
 	suma2 = 0
 	promedio_2 =0 
 	promedio_5 =0 

 	for a in range (1,x+1):
 		
 		multiplos_2 = a * 2
 		suma = suma + multiplos_2 
 		promedio1 = suma/x
 		print "%d"%multiplos_2
 	print "el promedio de los multiplos de dos es "  + "%d"%promedio1 
 	print "\n"



 	for b in range (1,y+1):

 		multiplos_5 = b * 5
 		suma2 = multiplos_5 + suma2
 		promedio2 =suma2/y 
 		print "%d"%multiplos_5
 	print "el promedio de los multiplos de cinco es " + "%d"%promedio2
 	print 	"\n"

 	if promedio1<promedio2:
 		print "el promedio dos es el mayor"
 	print "\n"

 	if promedio2<promedio1:
 		print "el promedio uno es el mayor"
 	print "\n"



except ValueError:
	print "La cantidad ingresada debe ser un valor numerico"