import httplib

connection = httplib.HTTPConnection('sindikasi.okezone.com')
connection.request('GET', '/index.php/okezone/RSS2.0/')
rawreply = connection.getresponse().read()
print rawreply