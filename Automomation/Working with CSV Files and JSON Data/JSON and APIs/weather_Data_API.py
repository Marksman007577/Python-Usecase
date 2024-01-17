#! python3
import json, requests, sys

# Step 1: Get Location from the Command Line Argument
# In Python, command line arguments are stored in the sys.argv list.
# The APPID variable should be set to the API key for your account.
# Without this key, your requests to the weather service will fail
APPID = 'YOUR_APPID_HERE'


# Recall that sys.argv will always
# have at least one element, sys.argv[0], which contains the Python script’s
# filename.) If there is only one element in the list, then the user didn’t
# provide a location on the command line, and a “usage” message will be
# provided to the user before the program ends.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Step 2: Download the JSON Data
url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location,APPID)

response = requests.get(url)
response.raise_for_status()

# Step 3: Load JSON Data and Print Weather
weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])