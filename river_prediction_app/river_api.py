import requests

from . import utilities

RIVER_API_TOKEN = '63503e5e31344898b7726a0773a1fa6e'
WEATHER_API_TOKEN = '08d58edcc444bcf250de23962ccc12ec'


def get_river_data():
    # naturalresources.wales River Levels API URL
    api_url = "https://api.naturalresources.wales/riverlevels/v1/distance/{distance}/latlon/{lat}/{long}"

    # Parameters to send with API call
    url_params = {'distance': 3000, 'lat': 51.48, 'long': -3.18}
    api_url = api_url.format(**url_params)
    headers = {'Ocp-Apim-Subscription-Key': RIVER_API_TOKEN}
    resp = {}
    try:
        resp = requests.get(api_url, headers=headers)
    except Exception as e:
        print(e)

    status_code = resp.status_code
    if status_code != 200:
        # This means something went wrong.
        print("Error fetching data: {}", status_code)
        return
    river_level = utilities.parse_river_api_response(resp)

    return river_level


def get_rain_prediction():
    # worldtradingdata.com Historical API url
    api_url = "http://api.openweathermap.org/data/2.5/forecast"

    # Parameters to send with API call
    params = {'q': 'cardiff,gb'}
    params['appid'] = WEATHER_API_TOKEN

    resp = {}
    try:
        resp = requests.get(api_url, params=params)
    except Exception as e:
        print(e)

    status_code = resp.status_code
    if status_code != 200:
        # This means something went wrong.
        print("Error fetching data: {}", status_code)
        return
    rain_prediction = utilities.parse_weather_api_response(resp)
    return rain_prediction


def get_river_level():
    river_level = get_river_data()
    rain_prediction = get_rain_prediction()
    river_level_prediction = utilities.predict_river_level(rain_prediction)
    river_level['avg_rain'] = rain_prediction
    river_level['prediction'] = river_level_prediction
    return river_level


def print_date_time():
    pass
