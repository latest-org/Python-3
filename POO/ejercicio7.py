#-*-coding:utf-8-*-

from datetime import datetime

class Producto(object):

	def __init__(self,id_producto,clase, precio_compra, cantidad,precio_venta,nombre):
	
		self.__id_producto = id_producto		
		self.__clase = clase
		self.__precio_compra = precio_compra
		self.__precio_venta = precio_venta
		self.__cantidad = cantidad
		self.__nombre = nombre
		
	def set_id_producto(self,id_producto):
		self.__id_producto = id_producto
		
	def get_id_producto(self):
		return self.__id_producto
		
	def set_clase(self,clase):
		self.__clase = clase
		
	def get_clase(self):
		return self.__clase
		
	def set_pecio_compra(self,precio_compra):
		self.__precio_compra  = precio_compra
	
	def get_precio_compra(self):
		return self.__precio_compra
		
	def set_cantidad(self,cantidad):
		self.__cantidad = cantidad
	
	def get_cantidad(self):
		return self.__cantidad
		
	def	set_precio_venta(self,precio_venta):
		self.__precio_venta = precio_venta
		
	def get_precio_venta(self):
		return self.__precio_venta
			
	def set_nombre (self,nombre):
		self.__nombre = nombre
		
	def get_nombre(self):
		return self.__nombre
		
		
