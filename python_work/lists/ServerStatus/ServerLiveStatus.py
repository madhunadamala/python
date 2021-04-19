import urllib.request
try:
	status = urllib.request.urlopen("http://www.stackoverflow.com").getcode()
except urllib.error.URLError:
	print ("False")
else:
	print (status)