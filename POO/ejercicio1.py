import datetime

class Hora():
	def __init__(self, *args):
		#Implementamos el constructor por defecto (sin parametros)
		if len(args) == 0:
			self.hora = 0
			self.minuto = 0
			self.segundo = 0
		#implementamos el constructor parametrizable (con los tres parametros)
		elif len(args) == 3:
			'''self.hora = args[0]
			self.minuto = args[1]
			self.segundo = args[2]'''
			self.__validar(args[0], args[1], args[2])

	def __validar_hora(self, hora):
		if 0 <= hora <= 23: #if hora >= 0 and hora <= 23:
			return True
		return False

	def __validar_minuto_segundo(self, valor):
		if 0 <= valor <= 59: #if hora >= 0 and hora <= 23:
			return True
		return False

	def __validar(self, hora, minuto, segundo):
		if self.__validar_hora(hora) and self.__validar_minuto_segundo(minuto) and self.__validar_minuto_segundo(segundo):
			self.hora = hora
			self.minuto = minuto
			self.segundo = segundo
		else:
			self.hora = 0
			self.minuto = 0
			self.segundo = 0

	def leer(self):
		try:
			hora = int(raw_input("Digite la Hora (0-23):"))
			minuto = int(raw_input("Digite el minuto (0-59):"))
			segundo = int(raw_input("Digite el segundo (0-59):"))
			self.__validar(hora, minuto, segundo)
		except ValueError:
			print "Error al ingreso de los datos"

	def convertir_segundos(self):
		fecha = datetime.datetime.now()
		return (fecha.hour * 3600) + (fecha.minute * 60) + fecha.second

	def convertir_segundos_hora(self, hora, minuto, segundo):
		return (hora * 3600) + (minuto * 60) + segundo

	def convertir_hora(self, segundos):
		if segundos <= 86400:
			horas = int(segundos / 3600)
			residuo_horas = segundos % 3600
			minutos = int(residuo_horas / 60)
			segundos = residuo_horas % 60
			self.__validar(horas, minutos, segundos)
		else:
			print "El valor de segundos no es correcto"

	def calcular_segundos_desde(self, hora):
		segundo_hora1 = self.convertir_segundos_hora(self.hora, self.minuto, self.segundo)
		segundo_hora2 = self.convertir_segundos_hora(hora.hora, hora.minuto, hora.segundo)
		if segundo_hora1 <= segundo_hora2:
			return segundo_hora2 - segundo_hora1
		return segundo_hora1 - segundo_hora2

	def agregar_segundo(self):
		if self.segundo == 59 and self.minuto == 59 and self.hora == 23:
			self.hora = 0
			self.minuto = 0
			self.segundo = 0
		elif self.segundo == 59 and self.minuto == 59:
			self.hora += 1 
			self.minuto = 0
			self.segundo = 0
		elif self.segundo == 59:
			self.minuto += 1
			self.segundo = 0
		else:
			self.segundo += 1

	def restar_segundo(self):
		if self.segundo == 0 and self.minuto == 0 and self.hora == 0:
			self.hora = 23
			self.minuto = 59
			self.segundo = 59
		elif self.segundo == 0 and self.minuto == 0:
			self.hora -= 1 
			self.minuto = 59
			self.segundo = 59
		elif self.segundo == 0:
			self.minuto -= 1
			self.segundo = 59
		else:
			self.segundo -= 1

	def clonar_hora(self):
		return Hora(self.hora, self.minuto, self.segundo)

	def mostrar_hora(self):
		return "%d:%d:%d" % (self.hora, self.minuto, self.segundo)

	def verificar_hora_igual(self, hora):
		if self.hora == hora.hora and self.minuto == hora.minuto and self.segundo == hora.segundo:
			return True
		return False

	def verificar_hora_menor(self, hora):
		segundo_hora1 = self.convertir_segundos_hora(self.hora, self.minuto, self.segundo)
		segundo_hora2 = self.convertir_segundos_hora(hora.hora, hora.minuto, hora.segundo)
		if segundo_hora1 < segundo_hora2:
			return True
		return False

	def verificar_hora_mayor(self, hora):
		segundo_hora1 = self.convertir_segundos_hora(self.hora, self.minuto, self.segundo)
		segundo_hora2 = self.convertir_segundos_hora(hora.hora, hora.minuto, hora.segundo)
		if segundo_hora1 > segundo_hora2:
			return True
		return False


















