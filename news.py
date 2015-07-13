import feedparser
url="http://www.thehindu.com/"			

def createurl(url, choice):
	if (choice>9 or choice<1):
		print "Thank you for using the news app."
		exit()
	elif choice==1:
		print "Displaying latest news: "
		url=url+"news/"
	elif choice==2:
		print "Displaying latest international news."
		url=url+"news/international/"
	elif choice==3:
		print "Displaying latest national news."
		url=url+"news/national/"
	elif choice==4:
		print "Displaying latest business news."
		url=url+"business/"
	elif choice==5:
		print "Displaying latest sports news."
		url=url+"sport/"
	elif choice==6:
		url=url+"news/cities/"
	elif choice==7:
		print "Displaying latest science and technology news."
		url=url+"sci-tech/"
	elif choice==8:
		print "Displaying latest entertainment news."
		url=url+"entertainment/"
	elif choice==9:
		print "Displaying latest cricket news."
		url=url+"sport/cricket/"
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


print "Choose one of the following:\n1)General News\n2)International\n3)National\n4)Business\n6)City\n7)sci-tech\n8)Entertainment\n9)Cricket\n0)To exit"
choice=input("Enter choice: ")
url=createurl(url, choice)
print url
parsefornews(url)
