#Пишем программу, которая запрашивает постедовательно: Номер телефона (phone), 
#Текст сообщения (message). После ввода данных выполнять отправку сообщения по указанному номеру.
#После отправки сообщения, сохранять в лог файл "send.log"
# следующие данные: [yyyy.MM.dd hh:mm:ss:msec] [номер телефона] [сообщение]
import requests
import datetime
def SaveLog(s):
	p = datetime.datetime.now()
	f = open('send' + p.strftime("%Y%m%d%H%M%S") + '.json', 'wb') 	
	f.write (s)
	f.close()
number = input('Введите номер телефона:')
text = input('Введите сообщение:')
url = 'https://sms.ru/sms/send?api_id=49982794-1794-DBFA-C3BF-C54C58843793&to=%s&msg=%s&json=1' % (number, text.replace (' ','+'))
print (url)
response = requests.get(url)
SaveLog(response.content)
