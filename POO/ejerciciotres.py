# -*- coding: utf-8 -*-

from datetime import datetime

class Date: 
	MONTHS = ("January","February","March", "April", "May", "June", "July", "August","September", "October", "November","December")
	def __init__(self,*args):
		date = datetime.now()
		if len(args)!=3:
			self.day = date.day
			self.month = date.month
			self.year = date.year
			
		elif len(args)==3:
			if self.validate_year(args[0]):
				self.year = args [0]
				
				if self.validate_month(args[1]):
					self.month = args[1]
					
					if self.validate.day(args[2]):
						self.day = args[2]
					
					else:
						self.day = date.day
				else:
					self.month = date.month
			else:
				self.year = date.year
		
			
			
	def validate_month(self,month):
		if 0 < year <=12:
			return True
		return False
		
	def validate_year(self,year):
		if year>0:
			return True
		return False
	
	def validate_day(self,day):
		if self.month in [4,6,9,11]:
			if 1<= day <= 30:
				return True
		elif self.month in [1,3,5,7,8,10,12]:		
			if 1<= day <=31:
				return True
				
		elif self.month==2:	
			if self.is_leap(self.year):
				if 1<= day <=29:
					return True 
			else:
				if 1 <= day <=28:
					return True 
		return False
		
	def is_leap(self,year):
		if self.year %4==0 and (year%100!=0 or year %400==0):
			return True 
		return False
			
	def update_date(self,year,month,day):
		
		if self.validate_year(year):
				self.year = year
				
		if self.validate_month(month):
					self.month = month
					
		if self.validate.day(day):
						self.day = day
		
	def view_date(self):
		print "%d/%s/%d"%self.day,Date.MONTHS[self.month -1],self.year
