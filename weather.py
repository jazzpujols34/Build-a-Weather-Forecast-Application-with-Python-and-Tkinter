import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

api_key =  os.getenv('OPEN_WEATHER_MAP_API_KEY')
city_name = input('Enter a city name: ')

api_endpoint = 'https://api.openweathermap.org/data/2.5/weather'
query_params = {'q': city_name, 'appid': api_key, 'units': 'metric'}

response = requests.get(api_endpoint, params=query_params)

if response.status_code == 200:
    data = response.json()
    # Handle response data
    print(data)
    # temperature = data['main']['temp']
    # print(temperature)
else:
    # Handle errors
    print(f'Error: {response.status_code} - {response.text}')