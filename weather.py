import requests
from json import load, dumps
api_key="3bc41d6d4311aebfda7147242d5cf39f"
#location_id="524901"
location_id=0
city_name=""
base_url="http://api.openweathermap.org/data/2.5/forecast/city?"
base_url_for_avg="http://api.openweathermap.org/data/2.5/forecast/daily?"
base_url_for_current = "http://api.openweathermap.org/data/2.5/weather?"
city_name=raw_input("Enter your city name: ")
def create_url(url, api_key, location_id, city_name):     #Function to create the url call
	if(location_id!=0):
		url=url+"id="+location_id+"&"
	if(city_name!=""):
		url=url+"q="+city_name+"&"
	if((location_id==0)and(city_name=="")):
		print "Something Wrong with your input."
		exit()
	url=url+"APPID="+api_key
	url=url+"&units=metric"
	return url


def detailed_json_parsing_today(json_obj):				#Gives weather for every 3 hrs today will be useful for giving weather when time is given
	todays_date=json_obj['list'][0]['dt_txt'][0:11]
	print "Todays detailed weather at "+json_obj['city']['name']+": "
	min_temp=1000
	max_temp=-1000
	for each_day in json_obj['list']:
		if(each_day['dt_txt'][0:11]==todays_date):
			time=each_day['dt_txt'][11:19]
			print "Time: "+ str(time) +": "+ "Weather condition: "+str(each_day['weather'][0]['main'])
			print "                "+"Temperature: "+str(each_day['main']['temp'])+ " degree C"
			print "                "+"Humidity: "+ str(each_day['main']['humidity'])+"%"
			if(each_day['main']['temp_max']>max_temp):
				max_temp=each_day['main']['temp_max']
			if(each_day['main']['temp_min']<min_temp):
				min_temp=each_day['main']['temp_min']

def find_nearest_time(time):    #Get time nearest to asked time that is divisible by 3
	new_time=time[0:2]
	final_time=int(new_time)
	diff=final_time%3
	if(diff==0):
		if(new_time!="24"):
			return str(new_time)+":00:00"
		else:
			return "00:00:00"
	elif(diff==1):
		final_time=final_time-1
		if(final_time<10):
			return "0"+str(final_time)+":00:00"
		else:
			return str(final_time)+":00:00"
	elif(diff==2):
		final_time=final_time+1
		if(final_time<10):
			return "0"+str(final_time)+":00:00"
		else:
			if(str(final_time)!="24"):
				return str(final_time)+":00:00"
			else:
				return "00:00:00"

def json_parsing_today_time(json_obj, time):        #parse to give output at nearest time
	new_time=find_nearest_time(time)
	todays_date=json_obj['list'][0]['dt_txt'][0:11]
	for each_day in json_obj['list']:
		if(new_time!="00:00:00"):
			recent_time=each_day['dt_txt'][11:19]
			if(recent_time==new_time):
				print "Weather conditions at "+time+" are expected to be "+str(each_day['weather'][0]['main'])
				print "Temperature at "+time+" is expected to be "+ str(each_day['main']['temp'])
				print "Humidity at "+time+" is expected to be "+str(each_day['main']['humidity'])+"%"
				exit()	
	
def json_parsing_current(current_json_obj):  
	print "Current weather conditions at "+current_json_obj['name']+": "+current_json_obj['weather'][0]['description']
	print "Current Temperature is: "+str(current_json_obj['main']['temp'])+" degree C"
	print "Current humidity is: "+str(current_json_obj['main']['humidity'])+"%"
	
def json_parsing_today(avg_json_obj):		#Gives average weather today
	print "Weather condition today at "+avg_json_obj['city']['name'] +" is expected to be: "+ avg_json_obj['list'][0]['weather'][0]['description']
	print "Max temperature today is expected to be: "+str(avg_json_obj['list'][0]['temp']['max'])+" degree C"
	print "Min temperature today is expected to be: "+str(avg_json_obj['list'][0]['temp']['min'])+" degree C"
	print "Average humidity is expected to be "+str(avg_json_obj['list'][0]['humidity'])+"% today."
	
def json_parsing_tomorrow(avg_json_obj):
	print "Weather condition tomorrow at "+avg_json_obj['city']['name']+" is expected to be: "+ avg_json_obj['list'][1]['weather'][0]['description']
	print "Max temperature tomorrow is expected to be: "+str(avg_json_obj['list'][1]['temp']['max'])+" degree C"
	print "Min temperature tomorrow is expected to be: "+str(avg_json_obj['list'][1]['temp']['min'])+" degree C"
	print "Average humidity is expected to be "+str(avg_json_obj['list'][1]['humidity'])+"% tomorrow."
				
def json_parsing_dayaftertomorrow(json_obj):
	print "Weather condition day-after-tomorrow at "+avg_json_obj['city']['name']+" is expected to be: "+ avg_json_obj['list'][2]['weather'][0]['description']
	print "Max temperature day-after-tomorrow is expected to be: "+str(avg_json_obj['list'][2]['temp']['max'])+" degree C"
	print "Min temperature day-after-tomorrow is expected to be: "+str(avg_json_obj['list'][2]['temp']['min'])+" degree C"
	print "Average humidity is expected to be "+str(avg_json_obj['list'][2]['humidity'])+"% day-after-tomorrow."
			
#url=create_url(base_url, api_key, location_id,city_name)
#url_for_average = create_url(base_url_for_avg, api_key, location_id,city_name)+"&cnt=7"
#url_for_current=create_url(base_url_for_current, api_key, location_id,city_name)
#print url
#print url_for_current
#response=requests.get(url)
#response_for_average= requests.get(url_for_average)
#response_for_current= requests.get(url_for_current)
#json_obj=response.json()
#avg_json_obj=response_for_average.json()
#current_json_obj=response_for_current.json()
#json_parsing_current(current_json_obj)
#print dumps(current_json_obj, indent=4)
#print dumps(avg_json_obj, indent=4)
#print dumps(json_obj, indent=4)
#detailed_json_parsing_today(json_obj)				#when you need a detailed weather report for today
#json_parsing_today(avg_json_obj)					#when you need average data for today
#json_parsing_tomorrow(avg_json_obj) 				#when you need average data for tomorrow
#json_parsing_dayaftertomorrow(avg_json_obj)		#when you need average data for dayaftertomorrow
#json_parsing_today_time(json_obj, "03:00")
#print find_nearest_time("23:30")
print "Choose one of the following options: "
print "1)Give current weather.\n2)Give average weather data for today.\n3)Give tomorrows weather\n4)Give Day-after-tomorrows weather\n5)Give weather at time: HH:MM"
choice=input("Enter your choice: ")
if(choice==1):
	url_for_current=create_url(base_url_for_current, api_key, location_id,city_name)
	response_for_current= requests.get(url_for_current)
	current_json_obj=response_for_current.json()
	json_parsing_current(current_json_obj)
elif(choice==2):
	url_for_average = create_url(base_url_for_avg, api_key, location_id,city_name)+"&cnt=7"
	response_for_average= requests.get(url_for_average)
	avg_json_obj=response_for_average.json()
	json_parsing_today(avg_json_obj)
elif(choice==3):
	url_for_average = create_url(base_url_for_avg, api_key, location_id,city_name)+"&cnt=7"
	response_for_average= requests.get(url_for_average)
	avg_json_obj=response_for_average.json()
	json_parsing_tomorrow(avg_json_obj) 
elif(choice==4):
	url_for_average = create_url(base_url_for_avg, api_key, location_id,city_name)+"&cnt=7"
	response_for_average= requests.get(url_for_average)
	avg_json_obj=response_for_average.json()
	json_parsing_dayaftertomorrow(avg_json_obj)
elif(choice==5):
	time=raw_input("Enter time HH:MM\n")
	url=create_url(base_url, api_key, location_id,city_name)
	response=requests.get(url)
	json_obj=response.json()
	json_parsing_today_time(json_obj, time)
	

