import socket,sys

sock = socket.socket()
sock.connect(('sindikasi.okezone.com', 80))
sock.sendall(
	'GET /index.php/okezone/RSS2.0/ HTTP/1.1\r\n'
	'Host: sindikasi.okezone.com\r\n'
	'Connection: close\r\n'
	'User-Agent: cobasocket\r\n'
	'\r\n'
	)

while True:
	buf = sock.recv(1000)
	if not buf :
		break
	print buf
sock.close()