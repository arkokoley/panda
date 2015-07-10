from bs4 import BeautifulSoup
import requests
i=raw_input("Enter Word: ")

try:
	def dictionary(i):
		r=requests.get('http://www.dictionaryapi.com/api/v1/references/collegiate/xml/' + str(i) + '?key=c3855e7f-ce94-443b-89e2-50b1e4b062e8')
		soup=BeautifulSoup(r.text,'lxml')
		print 'Pronunciation: ' + soup.body.hw.string
		print 'Meaning',
		for d in soup.body.find_all('dt'):
			for string in d.strings:
				print string,
			print " "
	dictionary(i)

except Exception:
	print 'Word not found'
	
