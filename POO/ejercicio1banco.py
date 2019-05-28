#-*-coding:utf-8-*-
from datetime import datetime
import random
from ejercicio1cuenta import CuentaBancaria
from  os import system 
class Banco(object):
	def __init__(self):
		self.__cuentas = []
		self.__numeros_cuentas = []
		
	def buscar_cuenta(self,numer_cuenta):

		for a in range(len(self.__cuentas)):
			if numero_cuenta == self.__cuentas[a].get_numero_cuenta():
				return a
		return -1
		
			
	def adicionar_cuenta(self,cuenta):
		pos = self.buscar_cuenta(cuenta.get_numero_cuenta())
		if pos == -1:
			self.__cuentas.append(cuenta)
			return True 
		return False
		
	def depositar_monto_cuenta(self,monto,numero_cuenta):
		pos = self.buscar_cuenta(numero_cuenta)
		if pos !=-1:
			self.__cuentas[pos].depositar(monto)
			return True
		return False	
		
	def retirar_monto_cuenta(self,monto,numero_cuenta):
		pos = self.buscar_cuenta(numero_cuenta)
		if pos !=-1:
			self.__cuentas[pos].retirar(monto)
			return True
		return False	
		
		
	def consultar_saldo_cuenta(self,monto,numero_cuenta):
		pos = self.buscar_cuenta(numero_cuenta)
		saldo =-1
		if pos !=-1:
			saldo = self.__cuentas[pos].consultar()
		return saldo
			
		
	def generar_numero_cuenta(self):
		while True:
			numero = random.randint(10000000,99999999)
			if numero not in self.__numeros_cuentas:
				self.__numeros_cuentas.append(numero)
				break
		return numero
		
	def pedir_datos_retiro_cuenta(self):	
		try:
			print "***********************************"
			print "              RETIROS              "
			print "***********************************"
			numero_cuenta = int(input("Digite el numero de la cuenta: "))
			monto = float(input("Digite la cantidad de dinero a retirar de la cuenta: "))
			if self.retirar_monto_cuenta(monto,numero_cuenta):
				print "*******************************************"
				print "    El retiro se realizo correctamente!     "
				print "*******************************************"
				raw_input()
			else:
				print "*******************************************"
				print "   El retiro no se realizo correctamente!  "
				print "*******************************************"
				raw_input()
				
		except ValueError:
						print "*******************************************"
						print "ERROR - el valor del monto debe ser numerico"
						print "*******************************************"
						input()
						
	def pedir_datos_deposito_cuenta(self):	
		try:
			print "***********************************"
			print "            DEPÓSITOS              "
			print "***********************************"
			numero_cuenta = int(input("Digite el numero de la cuenta: "))
			monto = float(input("Digite la cantidad de dinero a depositar en la cuenta: "))
			if self.depositar_monto_cuenta(monto,numero_cuenta):
				print "*******************************************"
				print "    El deposito se realizo correctamente!     "
				print "*******************************************"
				raw_input()
			else:
				print "*******************************************"
				print "   El deposito no se realizo correctamente!  "
				print "*******************************************"
				raw_input()
				
		except ValueError:
						print "*******************************************"
						print "ERROR - el valor del monto debe ser numerico"
						print "*******************************************"
						input()
	
	def mostrar_saldo_cuenta(self):
		try:
			print "***********************************"
			print "       SALDO DE TU CUENTA          "
			print "***********************************"
			numero_cuenta = int(input("Digite el numero de la cuenta: "))
			print "*******************************************"
			print "  El saldo de su cuenta es: $%.2f    "%(self.consultar_saldo_cuenta(numero_cuentas))
			print "*******************************************"
			raw_input()
		except ValueError:
			print "*******************************************"
			print "ERROR - el valor del monto debe ser numerico"
			print "*******************************************"
			input()
	
	
	def pedir_datos_cuenta(self):
		try:
	
			print "***********************************"
			print "            CREAR CUENTA           "
			print "***********************************"
			titular = raw_input("Digite el nombre del titular de la cuenta: ")
			saldo = float(raw_input("Digite el saldo inicial de la cuenta: "))
			numero_cuenta = self.generar_numero_cuenta()
			id_titular = int(raw_input("Digite el numero de identificacion del titular de la cuenta: "))
			fecha_actual = datetime.now()
		
			while True:
			
				print "************************************"		
				print "          Tipos de Cuenta           " 
				print "************************************"
				print "1 = Ahorro"
				print "2 = Corriente"
				print "************************************"
				try:
					op_tipo_cuenta = int(input("Elija tipo de cuenta: "))
					if op_tipo_cuenta ==1:
						tipo_cuenta = "Ahorro"
						cupo = 0
						break
					elif op_tipo_cuenta ==2:
						tipo_cuenta = "Corriente"

						try:
							cupo = float(input("Digite el cupo asignado para la cuenta: "))
							break
						except ValueError:	
							print "*******************************************"
							print "ERROR - La opcion debe ser un numero entero"
							print "*******************************************"
							input()
						
					else:
						print"********************************************"
						print "  ERROR - Opcion fuera del rango   (1,2)    "
						print "********************************************"
						input()
						
				
				except ValueError:
					print "*******************************************"
					print "ERROR - La opcion debe ser un numero entero"
					print "*******************************************"
					input()
					
			cuenta = CuentaBancaria(titular,saldo,numero_cuenta,id_titular,fecha_actual,tipo_cuenta,cupo)
			self.adicionar_cuenta(cuenta)
			print "*******************************************"
			print "      La cuenta se creo correctamente      "
			print "*******************************************"
			raw_input()
				
		except ValueError:
			print "*******************************************"
			print "ERROR - La opcion debe ser un numero entero"
			print "*******************************************"
			input()
	
	def encabezado_menu(self):
		system("clear")
		print "***********************************"
		print "***********************************"
		print "******                      *******"
		print "******    BANCO SANTIAGO    *******"
		print "******                      *******"
		print "***********************************"
		print "***********************************"
		print "***********************************"
		print "           MENU PRINCIPAL          "
		print "***********************************"
		print "***********************************"
		print "1=Crear Cuenta"
		print "2=Retiros"
		print "3=Depositos"
		print "4=Consultar Saldo"
		print "5=Salir"
		print "***********************************"
		print "***********************************"
		
		
	def menu_principal(self):
		while True:
			self.encabezado_menu()
			try:
				op = int(raw_input("DIGITE SU OPCION: "))
				print "***********************************"

				if op == 1:
					self.pedir_datos_cuenta()

				elif op == 2:
					self.pedir_datos_retiro_cuenta()

				elif op == 3:
					self.pedir_datos_deposito_cuenta()

				elif op == 4:
					self.mostrar_saldo_cuenta()

				elif op == 5:
					break

			except ValueError:
				print "*******************************************"
				print "ERROR - La opcion debe ser un numero entero"
				print "*******************************************"
				input()
if __name__=='__main__':
	banco = Banco()
	banco.menu_principal()
