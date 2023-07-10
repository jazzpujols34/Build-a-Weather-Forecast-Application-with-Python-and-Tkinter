import requests
import re
import os
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

OPEN_WEATHER_MAP_API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')
OPEN_WEATHER_MAP_API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'

IPBASE_API_KEY = os.getenv('IPBASE_API_KEY')
IPBASE_API_ENDPOINT = "https://api.ipbase.com/v2/info"

IP_ADDRESS_REGEX = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

def get_weather(input_value):
    if IP_ADDRESS_REGEX.match(input_value):
        ipbase_query_params = {
            "apiKey": IPBASE_API_KEY,
            "ip": input_value
        }
        response = requests.get(IPBASE_API_ENDPOINT, params=ipbase_query_params)
        city_name = response.json()["data"]["location"]["city"]["name"]
    else:
        city_name = input_value

    weather_query_params = {
        'q': city_name,
        'appid': OPEN_WEATHER_MAP_API_KEY,
        'units': 'metric'
    }
    response = requests.get(OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
    weather_data = response.json()

    if response.status_code == 200:
        return f"{weather_data['name']}: {weather_data['main']['temp']}°C"
    else:
        return f"Error: {response.status_code} - {response.text}"

iface = gr.Interface(fn=get_weather, inputs="text", outputs="text")
iface.launch()
