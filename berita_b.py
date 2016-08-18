import socket,sys

sock = socket.socket()
sock.connect(('detik.feedsportal.com', 80))
sock.sendall(
	'GET /c/33613/f/656082/index.rss HTTP/1.1\r\n'
	'Host: detik.feedsportal.com\r\n'
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