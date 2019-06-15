import requests

# worldtradingdata.com Historical API url
api_url = "http://api.openweathermap.org/data/2.5/forecast"

# Parameters to send with API call
params = {'q': 'cardiff,gb'}


# Method to set api token
def set_api_token(token):
    params['appid'] = token


# This method fetch the data from API, perform calculations and returns the response
def get_performance(ticker, start_date=None, end_date=None, api_token=None):
    # Set request params
    req_params = params
    req_params['symbol'] = ticker
    req_params['date_from'] = start_date
    req_params['date_to'] = end_date

    # Update API token
    if api_token is not None:
        req_params['api_token'] = api_token
        params['api_token'] = api_token

    # check if api token set and show message
    if 'api_token' not in req_params or req_params['api_token'] is None:
        print("api_token is not set! \nPlease set api token using: "
              "newco_api.set_api_token(YOUR_API_TOKEN) OR pass in a parameter api_token=YOUR_API_TOKEN")
        return

    try:
        resp = requests.get(api_url, params=req_params)
    except Exception as e:
        print(e)
        return

    status_code = resp.status_code
    if status_code != 200:
        # This means something went wrong.
        print("Error fetching data: {}", status_code)
        return

    resp_json = resp.json()

    if 'message' in resp_json.keys() or 'Message' in resp_json.keys():
        print('Error fetching data: {}'.format(resp_json))
        return

    # response = get_calculations(resp_json)
    # return response


token = '08d58edcc444bcf250de23962ccc12ec'
set_api_token(token)

resp = {}
try:
    resp = requests.get(api_url, params=params)
except Exception as e:
    print(e)

resp_json = resp.json()
print(resp_json)

if 'features' in resp_json.keys():
    features = resp_json['features']
    if len(features) > 1:
        first_station_readings = features[0]['properties']
        values = {
            'Station Name': first_station_readings['NameEN'],
            'Latest Value': first_station_readings['LatestValue'],
            'Latest Reading Time': first_station_readings['LatestTime'],
            'Units': first_station_readings['Units']
        }
        print('values : {}'.format(first_station_readings))

print(values)
