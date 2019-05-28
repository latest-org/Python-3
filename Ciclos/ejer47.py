#-*-coding:utf-8-*-

'''Leer números hasta que el usuario ingrese 0. cuando el usuario ingrese 0 determinar a cuanto es igual el 
promedio entero de los número primos leídos'''

try:
	numero=1
	suma=0
	promedio=0
	contador=0
	contador2=0


	while numero !=0:
		numero = int(input("Digite un numero entero: "))	

		for i in range(1,numero+1,1):
			if (numero % i) ==0:
				contador+=1

		if contador ==2:
			suma+= numero
			contador2 +=1
			promedio= suma // contador2

	print("La suma de los numeros primos son: %d"%suma)		
	while numero ==0:
		print("El promedio de esa suma es: %d"%promedio)
		break

except ValueError:
	print("El valor digitado debe ser numerico")			
			
