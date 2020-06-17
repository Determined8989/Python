import os 
import datetime
def SaveLog(s):
	p = datetime.datetime.now()
	f = open('LOG/log_' + p.strftime("%Y%m%d%H%M") + '.txt', 'a') 	
	f.write (p.strftime("%Y-%m-%d-%H.%M.%S") + '-' + s + '\n')
	f.close()	
def printInfo():
	basedir = "LOG"
	subnames = os.listdir(basedir)
	print(len(subnames))
	sub_size = 0
	for subname in subnames:
		sub_size += os.path.getsize('LOG/'+ subname)		    
	print (sub_size)
def cls():
	os.system('cls||clear')
def main():
	SaveLog("Пользователь начал работу")
	while True: 
		a = input('Введите слово:')
		if a.lower() == "exit":
			printInfo()
			SaveLog('Пользователь завершил работу')
			break
		elif a.lower() == "clear":
			cls()
			SaveLog ('Пользователь очистил экран')
		else:
			SaveLog ('Пользователь ввел неизвестную команду: ' + a)
main()