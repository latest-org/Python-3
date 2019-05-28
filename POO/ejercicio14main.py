# -*- coding: utf-8 -*-
from os import system
from ejercicio14alumno import Alumno
from ejercicio14curso import Curso


class Colegio():
	def __init__(self):
		self.lista_cursos = []
		self.lista_alumnos = []

	def buscar_alumno(self, id_alumno):
		pos = 0
		for alumno in self.lista_alumnos:
			if alumno.get_id() == id_alumno:
				return pos
			pos += 1
		return -1

	def adicionar_alumno(self):
		try:
			id = raw_input("Digite el ID del Alumno: ")
			nombre = raw_input("Digite el Nombre del Alumno: ")
			promedio = float(raw_input("Digite el promedio del Alumno: "))
			alumno = Alumno(id, nombre, promedio)
			self.lista_alumnos.append(alumno)
			print "**************************************"
			print "¡El alumno se adiciono correctamente!"
			print "**************************************"
			raw_input()

		except ValueError:
			print "**************************************"
			print "ERROR - El promedio debe ser un numero"
			print "**************************************"
			raw_input()

	def visualizar_alumno(self):
		id_alumno = raw_input("Digite el ID del Alumno: ")
		pos = self.buscar_alumno(id_alumno)
		if pos != -1:
			print "**************************************"
			print "          DATOS DEL ALUMNO            "
			print "**************************************"
			print "ID: %s" % (self.lista_alumnos[pos].get_id())
			print "Nombre: %s" % (self.lista_alumnos[pos].get_nombre())
			print "Promedio: %.1f" % (self.lista_alumnos[pos].get_promedio())
			raw_input()
		else:
			print "**************************************"
			print "INFO - El Alumno no existe            "
			print "**************************************"
			raw_input()

	def modificar_alumno(self, op):
		id_alumno = raw_input("Digite el ID del Alumno: ")
		pos = self.buscar_alumno(id_alumno)
		if pos != -1:
			print "**************************************"
			print "          DATOS DEL ALUMNO            "
			print "**************************************"
			print "ID: %s" % (self.lista_alumnos[pos].get_id())
			print "Nombre: %s" % (self.lista_alumnos[pos].get_nombre())
			print "Promedio: %.1f" % (self.lista_alumnos[pos].get_promedio())
			print "**************************************"

			if op == 1:
				id = raw_input("Digite el nuevo ID: ")
				self.lista_alumnos[pos].set_id(id)
				for curso in self.lista_cursos:
					curso.modificar_alumno(self.lista_alumnos[pos])
				print "********************************************"
				print "¡El ID del alumno se modificó correctamente!"
				print "********************************************"
				raw_input()

			elif op == 2:
				nombre = raw_input("Digite el nuevo Nombre: ")
				self.lista_alumnos[pos].set_nombre(nombre)
				for curso in self.lista_cursos:
					curso.modificar_alumno(self.lista_alumnos[pos])
				print "************************************************"
				print "¡El Nombre del alumno se modificó correctamente!"
				print "************************************************"
				raw_input()

			elif op == 3:
				try:
					promedio = float(raw_input("Digite el nuevo Promedio: "))
					self.lista_alumnos[pos].set_promedio(promedio)
					for curso in self.lista_cursos:
						curso.modificar_alumno(self.lista_alumnos[pos])
					print "*************************************************"
					print "¡El Promedio del alumno se modificó correctamente!"
					print "*************************************************"
					raw_input()

				except ValueError:
					print "**************************************"
					print "ERROR - El promedio debe ser un numero"
					print "**************************************"
					raw_input()

			elif op == 4:
				try:
					id = raw_input("Digite el ID del Alumno: ")
					nombre = raw_input("Digite el Nombre del Alumno: ")
					promedio = float(raw_input("Digite el promedio del Alumno: "))
					self.lista_alumnos[pos].set_id(id)
					self.lista_alumnos[pos].set_nombre(nombre)
					self.lista_alumnos[pos].set_promedio(promedio)
					for curso in self.lista_cursos:
						curso.modificar_alumno(self.lista_alumnos[pos])
					print "**************************************"
					print "¡El alumno se modificó correctamente!"
					print "**************************************"
					raw_input()

				except ValueError:
					print "**************************************"
					print "ERROR - El promedio debe ser un numero"
					print "**************************************"
					raw_input()

			else:
				print "**************************************"
				print "ERROR - Opcion del menu invalida"
				print "**************************************"

		else:
			print "**************************************"
			print "INFO - El Alumno no existe            "
			print "**************************************"
			raw_input()


	def borrar_alumno(self):
		id_alumno = raw_input("Digite el ID del Alumno: ")
		pos = self.buscar_alumno(id_alumno)
		if pos != -1:
			print "**************************************"
			print "          DATOS DEL ALUMNO            "
			print "**************************************"
			print "ID: %s" % (self.lista_alumnos[pos].get_id())
			print "Nombre: %s" % (self.lista_alumnos[pos].get_nombre())
			print "Promedio: %.1f" % (self.lista_alumnos[pos].get_promedio())
			print "**************************************"
			print "ESTA SEGURO QUE DESEA BORRAR EL ALUMNO?"
			print "1=SI"
			print "2=NO"
			print "**************************************"

			try:
				op = int(raw_input("Digite su opción: "))
				if op == 1:
					for curso in self.lista_cursos:
						curso.remover_alumno(self.lista_alumnos[pos])
					
					del(self.lista_alumnos[pos])
					print "**************************************"
					print "¡El alumno se eliminó correctamente!"
					print "**************************************"
					raw_input()

			except ValueError:
				print "*******************************************"
				print "ERROR - La opcion debe ser un numero entero"
				print "*******************************************"
				raw_input()	

		else:
			print "**************************************"
			print "INFO - El Alumno no existe            "
			print "**************************************"
			raw_input()

	def listar_alumnos(self):
		print "**************************************"
		print "        DATOS DE LOS ALUMNOS          "
		print "**************************************"
		for alumno in self.lista_alumnos:
			print "**************************************"
			print "ID: %s" % (alumno.get_id())
			print "Nombre: %s" % (alumno.get_nombre())
			print "Promedio: %.1f" % (alumno.get_promedio())
		print "**************************************"
		raw_input()

	def buscar_curso(self, id_curso):
		pos = 0
		for curso in self.lista_cursos:
			if curso.get_id() == id_curso:
				return pos
			pos += 1
		return -1

	def adicionar_curso(self):
		print "***********************************"
		print "          ADICIONAR CURSO          "
		print "***********************************"
		id = raw_input("Digite el ID del curso: ")
		nombre = raw_input("Digite el nombre del curso: ")
		descripcion = raw_input("Digite la descripcion del curso: ")
		curso = Curso(id, nombre, descripcion)
		self.lista_cursos.append(curso)
		print "**************************************"
		print "¡El curso se adiciono correctamente!"
		print "**************************************"
		raw_input()

	def visualizar_curso(self):
		id_curso = raw_input("Digite el ID del Curso: ")
		pos = self.buscar_curso(id_curso)
		if pos != -1:
			print "**************************************"
			print "          DATOS DEL CURSO             "
			print "**************************************"
			print "ID: %s" % (self.lista_cursos[pos].get_id())
			print "Nombre: %s" % (self.lista_cursos[pos].get_nombre())
			print "Descripción: %s" % (self.lista_cursos[pos].get_descripcion())
			raw_input()
		else:
			print "**************************************"
			print "INFO - El Curso no existe            "
			print "**************************************"
			raw_input()

	def modificar_curso(self, op):
		id_curso = raw_input("Digite el ID del Curso: ")
		pos = self.buscar_curso(id_curso)
		if pos != -1:
			print "**************************************"
			print "          DATOS DEL CURSO             "
			print "**************************************"
			print "ID: %s" % (self.lista_cursos[pos].get_id())
			print "Nombre: %s" % (self.lista_cursos[pos].get_nombre())
			print "Descripción: %s" % (self.lista_cursos[pos].get_descripcion())
			print "**************************************"

			if op == 1:
				id = raw_input("Digite el nuevo ID: ")
				self.lista_cursos[pos].set_id(id)
				print "********************************************"
				print "¡El ID del curso se modificó correctamente!"
				print "********************************************"
				raw_input()

			elif op == 2:
				nombre = raw_input("Digite el nuevo Nombre: ")
				self.lista_cursos[pos].set_nombre(nombre)
				print "************************************************"
				print "¡El Nombre del curso se modificó correctamente!"
				print "************************************************"
				raw_input()

			elif op == 3:
				descripcion = raw_input("Digite la nueva descripción: ")
				self.lista_cursos[pos].set_descripcion(descripcion)
				print "****************************************************"
				print "¡La descripción del curso se modificó correctamente!"
				print "****************************************************"
				raw_input()

			elif op == 4:
				id = raw_input("Digite el ID del Curso: ")
				nombre = raw_input("Digite el Nombre del Curso: ")
				descripcion = raw_input("Digite la descripción del Curso: ")
				self.lista_cursos[pos].set_id(id)
				self.lista_cursos[pos].set_nombre(nombre)
				self.lista_cursos[pos].set_descripcion(descripcion)
				print "**************************************"
				print "¡El curso se modificó correctamente!"
				print "**************************************"
				raw_input()

			else:
				print "**************************************"
				print "ERROR - Opcion del menu invalida"
				print "**************************************"

		else:
			print "**************************************"
			print "INFO - El Curso no existe            "
			print "**************************************"
			raw_input()


	def borrar_curso(self):
		id_curso = raw_input("Digite el ID del Curso: ")
		pos = self.buscar_curso(id_curso)
		if pos != -1:
			print "**************************************"
			print "          DATOS DEL CURSO             "
			print "**************************************"
			print "ID: %s" % (self.lista_cursos[pos].get_id())
			print "Nombre: %s" % (self.lista_cursos[pos].get_nombre())
			print "Descripción: %s" % (self.lista_cursos[pos].get_descripcion())
			print "**************************************"
			print "ESTA SEGURO QUE DESEA BORRAR EL CURSO?"
			print "1=SI"
			print "2=NO"
			print "**************************************"

			try:
				op = int(raw_input("Digite su opción: "))
				if op == 1:
					del(self.lista_cursos[pos])
					print "**************************************"
					print "¡El curso se eliminó correctamente!"
					print "**************************************"
					raw_input()

			except ValueError:
				print "*******************************************"
				print "ERROR - La opcion debe ser un numero entero"
				print "*******************************************"
				raw_input()	

		else:
			print "**************************************"
			print "INFO - El Curso no existe            "
			print "**************************************"
			raw_input()

	def listar_cursos(self):
		print "**************************************"
		print "        DATOS DE LOS CURSOS           "
		print "**************************************"
		for curso in self.lista_cursos:
			print "**************************************"
			print "ID: %s" % (curso.get_id())
			print "Nombre: %s" % (curso.get_nombre())
			print "Descripción: %s" % (curso.get_descripcion())
		print "**************************************"
		raw_input()

	def encabezado_menu_modificar_alumno(self):
		system("clear")
		print "***********************************"
		print "         MODIFICAR ALUMNO          "
		print "***********************************"
		print "1=Modificar ID"
		print "2=Modificar Nombre"
		print "3=Modificar Promedio"
		print "4=Modificar Todos"
		print "5=Salir"
		print "***********************************"

	def menu_modificar_alumno(self):
		while True:
			self.encabezado_menu_modificar_alumno()
			try:
				op = int(raw_input("DIGITE SU OPCION: "))
				print "***********************************"
				
				if op in [1, 2, 3, 4]:
					self.modificar_alumno(op)

				elif op == 5:
					break	

			except ValueError:
				print "*******************************************"
				print "ERROR - La opcion debe ser un numero entero"
				print "*******************************************"
				raw_input()	

	def encabezado_menu_administrar_alumno(self):
		system("clear")
		print "***********************************"
		print "        ADMINISTRAR ALUMNO         "
		print "***********************************"
		print "1=Adicionar Alumno"
		print "2=Visualizar Alumno"
		print "3=Modificar Alumno"
		print "4=Borrar Alumno"
		print "5=Listar Alumnos"
		print "6=Salir"
		print "***********************************"

	def menu_administrar_alumno(self):
		while True:
			self.encabezado_menu_administrar_alumno()
			try:
				op_alumno = int(raw_input("DIGITE SU OPCION: "))
				print "***********************************"

				if op_alumno == 1:
					self.adicionar_alumno()

				elif op_alumno == 2:
					self.visualizar_alumno()

				elif op_alumno == 3:
					self.menu_modificar_alumno()

				elif op_alumno == 4:
					self.borrar_alumno()	

				elif op_alumno == 5:
					self.listar_alumnos()	

				elif op_alumno == 6:
					break	

			except ValueError:
				print "*******************************************"
				print "ERROR - La opcion debe ser un numero entero"
				print "*******************************************"
				raw_input()	

	def encabezado_menu_modificar_curso(self):
		system("clear")
		print "***********************************"
		print "         MODIFICAR CURSO           "
		print "***********************************"
		print "1=Modificar ID"
		print "2=Modificar Nombre"
		print "3=Modificar Descripción"
		print "4=Modificar Todos"
		print "5=Salir"
		print "***********************************"

	def menu_modificar_curso(self):
		while True:
			self.encabezado_menu_modificar_curso()
			try:
				op = int(raw_input("DIGITE SU OPCION: "))
				print "***********************************"
				
				if op in [1, 2, 3, 4]:
					self.modificar_curso(op)

				elif op == 5:
					break	

			except ValueError:
				print "*******************************************"
				print "ERROR - La opcion debe ser un numero entero"
				print "*******************************************"
				raw_input()	

	def encabezado_menu_administrar_curso(self):
		system("clear")
		print "***********************************"
		print "        ADMINISTRAR CURSO          "
		print "***********************************"
		print "1=Adicionar Curso"
		print "2=Visualizar Curso"
		print "3=Modificar Curso"
		print "4=Borrar Curso"
		print "5=Listar Cursos"
		print "6=Salir"
		print "***********************************"

	def menu_administrar_curso(self):
		while True:
			self.encabezado_menu_administrar_curso()
			try:
				op = int(raw_input("DIGITE SU OPCION: "))
				print "***********************************"

				if op == 1:
					self.adicionar_curso()

				elif op == 2:
					self.visualizar_curso()

				elif op == 3:
					self.menu_modificar_curso()

				elif op == 4:
					self.borrar_curso()	

				elif op == 5:
					self.listar_cursos()	

				elif op == 6:
					break	

			except ValueError:
				print "*******************************************"
				print "ERROR - La opcion debe ser un numero entero"
				print "*******************************************"
				raw_input()

	def matricular_alumnos(self):
		system("clear")
		print "***********************************"
		print "       MATRICULAR ALUMNO           "
		print "***********************************"
		id_alumno = raw_input("Digite el ID del Alumno: ")
		pos_alumno = self.buscar_alumno(id_alumno)

		if pos_alumno != -1:
			print "***********************************"
			id_curso = raw_input("Digite el ID del curso: ")
			pos_curso = self.buscar_curso(id_curso)

			if pos_curso != -1:
				if self.lista_cursos[pos_curso].matricular_alumno(self.lista_alumnos[pos_alumno]):
					print "**************************************"
					print "¡El alumno se matriculó correctamente!"
					print "**************************************"
					raw_input()
				else:
					print "***************************************"
					print "ERROR - El alumno no se pudo matricular"
					print "***************************************"
					raw_input()
			else:
				print "**************************************"
				print "ERROR - El curso no existe"
				print "**************************************"
				raw_input()

		else:
			print "**************************************"
			print "ERROR - El alumno existe"
			print "**************************************"
			raw_input()

	def listar_alumnos_curso(self):
		system("clear")
		print "***********************************"
		print "   LISTADO ALUMNOS DE UN CURSO     "
		print "***********************************"
		id_curso = raw_input("Digite el ID del Curso: ")
		pos = self.buscar_curso(id_curso)

		if pos != -1:
			self.lista_cursos[pos].mostrar_nomina()
		else:
			print "**************************************"
			print "ERROR - El curso no existe"
			print "**************************************"
			raw_input()

	def desvincular_alumnos(self):
		system("clear")
		print "***********************************"
		print "       DESVINCULAR ALUMNO          "
		print "***********************************"
		id_alumno = raw_input("Digite el ID del Alumno: ")
		pos_alumno = self.buscar_alumno(id_alumno)

		if pos_alumno != -1:
			print "***********************************"
			id_curso = raw_input("Digite el ID del curso: ")
			pos_curso = self.buscar_curso(id_curso)

			if pos_curso != -1:
				if self.lista_cursos[pos_curso].remover_alumno(self.lista_alumnos[pos_alumno]):
					print "**************************************"
					print "¡El alumno se desvinculó correctamente!"
					print "**************************************"
					raw_input()
				else:
					print "****************************************"
					print "ERROR - El alumno no se pudo desvincular"
					print "****************************************"
					raw_input()
			else:
				print "**************************************"
				print "ERROR - El curso no existe"
				print "**************************************"
				raw_input()

		else:
			print "**************************************"
			print "ERROR - El alumno existe"
			print "**************************************"
			raw_input()

	def encabezado_menu(self):
		system("clear")
		print "***********************************"
		print "***********************************"
		print "******                      *******"
		print "******     COLEGIO JAIME    *******"
		print "****** La Alegría de Crecer *******"
		print "******                      *******"
		print "***********************************"
		print "***********************************"
		print "***********************************"
		print "           MENU PRINCIPAL          "
		print "***********************************"
		print "***********************************"
		print "1=Administrar Alumno"
		print "2=Administrar Curso"
		print "3=Matricular Alumno a un Curso"
		print "4=Listar Alumnos por Curso"
		print "5=Desvincular Alumno de un Curso"
		print "6=Salir"
		print "***********************************"
		print "***********************************"

	def menu_principal(self):
		while True:
			self.encabezado_menu()
			try:
				op = int(raw_input("DIGITE SU OPCION: "))
				print "***********************************"

				if op == 1:
					self.menu_administrar_alumno()

				elif op == 2:
					self.menu_administrar_curso()

				elif op == 3:
					self.matricular_alumnos()

				elif op == 4:
					self.listar_alumnos_curso()

				elif op == 5:
					self.desvincular_alumnos()

				elif op == 6:
					break

			except ValueError:
				print "*******************************************"
				print "ERROR - La opcion debe ser un numero entero"
				print "*******************************************"
				raw_input()
	

if __name__ == '__main__':
	colegio = Colegio()
	colegio.menu_principal()


