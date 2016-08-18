import httplib

connection = httplib.HTTPConnection('detik.feedsportal.com')
connection.request('GET', '/c/33613/f/656082/index.rss')
rawreply = connection.getresponse().read()
print rawreply
