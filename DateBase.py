'''
Используя библиотеку sqlite3 создать базу данных ediary
В базе данных завести таблицу person с полями:
FirstName, LastName, MiddleName, Sex, DateOfBirth,
Phone, Address, Document, 
ключевым является поле Id числового типа, автоинкрементируемое
'''

import sqlite3

db = sqlite3.connect('ediary.db')
sql = db.cursor()

sql.execute('DROP table if exists person')

sql.execute('''CREATE TABLE IF NOT EXISTS person (
	_id INTEGER PRIMARY KEY AUTOINCREMENT,
	Firstname TEXT,
	Lastname TEXT,
	Middlename TEXT,
	sex TEXT,
	DateOFBirth INT,
	phone INT,
	Adress TEXT,
	Document TEXT )''')



Firstname = input('Firstname: ')
Lastname = input('Lastname: ') 
Middlename = input('Middlename: ')
sex = input('Sex: ')
DateOFBirth = input('DateOFBirth: ')
phone = input('Phone: ')
Adress = input('Adress: ')
Document = input('Document: ')

db.commit()

entity = (Firstname, Lastname, Middlename , sex, 490579200, phone, Adress,Document)


sql.execute('INSERT INTO person(Firstname,Lastname,Middlename,sex,DateOFBirth,phone,Adress,Document) VALUES (?,?,?,?,?,?,?,?)', entity)
db.commit()
sql.execute('INSERT INTO person(Firstname,Lastname,Middlename,sex,DateOFBirth,phone,Adress,Document) VALUES (?,?,?,?,?,?,?,?)', entity)
db.commit()
for value in sql.execute("SELECT * FROM person"):
	print(value)
db.close()

