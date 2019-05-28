#-*-coding:utf-8-*-

'''defina la clase cuenta bancaria que permita las operaciones: retirar,depositar, consultar 
saldo, entre otros, No olvide definir el constructor
para crear objetos de ducha clase, ademas recuenden que la cuenta siempre tiene un dueño'''

class CuentaBancaria(object):
	TIPO_CUENTA = ("Ahorro","Corriente")
	def __init__(self,titular,saldo,numero_cuenta,id_titular,fecha,tipo_cuenta, cupo): 
		self.__titular = titular
		self.__saldo = saldo
		self.__numero_cuenta = numero_cuenta
		self.__id_titular = id_titular
		self.__fecha = fecha
		self.__tipo_cuenta = self.validar_tipo_cuenta(tipo_cuenta)
		self.__cupo = cupo
		
	def validar_tipo_cuenta(self, tipo_cuenta):
		if tipo_cuenta in CuentaBancaria.TIPO_CUENTA:
			return tipo_cuenta
		return CuentaBancaria.TIPO_CUENTA[0]
		
	def retirar(self,monto):
		if self.__tipocuenta == CuentaBancaria.TIPOCUENTA[0]:
			if self.__saldo - monto >= 10000:
				self.__saldo -=monto
				return True
			else:
				return False
		elif self.__tipo_cuenta == CuentaBancaria.TIPOCUENTA[1]:
			if self.__saldo + self.__cupo - monto >=0:
				self.__saldo -= monto		
				return True
				
			else:
				return False
				
		return False
	
	def depositar(self,monto):
		if monto>0:
			self.__saldo += monto
			return True
		return False
		
	def consultar(self):
		return self.__saldo
	
	def set_titular(self,titular):
		self.__titular = titular
	
	def get_titular(self):
		return self.__titular
		
	def set_numero_cuenta(self, numero_cuenta):
		self.__numero_cuenta = numero_cuenta
		
	def get_numero_cuenta(self):
		return self.__numero_cuenta
		
	def set_id_titular(self, id_titular):
		self.__id_titular = id_titular
		
	def get_id_titular(self):
		return self.__id_titular
	
	def set_fecha (self,fecha):
		self.__fecha = fecha

	def get_fecha(self):
		return self.__fecha
		
	def set_tipo_cuenta(self,tipo_cuenta):
		self.__tipo_cuenta = self.validar_tipo_cuenta(tipo_cuenta)
		
	def get_tipo_cuenta(self):
		return self.__tipo_cuenta
		
	def set_cupo(self, cupo):
		if cupo>0:
			self.__cupo = cupo
	
	def get_cupo(self):
		return cupo
		
				
		
		
		

