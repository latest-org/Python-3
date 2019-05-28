# -*- coding: utf-8 -*-

class Student:

	def __init__(self,first_name,last_name,code):
		self.__first_name = first_name
		self.__last_name = last_name
		self.__code = code
		
	def set_first_name(self,first_name):
		self.__first_name = first_name
		
	def get_first_name(self):
		return self.__first_name
		
	def set_last_name(self,last_name):
		self.__last_name = last_name
		
	def get_last_name(self):
		return self.__last_name 
	
	def set_code(self, code):
		self.__code = code
	
	def get_code (self):
		return self.__code
