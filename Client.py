import socket

text = input('Введите информацию:')
sock = socket.socket()
sock.connect(('localhost', 222))
sock.send(text.encode('utf-8'))

#sock.send(text)
data = sock.recv(1024)
sock.close()

print (data.decode('utf-8'))