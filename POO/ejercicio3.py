#-*-conding:utf-8-*-
import random
BAJO = 18.4
NORMAL = 18.5 
SOBREPESO = 25.0
OBESIDAD = 30 

class Persona(object):
	def __init__(self, *args):
		if len(args) ==0:
			self.__nombre = ""
			self.__edad = 0 
			self.__dni = self.generarDni()
			self.__sexo = "H"
			self.__peso = 0 
			self.__altura = 0 
		
		elif len (args)==3:
			self.__nombre = args[0]
			self.__edad = args[1]
			self.__dni = self.generarDni()
			self.__sexo = args[2]
			self.__peso = 0 
			self.__altura = 0 
		
		elif len (args) ==5:
			self.__nombre = args[0]
			self.__edad = args[1]
			self.__dni = self.generarDni()
			self.__sexo = args[2]
			self.__peso = args[3] 
			self.__altura = args[4]
			
	def calcularIMC(self):
		IMC = self.__peso/self.__altura**2
		if IMC <= BAJO:
			return -1
			
		elif IMC>=NORMAL and IMC <SOBREPESO:
			return 0 
				
		elif IMC>=SOBREPESO and IMC<OBESIDAD:
			return 1

	def toString(self):
		print "Nombre: %s"%self.___nombre + "\n"
		print "Edad: %d"%self.___edad + "\n"
		print "dni: %s"%self.___dni + "\n"
		print "sexo: %s"%self.___sexo + "\n"
		print "peso: %.f"%self.___peso  + "\n"
		print "altura: %.f"%self.___altura 
	
	
	
	def generarDni(self):
		num = random.randint(10000000,99999999)
		cad = "TRWAGMYFPDXBNJZSQVHLCKE"
		letra = cad[num % 23]		
		return  str(num)+letra
					
		
	def esMayorDeEdad(self):
		if self.__edad >= 18:
			return True
		else:
			return False

	def comprobarSexo(self, sexo):
		if sexo in ["H", "M"]:
			return sexo
		return "H"

	def set__nombre(self,nombre):
		self.__nombre = nombre	
	
	def set__edad(self,edad):
		self.__edad = edad

	def set__sexo(self,sexo):
		self.__sexo = sexo

	def set__peso (self,peso):
		self.__peso = peso
	
	def set__altura(self,altura):
		self.__altura = altura
	
		
def main():


	try:
		nombre = str(raw_input("Ingrese su nombre: "))
		edad = int(raw_input("Ingrese su edad: "))
		sexo = str (raw_input("Ingrese su sexo: "))
		peso = float(raw_input("Ingrese su peso actual: "))
		altura = float(raw_input("Ingrese su altura con punto: "))
		
		persona1 = personas(nombre,edad,sexo,peso,altura)
		persona2 = personas(nombre,edad,sexo)
		persona3 = ()
		print persona1.calcularIMC()
		print persona1.esMayorDeEdad()
		print persona1.comprobarSexo()
		print persona1.generarDni()
		
		if persona2.esMayorDeEdad() == True:
			print "%s es mayor de edad" % persona2.nombre
		else:
			print "%s no es mayor de edad" % persona2.nombre
		
	except ValueError:
		print 	"La cantidad ingresada debe ser un valor numero "
if __name__=='__main__':
	main()	




