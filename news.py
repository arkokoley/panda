import feedparser
url="http://www.thehindu.com/"
def parsefornews(url):
	url=url+"news/?service=rss"
	numberofnews=0
	feed=feedparser.parse(url)
	for item in feed["items"]:
		if numberofnews<10:
			numberofnews+=1
			print str(numberofnews)+") "+item["title"]
			print item["description"]
			print "For more information right click and open: "+item["link"]+"\n"
			
		
def parseforinternational(url):
	url=url+"news/international/?service=rss"
	numberofnews=0
	feed=feedparser.parse(url)
	for item in feed["items"]:
		if numberofnews<10:
			numberofnews+=1
			print str(numberofnews)+") "+item["title"]
			print item["description"]
			print "For more information right click and open: "+item["link"]+"\n"

def createurl(url, choice):
	if choice==1:
		url=url+"news/"
	elif choice==2:
		url=url+"international/"
	elif choice==3:
		url=url+"national/"
	elif choice==4:
		url=url+"business/"
	elif choice==5:
		url=url+"sports/"
	elif choice==6:
		url=url+"news/cities/"
	elif choice==7:
		url=url+"sci-tech/"
	elif choice==8:
		url=url+"entertainment/"
	elif choice==9:
		url=url+"sport/cricket/"
	elif choice==10:
		url=url+"sport/football/"
	url+="?service=rss"
	return url

def parsefornews(url):
	numberofnews=0
	feed=feedparser.parse(url)
	for item in feed["items"]:
		if numberofnews<10:
			numberofnews+=1
			print str(numberofnews)+") "+item["title"]
			print item["description"]
			print "For more information right click and open: "+item["link"]+"\n"
print "Choose one of the following:\n1)General News\n2)International\n3)National\n4)Business\n6)City\n7)sci-tech\n8)Entertainment"
choice=input("Enter choice: ")
url=createurl(url, choice)
print url
parsefornews(url)
