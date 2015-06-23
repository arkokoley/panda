import wikipedia
user_input = raw_input("")
user_input_predef = user_input[0:14]			#making sure that command is correct, this will be in the main python code
predifined1 = "panda what is "
predifined2 = "Panda what is "
def wikisearch(keywords):
		try:										#ironing out the errors	
			summary = wikipedia.summary(keywords)
		except wikipedia.exceptions.DisambiguationError as disambiguation: #input can mean many things: eg. panda what is mercury
			print("Oops, did you mean one of the following?")
			for i in range(0, len(disambiguation.options)):
				print "%d) " %(i+1) + disambiguation.options[i]
			option_number=input("If no option matches with your keyword, press '0'. Else enter the option number:  ") #gaurav correct this line to end if input is enter not zero
			if(option_number==0):
				exit()
			else:
				print disambiguation.options[option_number-1] + " selected:"
				wikisearch(disambiguation.options[option_number-1])			
				exit()
		except wikipedia.exceptions.PageError as error:
			print "'"+ user_query + "'"+  " does not match any pages. Try another query!"
			exit()
		except wikipedia.exceptions.HTTPTimeoutError as timeout:
			print "Server timeout error, there seems to be some network issue. Please try again later"
			exit()
		except wikipedia.exceptions.WikipediaException as wikiexception:
			print "There seems to be some error. Please try again later"
			exit()
		page = wikipedia.page(keywords)
		page_url = page.url
		print summary
		print("For more information right click and open the following link: " + page_url) 
if((user_input_predef == predifined1) or (user_input_predef== predifined2)): #should be in main python code
	user_query = user_input[14:]				#selecting the keyword
	wikisearch(user_query)						#running search command
else:
	print "Wrong command, please try again, the command should be of the form: 'panda what is <keyword>'"
