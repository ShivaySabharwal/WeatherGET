import requests
from datetime import datetime

api_key = 'db57d20ea002802159993b7dd067a046'
location = input("Enter the city name: ")

full_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    location+"&appid="+api_key
api_link = requests.get(full_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

fh = open('get_api.txt', 'w')

fh.write('-------------------------------------------------------------')
fh.write('Weather Stats for - {}  || {}'.format(location.upper(), date_time))
fh.write('-------------------------------------------------------------')

fh.write('Current temperature is: {:.2f} deg C'.format(temp_city))
fh.write('Current weather desc  : {}'.format(weather_desc))
fh.write('Current Humidity      : {}'.format(hmdt))
fh.write('Current wind speed    : {}'.format(wind_spd))

fh.close()
