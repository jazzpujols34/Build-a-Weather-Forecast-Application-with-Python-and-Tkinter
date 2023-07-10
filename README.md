# Weather Forecasting App

This is a simple weather forecasting application built with Python, Tkinter, Gradio, and the OpenWeatherMap and IPBase APIs.

## Features

- Get weather information by entering a city name or IP address.

- Get weather information for your current location.

- Interactive web interface with Gradio.

## Setup

1. Clone this repository.

2. Install the required Python packages with `pip install -r requirements.txt`.

3. Create a `.env` file in the root directory of the project, and add your OpenWeatherMap and IPBase API keys like so:

    ```
    OPEN_WEATHER_MAP_API_KEY=<your_openweathermap_api_key>

    IPBASE_API_KEY=<your_ipbase_api_key>
    ```

4. Run the Tkinter version of the application with `python app_tkinter.py`.

![image](https://github.com/jazzpujols34/Build-a-Weather-Forecast-Application-with-Python-and-Tkinter/assets/62235508/cc792177-3f08-4e99-9361-9063107ff9ae)

5. Run the Gradio version of the application with `python app_gradio.py`.

![image](https://github.com/jazzpujols34/Build-a-Weather-Forecast-Application-with-Python-and-Tkinter/assets/62235508/4a20d07e-ca31-498d-b8f9-46a0d0167288)


## Usage

- To get weather information for a specific city, enter the city name in the text field and click "Get Weather".

- To get weather information for a specific IP address, enter the IP address in the text field and click "Get Weather".

- To get weather information for your current location, click "Use Current Location".

- For the Gradio version, enter a city name or IP address in the web interface and click "Submit".

