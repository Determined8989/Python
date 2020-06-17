import os 
import datetime
while True: 
	a = input('Введите слово:')
	if a.lower() == "exit":
		basedir = "LOG"
		subnames = os.listdir(basedir)
		print(len(subnames))
		sub_size = 0
		for subname in subnames:
			sub_size += os.path.getsize('LOG/'+ subname)		    
		print (sub_size)
		break
	elif a.lower() == "clear":
		os.system('cls||clear')
	else:
		p = datetime.datetime.now()
		f = open('LOG/log_' + p.strftime("%Y%m%d%H%M") + '.txt', 'a') 	
		f.write (p.strftime("%Y-%m-%d-%H.%M.%S") + '-' + a + '\n')
		f.close()