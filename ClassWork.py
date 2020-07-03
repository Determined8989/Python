from datetime import date
class Person():
	middlename = ''
	firstname = ''
	secondname = ''
	dateofbirth = ''
	def __init__ (self,middlename,firstname,secondname,dateofbirth):
		self.middlename = middlename
		self.firstname = firstname
		self.secondname = secondname
		self.dateofbirth = dateofbirth
		#self.document = document
	def Presentation(self):
		print(
			'Фамилия:',self.middlename,
			',имя:',self.firstname,
			',отчество:',self.secondname,
			',Дата Рождения:',self.dateofbirth)
	def FullName(self):
		print(
			'Фамилия:',self.middlename,
			',имя:',self.firstname,
			',отчество:',self.secondname,
			',Дата Рождения:',self.dateofbirth)
	def FIO(self,middlename,initials):
		self.middlename = middlename
		print(self.middlename,
			initials)
			


Test = Person('Кушляев','Никита','Алексеевич','21.09.2004')
Test.FullName()
Test.FIO('Кушляев','Н.А')
Test.Presentation()
