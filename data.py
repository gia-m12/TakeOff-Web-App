import requests
import json

#first get airports nearby your location
origin_params = {
    'api_key': '4c934e67-5e04-4d19-953e-eac352d72f50',
    'lat': '40.099941',
    'lng': '-74.97579',
    'distance': '50'
}
origin_url = 'https://airlabs.co/api/v9/nearby'
origin_response = requests.get(origin_url, params=origin_params)
origin_airport = []
if origin_response.status_code == 200:
    origin_data = origin_response.json()
    airports = origin_data.get('response', {}).get('airports', [])
    origin_airport = airports[0]
    for airport in airports:
        if(airport.get("iata_code") != None):
            if origin_airport.get("popularity") < airport.get("popularity"):
                origin_airport = airport
else:
    print("API request failed with status code:", origin_response.status_code)
#get destination airports
des_params = {
    'api_key': '4c934e67-5e04-4d19-953e-eac352d72f50',
    'lat': '28.476224089314087',
    'lng': '-81.46854344694752',
    'distance': '50'
}
des_url = 'https://airlabs.co/api/v9/nearby'
des_response = requests.get(des_url, params=des_params)

if des_response.status_code == 200:
    des_airports = []
    des_data = des_response.json()
    airports = des_data.get('response', {}).get('airports', [])
    des_airport = airports[0]
    for airport in airports:
        if(airport.get("iata_code") != None):
            if des_airport.get("popularity") < airport.get("popularity"):
                des_airport = airport
else:
    print("API request failed with status code:", des_response.status_code)


airline_params = {
    'api_key': '4c934e67-5e04-4d19-953e-eac352d72f50',
    'country_code': 'US'
    
}
airlines = {
    'iata_codes': [],
    'icao_codes': []
}
#5 most common airlines used in US
names = ["American Airlines", "Southwest Airlines", "Spirit Airlines", "Delta Air Lines", "United Airlines"]
airline_response = requests.get('https://airlabs.co/api/v9/airlines', params=airline_params)
if airline_response.status_code == 200:
     airline_data = airline_response.json()
     airline_data = airline_data.get('response', {})
     for data in airline_data:
         if data['iata_code'] != None and data['icao_code'] != None and data['name'] in names:
            airlines['iata_codes'].append(data['iata_code'])
            airlines['icao_codes'].append(data['icao_code'])
else:
    print("API request failed with status code:", airline_response.status_code)

flights = {
    'flight_iata': [],
    'flight_icao': []
}
for i in range(len(names)):
    route_params = {
        'api_key': '4c934e67-5e04-4d19-953e-eac352d72f50',
        'dep_iata': origin_airport.get('iata_code'),
        'dep_icao': origin_airport.get('icao_code'),
        'arr_iata': des_airport.get("iata_code"),
        'arr_icao': des_airport.get("icao_code"),
        'airline_icao': airlines['icao_codes'][i],
        'airline_iata': airlines['iata_codes'][i]
    }
    route_response = requests.get('https://airlabs.co/api/v9/routes', params=route_params)
    if route_response.status_code == 200:
        route_data = route_response.json()
        route_data = route_data.get('response', {})
        for data in route_data:
            print("Depature Time: ", data['dep_time'])
            print("Arrival Time: ", data['arr_time'])
            print("Duration: ", data['duration'], " minutes")
            flights['flight_iata'].append(data['flight_iata'])
            flights['flight_icao'].append(data['flight_icao'])

    else:
        print("API request failed with status code:", route_response.status_code)

