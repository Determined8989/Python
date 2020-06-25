#Написать приложение прослушивающее порт указываемый при запуске приложения.
#В процессе прослушивания порта - сохранять все данные пришедшие на него в файл log.txt, добавляя строку формата:
#yyyy.MM.dd hh:mm:ss:msec - [полученный текст]
import socket
import datetime
time = datetime.datetime.now()
port = input('Введите порт:')
port = int(port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
	data = conn.recv(1024)
	if not data:
		break
	conn.send(data.upper())
	sourcef = open('log.txt','a')
	sourcef.write (time.strftime("%Y.%m.%d %H:%M:%S:%f")[:-4] + '-' + data.decode('utf-8') + '\n')
conn.close()