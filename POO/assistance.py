# -*- coding: utf-8 -*-

from date import Date
from student import Student 
from laboratorio import Laboratory

class AssistanceLaboratory:
	
	def __init__(self,date,laboratory,code):
		self.__code = code
		self.__date = date
		self.__laboratory = laboratory
		self.__students = []
		
	def get_code(self):
		return self.__code
		
	def search_student(self,student):
		for item_student in self.__students:
			if item.student.get_code() == student.get_code():
				return True
		return False
			
		
		
	def  add_student(self,student):
		if not self.search_student(student):
			self.__students.append(students)
			return True
		return False
				
		
