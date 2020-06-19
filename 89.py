from datetime import timedelta
from datetime import datetime
from datetime import date
from datetime import time
import os
today = date.today()
t = datetime.now()
w = date(today.year,1,1)
n = date(today.year,12,31)
def cls():
	os.system('cls||clear')
while True:
	a = input('Введите слово:')
	if a.lower() == "clear":
		cls()
	elif a.lower() == "exit":
		print ('Пользователь завершил работу')
		break
	elif a.lower() == 'date':
		print (t)
	elif a.lower() == 'week':
		if w < today:
			print ('С начала года прошло ' , int((today - w).days)//7  , ' недель')
	elif a.lower() == 'ny':
		if today < n:
			print ('До нового года оосталось' , int((n - today).days)+ 1 , 'дней')

