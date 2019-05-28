# -*- coding: utf-8 -*-

from laboratorio import Laboratory
from student import Student
from assistance import AssistanceLaboratory
from ejerciciotres import Date
from school import School
from schoolfile import Schoolfile
class Menu:
	def __init__(self,school_name, school_file_name):
		self.school = School(school_name)
		self.school_file = Schoolfile(school_file_name)
		
	def create_student(self):	
		system("clear")
		print "***********************************"
		print "         CREATE STUDENT            "
		print "***********************************"
		student_first_name = (raw_input("Enter the student name: "))
		student_last_name = (raw_input("Enter the student last name: "))
		student_code = (raw_input("Enter the student code: "))
		student = Student(student_first_name,student_last_name,student_code)
		self.school.add_student(student)
		print "*******************************************"
		print "    THE STUDENT WAS ADDED  SUCCESSFULLY    "
		print "*******************************************"
		input()
		
	def create_laboratory(self):	
		system("clear")
		print "***********************************"
		print "         CREATE LABORATORY            "
		print "***********************************"
		laboratory_name = (raw_input("Enter the laboratory name: "))
		laboratory_capacity = input("Enter the  laboratory capacity: ")
		laboratory_code = (raw_input("Enter the laboratory code: "))
		student = Laboratory(laboratory_name,laboratory_capacity, laboratory_code)
		self.school.add_laboratory(laboratory)
		print "*******************************************"
		print "  THE LABORATORY WAS ADDED  SUCCESSFULLY   "
		print "*******************************************"
		input()
	
	
	def create_assistance_laboratory(self):
		system("clear")
		print "***********************************"
		print "   CREATE ASSISTANCE LABORATORY    "
		print "***********************************"
	    laboratory_code = raw_input("Enter the laboratory code: ")
		laboratory_position = self.school.search_laboratory (laboratory_code)
		if laboratory_position != False:	
			try:
				day = int (input("Enter the day: "))
				month = int (input("Enter the month: "))
				year = int (input("Enter the year: "))
				date = Date(year,month,day)
				assistance_code = int(input("Enter the assistance's code: "))
				assistance_laboratory = AssistanceLaboratory(date, self.school.get_laboratory(laboratory_position), assistance_code)
				while True:
					print "***********************************"
					print "        ASSISTANCE STUDENTS        "
					print "***********************************"
					print "1= Enter de student assistance"
					print "2 = Exit"
					print "***********************************"
					op = int(raw_input("ENTER YOUR OPTION: "))
					print "***********************************"
					
					if op ==1:
						student_code = input("Enter the student code: ")
						student_position = self.school.search_student(student_code)
						
						if student_position != False:
							assistance_laboratory.add_student(self.school.get_student(student_position))
							
						else
							print "****************************************************"
							print "ERROR -     THE STUDENT DOES NOT EXIST              "
							print "****************************************************"
							input()
					elif op ==2:
						break
					
					else:
						print "****************************************************"
						print "ERROR -            IVALID OPTION                    "
						print "****************************************************"
						input()
				self.school.add_assistance(assistance_laboratory)
			
			except ValueError:
				print "****************************************************"
				print "ERROR - The value entered must be a integer number  "
				print "****************************************************"
				input()
		else
			print "****************************************************"
			print "ERROR -     THE LABORATORY DOES NOT EXIST           "
			print "****************************************************"
						input()
	def head_menu(self):
		system("clear")
		print "***********************************"
		print "***********************************"
		print "******                      *******"
		print "******         SENA         *******"
		print "******      C.D.I.T.I       *******"
		print "******                      *******"
		print "***********************************"
		print "***********************************"
		print "***********************************"
		print "             MAIN MENU             "
		print "***********************************"
		print "***********************************"
		print "1=Create Students"
		print "2=Create Laboratories"
		print "3=Register assistance to Laboratory"
		print "4=Exit"
		print "***********************************"
		print "***********************************"
		
		
	def main_menu(self):
		while True:
			self.head_menu()
			try:
				op = int(raw_input("ENTER YOUR OPTION: "))
				print "***********************************"
				self.school_file.save(self.school)	
				if op == 1:
					self.create_student()

				elif op == 2:
					self.create_laboratory()

				elif op == 3:
					self.create_assistance_laboratory()

				elif op == 4:
					break
					

				

			except ValueError:
				print "*******************************************"
				print "ERROR - The value entered must be a number "
				print "*******************************************"
				input()
if __name__=='__main__':
	menu = Menu("SENA","School.data")
	menu.school = menu.school_file.load()
	menu.main_menu()
