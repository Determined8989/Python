#Доработать приложение 
#После ввода url программа должна выполнить запрос к web серверу и получить текст url страницы.
#При получении текста страницы сохранить его в файл "source.html" внутри каталога созданного по алгоритму предыдущего задания.
#https://docs.python.org/3/library/urllib.parse.html
import os
import requests
from urllib.parse import urlparse
url = input ("Введите URL:")
response = requests.get(url)
#print(response.content.decode('utf-8'))
url = url.replace('https://', '')
url = url.replace('www.', '')
url = url.replace('http://','')
folderslist = url.split('/')
path  = ''
for foldername in folderslist:
	path += (foldername + '/')
	if not os.path.exists(path):
		os.mkdir(path)
sourcef = open(path + 'source.html','wb')
sourcef.write (response.content)
