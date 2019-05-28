#-*-coding:utf-8-*-





#Por último, indica el Videojuego tiene más horas estimadas 
#y la serie con mas temporadas. Muéstralos en pantalla
#con toda su información.

class Serie:
	def __init__(self, *args):
		
		if len(args) ==0 : 
			self.titulo = 0
			self.numero_temporada = 3
			self.entregado = False
			self.genero = ""
			self.creador = ""
			
		elif len(args)==2:
			self.titulo = [0]
			self.creador = args[1]
			self.numero_temporada = 3
			self.entregado = False
			self.genero = ""
			
		elif len(args)==4:
			self.titulo =args [0]
			self.creador =args [1]
			self.numero_temporada =args [2]
			self.genero =args [3]
			self.entregado = False	
					
	#metodo get
	def get_titulo(self):
		return self.titulo
		
	def get_creador(self):
		return self.creador 
		
	def get_numero_temporada(self):
		return self.numero_temporada
		
	def get_genero(self):
		return self.genero
		
	#metodo set
	def set_titulo(self, titulo):
		self.titulo = titulo
		
	def set_creador(self, creador):
		self.creador = creador
	
	def set_numero_temporada(self, numero_temporada):
		self.numero_temporada = numero_temporada
	def set_genero(self,genero):
		self.genero = genero
		
	def toString1(self):
		print "Titulo: %s"%self.titulo+ "\n"
		print "Creador: %s"%self.creador + "\n"
		print "Numero de Temporadas: %i"%self.numero_temporada + "\n"
		print "genero: %s"%self.genero 
		
	def entregar(self):
		cont4= 0 
		self.entregado = True
		cont4+=1
		return self.entregado, cont4
		
	def devolver(self):
		cont5 = 0 
		self.entregado = False
		cont5+=1
		return self.entregado, cont5 

		
class VideoJuegos:
	def __init__(self, *args):
		if len(args)==0:
			self.titulo = ""
			self.horas_estimadas = 10
			self.entregado = False 
			self.genero = ""
			self.compania = ""
			
		elif len(args)==2:
			self.titulo = args[0]
			self.horas_estimadas = args[1]
			self.entregado = False 
			self.genero = ""
			self.compania = ""
			
		elif len(args)==4:
			self.titulo = args[0]
			self.horas_estimadas = args[1]
			self.genero = args[2]
			self.compania = args[3]
			self.entregado = False 
	#metodo get
	def get_titulo(self):
		return self.titulo
		
	def get_horas_estimadas(self):
		return self.horas_estimadas 
		
	def get_genero(self):
		return self.genero
	
	def get_compania(self):
		return self.compania
		
	def entregar(self):
		cont4= 0 
		self.entregado = True
		cont4+=1
		return self.entregado, cont4
		
	def devolver(self):
		cont5 = 0 
		self.entregado = False
		cont5+=1
		return self.entregado, cont5 
		
	def isEntregado(self):
		return self.entregado
		
		
		
	#metodo set
	def set_titulo(self, titulo):
		self.titulo = titulo
		
	def set_horas_estimadas(self,horas_estimadas):
		self.horas_estimadas = horas_estimadas
	
	def set_genero(self,genero):
		self.genero = genero
		
	def set_compania(self,compania):
		self.compania = compania
		
	def toString2(self):
		print "Titulo: %s"%self.titulo + "\n"
		print "Horas Estimadas: %d"%self.horas_estimadas + "\n"
		print "Genero: %s"%self.genero + "\n"
		print "Compañía: %s"%self.compania 

def main():
	
		try:
			series = []
			video = []
			
			for a in range(2):
				x = str(raw_input("Ingrese una serie: "))
				y = str(raw_input("Ingrese el genero de una serie: "))
				z = int(raw_input("Ingrese un numero de sus temporadas: "))
				g = str(raw_input("Ingrese el nombre del creador de la serie: "))
				objeto = Serie(x,y,z,g)
				series.append(objeto)
				objeto.toString1()	
				print objeto.entregar()			
				
			mayor1 = series[0]
			for objeto in series:
				if objeto.get_numero_temporada()> mayor1.get_numerotemporada():
					mayor = objeto
					
			mayor1.string1()
			for a in range(2):
				a = str(raw_input("Ingrese el nombre de un videojuego: "))
				b = int(raw_input("Ingrese las horas estimadas: "))
				c = str(raw_input("Ingrese el genero del videojuego: "))
				d = str(raw_input("Ingrese el nombre de la compañia: "))
				objeto2 = VideoJuegos(a,b,c,d)
				video.append(objeto2)
				objeto2.toString2()
				print objeto2.entregar()
				
			print "es el videojuego con mas horas estimadas de juego: "	
			mayor = video[0]
			for objeto2 in video:
				if objeto2.get_horas_estimadas()> mayor.get_horas_estimadas():
					mayor = objeto2 
						
			mayor.toString2()
			
			
			

				
				
		except ValueError:
			print "La cantidad ingresada debe ser un valor numerico"
if __name__=='__main__':
	main()
	
	
	
	
	

