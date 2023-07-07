import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

api_key =  os.getenv('ipbase_API_KEY')
ip_address = "1.1.1.1" #os.getenv('ipbase_API_Address') # Optional

api_endpoint = 'https://api.ipbase.com/v2/info'
query_params = {'apiKey': api_key}

if ip_address:
    query_params['ip'] = ip_address

response = requests.get(api_endpoint, params=query_params)
# Use the .json() method to get the JSON response
json_response = response.json()

# if response.status_code == 200:
#     data = response.json()
#     # Assuming 'response' is your JSON response

#     # Use json.dumps with indent parameter to format the JSON
#     pretty_response = json.dumps(json_response, indent=4)

#     print(pretty_response)
#     # Handle response data
# else:
#     # Handle errors
#     print(f'Error: {response.status_code} - {response.text}')
    


if response.status_code == 200:
    data = response.json()
    # Handle response data
    try:
        location_data = data['data']['location']
        city_name = location_data['city']['name']
        print(city_name)
    except KeyError as e:
        print(f'Error: {e}')
else:
    # Handle errors
    print(f'Error: {response.status_code} - {response.text}')