import datetime as dt
import numpy as np
import requests
from decimal import Decimal, ROUND_HALF_UP

URL = "https://api.openweathermap.org/data/2.5/forecast?lat=42.3536&lon=71.0893&appid=MyAPIKey"

CITY = "Boston"

"""convert temperature from kelvin to fahrenheit"""
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

data = requests.get(URL).json()

for i in data['list']:
    current_date = ''
    time = i['dt_txt']
    next_date, hour = time.split(' ')
    if current_date != next_date:
            current_date = next_date
            year, month, day = current_date.split('-')
            date = {'y': year, 'm': month, 'd': day}
            print('\n{m}/{d}/{y}'.format(**date))

    hour = int(hour[:2])
    if hour < 12:
            if hour == 0:
                hour = 12
            meridiem = 'AM'
    else:
        if hour > 12:
            hour -= 12
            meridiem = 'PM'
    print('\n%i:00 %s' % (hour, meridiem))
    temp_kelvin = i['main']['temp']
    temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    feels_like_kelvin = i['main']['feels_like']
    feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
    wind_speed = i['wind']['speed']
    wind_speed_knots = wind_speed * 1.94384
    wind_gust = i['wind']['gust']
    wind_gust_knots = Decimal(str(i['wind']['gust'] * 1.94384)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    wind_gust_knots = wind_gust * 1.94384
    """sunset_time = dt.datetime.utcfromtimestamp(i['city']['sunset'] + i['timezone'])"""

    print(f"Temperature in {CITY}: {temp_fahrenheit}°F")
    print(f"Temperature in {CITY} feels like: {feels_like_fahrenheit}°F")
    print(f"Wind speed in {CITY}: {wind_speed_knots} knots")
    print(f"Wind gust in {CITY}: {wind_gust_knots} knots")
    """print(f"Sun sets in {CITY} at {sunset_time} local time.")"""

