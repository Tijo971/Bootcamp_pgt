# Bootcamp_pgt
import requests
import json
#import os
from datetime import datetime
api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")
complete_api_link ="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
#create variables to store and display data
clymet = {
"temp_city" : ((api_data['main']['temp']) - 273.15),
"weather_desc" : api_data['weather'][0]['description'],
"hmdt" : api_data['main']['humidity'],
"wind_spd" : api_data['wind']['speed'],
"date_time" : datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
}
print ("-------------------------------------------------------------")
print ("Weather Stats for - {} || {}".format(location.upper(),clymet ["date_time"]))
print ("-------------------------------------------------------------")
print ("Current Humidity :",clymet ["hmdt"], '%')
print ("Current temperature is: {:.2f} deg C".format(clymet["temp_city"]))
print ("Current wind speed :",clymet["wind_spd"] ,'kmph')
print ("Current weather desc :",clymet["weather_desc"])
json_obj=json.dumps(clymet,indent=2)
with open("climet.txt","w") as g:
    g.write("Weather Status for :--"+location.upper()+"\n"+json_obj)
