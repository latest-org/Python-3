# -*- coding: utf-8 -*-

from laboratorio import Laboratory
from student import Student
from assistance import AssistanceLaboratory

class School:
	
	def __init__ (self,name):
		self.__name = name
		self.__students = []
		self.__laboratories = []
		self.__assists = []
		
	def set_name(self):
		self.__name = name 
		
	def get_name(self):
		return self.__name
		
	def get_laboratory(self,position):
		return self.__laboratories[position]
		
	def get_student (self,position):
		return self.__students [position]
		
	def search_student(self,student_code):
		for a in range (len(self.__students)):
			if self.__students[a].get_code() ==student_code():
				return a
		return False
		
	def  add_student(self,student):
		if not self.search_student(student.get_code()):
			self.__students.append(students)
			return True
		return False	
		
	def search_laboratory(self,laboratory_code):
		for a in range (len(self.__laboratories)):
			if self.__laboratories[a].code ==laboratory_code:
				return a
		return False
		
	def add_laboratory(self,laboratory):
		if not self.search_laboratory(laboratory.code):
			self.__laboratories.append(laboratory)
			return True
		return False
		
	def search_assistance(self,assistance):
		for item_assistance in self.__assists:
			if item_assistance.get_code() in assistance.get_code():
				return True
		return False
		
	def add_assistance(self,assistance):
		if not self.seach.assistance(assistance):
			self.__assists,append(assistance)	
			return True
		return False
		
			
	
