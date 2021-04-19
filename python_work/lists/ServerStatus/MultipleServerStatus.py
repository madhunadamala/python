import  urllib.request

SITES = [
	"http://www.meesters-id.nl",
	"http://www.carolsingers.nl",
	"https://www.stackoverflow.com"	,
]

for site in SITES:
	try:
		print(site)
		status = urllib.request.urlopen("https://www.stackoverflow.com").getcode()
	except urllib.error.URLError:
		print(site)
		print ("False")
	else:
		print (status)

		
		