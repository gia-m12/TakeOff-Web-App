import json
import geocoder
import requests
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes or specify origins with CORS(app, origins="*") for all origins


# first get airports nearby your location
def origin(lat, lng):
    origin_params = {
        'api_key': '4c934e67-5e04-4d19-953e-eac352d72f50',
        'lat': lat,
        'lng': lng,
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
            if (airport.get("iata_code") != None):
                if origin_airport.get("popularity") < airport.get("popularity"):
                    origin_airport = airport
    else:
        print("API request failed with status code:", origin_response.status_code)
    return origin_airport


# get destination airports
def des(lat, lng):
    des_params = {
        'api_key': '4c934e67-5e04-4d19-953e-eac352d72f50',
        'lat': lat,
        'lng': lng,
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
            if (airport.get("iata_code") != None):
                if des_airport.get("popularity") < airport.get("popularity"):
                    des_airport = airport
    else:
        print("API request failed with status code:", des_response.status_code)
    return des_airport


airline_params = {
    'api_key': '4c934e67-5e04-4d19-953e-eac352d72f50',
    'country_code': 'US'

}


def get_airlines():
    airlines = {
         # 5 most common airlines used in US
        'names': ["American Airlines", "Southwest Airlines", "Spirit Airlines", "Delta Air Lines", "United Airlines"],
        'iata_codes': [],
        'icao_codes': []
    }
   
    airline_response = requests.get('https://airlabs.co/api/v9/airlines', params=airline_params)
    if airline_response.status_code == 200:
        airline_data = airline_response.json()
        airline_data = airline_data.get('response', {})
        for data in airline_data:
            if data['iata_code'] != None and data['icao_code'] != None and data['name'] in airlines['names']:
                airlines['iata_codes'].append(data['iata_code'])
                airlines['icao_codes'].append(data['icao_code'])
    else:
        print("API request failed with status code:", airline_response.status_code)
    return airlines


def get_routes(origin_airport, des_airport, airlines):
    for i in range(5):
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
        times = {}
        if route_response.status_code == 200:
            route_data = route_response.json()
            route_data = route_data.get('response', {})
            if route_data:
                shortest = route_data[0]['duration']
                day = ""
            for data in route_data:
                if data['duration'] < shortest:
                    shortest = data['duration']
                    day = data['days'][0]
        else:
            print("API request failed with status code:", route_response.status_code)
        times[airlines['names'][i]] = [day, shortest]
    return times
    
@app.route('/get_coordinates', methods=['POST'])
def get_coordinates():
    data = request.get_json()
    lat = data['lat']
    lng = data['lng']
    origin_airport = origin(lat, lng)
    location = geocoder.osm(data['address'])
    lat, long = location.lat, location.lng
    des_airport = des(lat, long)
    airlines = get_airlines()
    info = get_routes(origin_airport, des_airport, airlines)
    print(info)
    return jsonify({
        'origin_airport': origin_airport,
        'des_airport': des_airport,
        'aa': info.get('American Airlines', {}),
        'sw': info.get('Southwest Airlines', {}),
        'sp': info.get('Spirit Airlines', {}),
        'da': info.get('Delta Air Lines', {}),
        'ua': info.get('United Airlines', {}),
        'message': 'Data processed'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5001)
