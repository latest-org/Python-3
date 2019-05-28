#-*-conding:utf-8-*-

class Cancion(object):
	def __init__(self,titulo,autor, duracion):
		self.titulo = titulo
		self.autor = autor 
		self.duracion = duracion 
		
	def get_titulo(self):
		return self.titulo
		
	def get_autor(self):
		return self.autor
		 
	def get_duracion(self):
		return self.duracion
	
	def set_titulo(self,titulo):
		self.titulo = titulo
		
	def set_autor(self, titulo):
		self.autor = autor
	
	def set_duracion(self,duracion):
		self.duracion = duracion 


		
def main():
	titulo = str(raw_input("Ingrese el titulo de la cancion: "))
	autor = str (raw_input("Ingrese el nombre del autor: "))
	duracion = int(raw_input("Tiempo de duracion de la cancion en seg: "))
	cancion1 = Cancion(titulo, autor, duracion)
	print "el titulo de la cancion es %s"% cancion1.get_titulo()
	print "el autor de la cancion es %s"% cancion1.get_autor()
	print "el titulo de la cancion es %i"% cancion1.get_duracion()


if __name__=='__main__':
	main()

		
