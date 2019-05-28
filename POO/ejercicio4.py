#-*-coding:utf-8-*-
import random 

class Password:

	def __init__(self, *args):
		if len (args) ==0:
			self.longitud =  8
			self.contrasena = 0
		elif len(args)==2:
			self.longitud = [0]
			self.contrasena = [1]
			
	def CompruebaPassword(self):
		var = "123467890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.contrasena = ("").join(random.choice(var)for a in range (self.longitud))
		return self.contrasena 
			
	def esFuerte(self):
		cont1 = 0 
		cont2 = 0 
		cont3= 0 
		
		for a in range(len(self.contrasena)):
			numero = self.contrasena[a]
			
			if numero.isupper() == True:
				cont1+=1
			elif numero.islower() == True:
				cont2+=1
			elif numero.isdigit() == True:
				cont3+=1
			
		if cont1>2 and cont2 >1 and cont3>5:
			return True
		return False
	def get_longitud(self):
		return self.longitud
		
	def get_contrasena(self):
		return self.contrasena
		
	def set_longitud(self, longitud):
		self.longitud = longitud
		
	
			
def main():

	

	try:
		
		longitud = int(raw_input("Ingrese la longitud de la contraseña: "))
		contrasenia = int(raw_input("Ingrese la cantidad de contraseñas: "))
		
		ArrayPassword = [] 
		evalua = []
		
		for b in range(contrasenia):
			ArrayPassword.append(Password())
			ArrayPassword[b].set_longitud(longitud)	
			ArrayPassword[b].CompruebaPassword()
			
			evalua.append(ArrayPassword[b].esFuerte())
			texto = ArrayPassword[b].get_contrasena(), evalua[b]
			print texto
			
		
	except ValueError:
		print 	"La cantidad ingresada debe ser un valor numero "
		
	
		
		
if __name__=='__main__':
	main()	




