# -*- coding: utf-8 -*-
import pickle

class Schoolfile: 
	def __init__(self,file_name):
		self.__file_name = file_name 
		file.close()
	def save(self,data):
		file = open(self.__file_name, 'wb')
		pickle.dump(data, file)
		file.close()
		
	def load(self):	
		file = open(self.__file_name, 'rb')
		data = pickle.load(file)
		file.close()
		return data
