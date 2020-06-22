#1.Убираем префикс
#2.Разбиваем на составляющие через разделитель
#3.Для каждого из элементов списка создаем каталог, проверяя при этом наличие
#https://docs.python.org/3/library/urllib.parse.html
import os
from urllib.parse import urlparse
url = input ("Введите URL:")
url = url.replace('https://', '')
url = url.replace('www.', '')
url = url.replace('http://','')
folderslist = url.split('/')
path  = ''
for foldername in folderslist:
	path += (foldername + '/')
	if not os.path.exists(path):
		os.mkdir(path)
	print(path)
