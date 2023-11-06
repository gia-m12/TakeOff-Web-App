import requests
import json

params = {
    'api_key': '4c934e67-5e04-4d19-953e-eac352d72f50',
    'lat': '40.099941',
    'lng': '-74.97579',
    'distance': '50'
    
}
url = 'https://airlabs.co/api/v9/nearby'
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    airports = data.get('response', {}).get('airports', [])
    for airport in airports:
        if(airport.get("iata_code") != None):
            print("Name:", airport.get("name"))
            print("IATA Code:", airport.get("iata_code"))
            print("ICAO Code:", airport.get("icao_code"))
            print("Latitude:", airport.get("lat"))
            print("Longitude:", airport.get("lng"))
            print("Country Code:", airport.get("country_code"))
            print("Popularity:", airport.get("popularity"))
            print("Distance:", airport.get("distance"))
            print()
else:
    print("API request failed with status code:", response.status_code)