import numbers


def predict_river_level(rain):
    # If rain value is not a number
    if not isinstance(rain, numbers.Number):
        return "Can't Predict"
    # No rain
    if rain == 0.0:
        return 'River level will go down'
    # Slight Rain
    elif 0.0 < rain < 0.5:
        return 'River level will stay the same'
    # Moderate Rain
    elif 0.5 < rain < 4.0:
        return 'River level will go slightly up'
    # Heavy Rain
    elif 4.0 < rain < 8.0:
        return 'River level will go up'
    # Torrential / Very heavy rain
    elif 8.0 < rain:
        return 'River level will go up a lot'
    return 'River level will go down'


def get_river_name(title):
    river_name = title.split(" at ")[0]
    return river_name


# print(get_river_name("Ogmore at Penybont"))
def parse_river_api_response(resp):
    resp_json = resp.json()
    values = {}
    if 'features' in resp_json.keys():
        features = resp_json['features']
        if len(features) > 0:
            first_station_readings = features[0]['properties']
            values = {
                'river_name': get_river_name(first_station_readings['TitleEN']),
                'station_name': first_station_readings['NameEN'],
                'level': first_station_readings['LatestValue'],
                'time': first_station_readings['LatestTime'],
                'station_id': first_station_readings['Location']
            }
    return values


def parse_weather_api_response(resp):
    resp_json = resp.json()
    if resp_json is None:
        return
    prediction_list = resp_json['list']
    rain_predictions = []
    if prediction_list is not None and len(prediction_list) is not 0:
        _3h_rain_predictions = [prediction.get("rain") for prediction in prediction_list]
        for rain_prediction in _3h_rain_predictions:
            if rain_prediction is not None:
                _3h_rain_prediction=rain_prediction.get("3h")
                if _3h_rain_prediction is not None:
                    rain_predictions.append(_3h_rain_prediction)
    rain_prediction = sum(rain_predictions) / len(rain_predictions)
    return rain_prediction
