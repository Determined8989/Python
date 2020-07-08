import datetime
from datetime import date
class Person():
	def __init__ (self,secondname,firstname,middlename,dateofbirth,document):
		self.secondname = secondname
		self.firstname = firstname
		self.middlename = middlename
		self.dateofbirth = dateofbirth
		self.document = document
	def Presentation(self):
		print(
			'Фамилия:',self.secondname,
			',имя:',self.firstname,
			',отчество:',self.middlename,
			',Дата Рождения:',self.dateofbirth)
	def FullName(self):
		return(self.secondname+' '+self.firstname+' '+self.middlename)
	def Age(self):
		present = date.today()
		return((int((present - self.dateofbirth).days//365.25)))
	def FIO(self):
		return(self.secondname+' '+self.firstname[:1]+'.'+self.middlename[:1]+'.')


class Document():
	def __init__(self,doctype,series,number,dateoffissue,validthru):
		self.doctype = doctype
		self.dateoffissue = dateoffissue
		self.validthru = validthru
		self.series = series
		self.number = number
	def isValid(self):
		if date.today() > self.validthru:
			result = False
		else:
			result = True
		return(('isValid:'+(str(result))))
	def Presentation(self):
		print(self.doctype,' cерия',self.series,'№', self.number,',выдан',self.dateoffissue, ', годен до ',self.validthru)

class Teacher():
	def __init__(self,person, schoolnum, mainsubject):
		self.person = person
		self.schoolnum = schoolnum
		self.mainsubject = mainsubject

class Mark():
	def __init__(self,date,tchr,subject,mark):
		self.date = date
		self.tchr = tchr
		self.subject = subject
		self.mark = mark
	def Presentation(self):
		result = '| %s | %s | %s | %s |' %(self.date.strftime("%Y.%m.%d"),self.subject.ljust(15)[:15],self.tchr.person.FIO().ljust(20)[:20],str(self.mark).ljust(6)[:6] )
		return(result)
class Diary():
	marks = []
	def Add(self,date,tchr,subject,mark):
		mark = Mark(date,tchr,subject,mark)
		self.marks.append(mark)
	def ShowMarks(self,date,subject):
		print( '| %s | %s | %s | %s |' %('Дата'.ljust(10)[:10],'Предмет'.ljust(15)[:15],'Преподаватель'.ljust(20)[:20],'Оценка'.ljust(6)[:6]))
		print('----------------------------------------------------------------')
		for mark in self.marks:
			result = True
			if not date is None and not date == mark.date:
				result = False
			if not subject is None and not subject == mark.subject:
				result = False
			if result:
				print(mark.Presentation())
	def ShowAverage(self):
		allmraks = {}
		print('| %s | %s |' %('Предмет'.ljust(15)[:15],'Оценка'.ljust(6)[:6]))
		print('----------------------------')
		for mark in  self.marks:
			listofmarks = allmraks.setdefault(mark.subject,[])
			listofmarks.append(mark.mark)
		for key, val in allmraks.items():
			avg = sum(val)/len(val)
			print('| %s | %s |' %(key.ljust(15)[:15], (str(avg).ljust(6)[:6])))
	def GetAverageScore(self,subject):
		self.subject = subject
		mraks = {}
		for mark in  self.marks:
			listofmarks = mraks.setdefault(self.subject,[])
			if subject == mark.subject:
				listofmarks.append(mark.mark)
		for key, val in mraks.items():
			avg = sum(val)/len(val)
			print('| %s | %s |' %('Предмет'.ljust(15)[:15],'Оценка'.ljust(6)[:6]))
			print('----------------------------')
			print('| %s | %s |' %(key.ljust(15)[:15], (str(avg).ljust(6)[:6])))


"""
class Student():
	person = 
	mother = 
	father = 
	schoolnum = 
	grade = 

"""


doc = Document('Паспорт',4569,456897, date(2019,10,15),date(2022,10,15))
doc2 = Document('Паспорт',2954,452954, date(2020,7,15),date(2023,7,15))
human = Person('Кушляев','Никита','Алексеевич', date(2004,9,21),doc)
human2 = Person('Грабко','Татьяна','Павловна',date(1978,5,23),doc2)
teacher1 = Teacher(human2,124,'IT')
teacher2 = Teacher(human,123,'English')
#print(mark1.Presentation())
#print(mark2.Presentation())
diary1 = Diary()
diary1.Add(date(2020,3,13),teacher1,'English',3)
diary1.Add(date(2020,3,13),teacher1,'English',4)
diary1.Add(date(2020,3,13),teacher1,'English',3)
diary1.Add(date(2020,3,13),teacher1,'English',5)
diary1.Add(date(2020,3,14),teacher1,'IT',5)
diary1.Add(date(2020,3,14),teacher1,'IT',4)
diary1.Add(date(2020,3,14),teacher1,'IT',5)
diary1.Add(date(2020,3,14),teacher1,'IT',3)
diary1.Add(date(2020,3,14),teacher1,'История',5)
diary1.Add(date(2020,3,14),teacher1,'История',5)
diary1.Add(date(2020,3,14),teacher1,'История',3)
diary1.Add(date(2020,3,14),teacher1,'История',4)
diary1.ShowMarks(date(2020,3,14),'IT')
#diary1.ShowAverage()
diary1.GetAverageScore('English')
#print(Diary1.ShowMarks(date(2020,3,14),'История'))
