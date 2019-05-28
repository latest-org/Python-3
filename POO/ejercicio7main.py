# -*- coding: utf-8 -*-
from ejercicio7 import Producto
from os import system 
''''7.El sistema es para una microempresa que fabrica y vende ropa, esta empresa requiere 
tener una relación completa de los productos que tiene en el almacén, y que cuando se realice 
una venta además de que se imprima una nota y se pueda registrar el efectivo recibido para que el 
sistema entregue cuanto cambio se debe dar, las existencias del almacén se actualicen de acuerdo a 
la venta realizada, por otro lado necesita que al terminar un día, una semana y un mes, el sistema 
entregue un reporte de las ventas realizadas así como el dinero obtenido, también requiere que cuando 
queden menos de 8 productos de un mismo tipo el sistema de un aviso de que el producto se está terminando.
Además de que se puedan agregar y dar de baja productos, también se debe tener la opción de ingresar 
las inversiones que se han hecho para que se puedan visualizar las ganancias obtenidas.'''

class Menu(object):
	def __init__(self):
		self.lista_producto = []
		
	def agregar_producto(self):
		try:
			print "*********************PRODUCTO***************************"
			id_producto = int(raw_input("Ingrese el id del producto a crear: "))
			print "\n"
			pos = self.buscar_producto(id_producto)
			if pos == -1:
				clase = str(raw_input("Ingrese la clase de producto: "))
				precio_compra = int(raw_input("Ingrese su precio de compra: "))
				cantidad = int (raw_input("Ingrese la cantidad: "))
				precio_venta = int (raw_input("Ingrese su precio de venta: "))
				nombre = str(raw_input("Ingrese el nombre del producto: "))										
				producto = Producto(id_producto,clase, precio_compra, cantidad,precio_venta,nombre)
				if producto not in self.lista_producto:
					self.lista_producto.append(producto)
					print "*********EL PRODUCTO SE AGREGO CORRECTAMENTE***********"
					print "el id del producto es : %d"%id_producto
					print "********************************************************"
					raw_input()
			else:
				print "*************************************************************"
				print "********************EL PRODUCTO YA EXISTE********************"
				print "*************************************************************"
				raw_input()
		except ValueError:
			print "Error"
	
	def listar_productos(self):
		id_producto = int(raw_input("Ingrese el id del producto para listar: "))
		"\n"
		pos = self.buscar_producto(id_producto)	
		if pos != -1:
			print "El nombre del producto es %s"%(self.lista_producto[pos].get_nombre())
			print "La cantidad de productos es %d"%(self.lista_producto[pos].get_cantidad())
			print "El id del producto es %d"%(self.lista_producto[pos].get_id_producto())
			print "El precio del producto es %d"%(self.lista_producto[pos].get_precio_venta())
			print "La clase del producto es %s"%(self.lista_producto[pos].get_clase())
			raw_input()	
	
	def buscar_producto(self,id_producto):
		
		pos = 0 
		for producto in self.lista_producto:
			if producto.get_id_producto() == id_producto:
				return pos
			pos+=1
		return -1
		
	def realizar_venta(self):
		id_producto = int(raw_input("Ingrese el id del producto para para comprar: "))
		"\n"
		pos = self.buscar_producto(id_producto)	
		if pos != -1:
			print "El nombre del producto es %s"%(self.lista_producto[pos].get_nombre())
			print "La cantidad de productos es %d"%(self.lista_producto[pos].get_cantidad())
			print "El id del producto es %d"%(self.lista_producto[pos].get_id_producto())
			print "El precio del producto es %d"%(self.lista_producto[pos].get_precio_venta())
			print "La clase del producto es %s"%(self.lista_producto[pos].get_clase())
			"\n"
			cantidad_productos = int(raw_input("Ingrese la cantidad de productos que quiere comprar: "))
			cantidad_dinero = int(raw_input("Ingrese el monto con el que va a pagar: "))
			
			raw_input()
		else:
			print "*************************************************************"
			print "********************EL PRODUCTO NO EXISTE********************"
			print "*************************************************************"
			raw_input()
			
	def eliminar_producto(self):
		
	
	def head_menu(self):
		system("clear")
		print "***********************************"
		print "***********************************"
		print "******                      *******"
		print "******       UNDERWEAR      *******"
		print "******                      *******"
		print "******                      *******"
		print "***********************************"
		print "***********************************"
		print "***********************************"
		print "               MENU                "
		print "***********************************"
		print "***********************************"
		print "1=Crear producto"
		print "2=Vender producto"
		print "3=Eliminar producto"
		print "4=Listar producto"
		print "5=Reporte de venta"
		print "6=Salir"
		print "***********************************"
		print "***********************************"
		
	def menu_principal(self):
		while True:
			self.head_menu()
			try:
				opcion = int(raw_input("Elige una opcion dentro del rango: "))
				print "\n"
					
				if opcion ==1:
					self.agregar_producto()
								
				elif opcion ==2:	
					self.realizar_venta()
				
				elif opcion ==3:
					eliminar_producto()
				
				elif opcion==4:
					self.listar_productos()
						
				elif opcion==5:
					pass
						
				elif opcion ==6:
					break
				
				
			except ValueError:
				print "La cantidad ingresada esta fuera de rango"
				raw_input()
					
		
	
if __name__=='__main__':
	menu = Menu()
	menu.menu_principal()
