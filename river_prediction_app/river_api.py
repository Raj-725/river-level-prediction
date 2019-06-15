import numbers
import time


def print_date_time():
    print(time.strftime(" Running: %A, %d. %B %Y %I:%M:%S %p"))


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


def get_river_data():
    print(time.strftime(" River Running: %A, %d. %B %Y %I:%M:%S %p"))
    return ''


def get_weather_data():
    print(time.strftime(" Weather Running: %A, %d. %B %Y %I:%M:%S %p"))
    return ''

# print(predict_river_level(1))
