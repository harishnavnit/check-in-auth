import os
import json
import requests


class GMapPlaces():
    API_KEY = os.environ.get('GMAP_PLACES_KEY')
    MAP_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    def __init__(self, position):
        self.current_location = position
        if self.API_KEY == "":
            raise Exception("Places API key not found")
        print("API key = ", self.API_KEY)

    def search(self, radius=100, type="", keyword=""):
        location = str(self.current_location['latitude']) + "," +\
            str(self.current_location['longitude'])

        params = {'location': location, 'radius': radius,
                  'type': type, 'keyword': keyword, 'key': self.API_KEY}
        response = requests.get(self.MAP_URL, params)

        print(json.dumps(response.text, indent=4))


if __name__ == "__main__":
    pos = {'latitude': 12.9715987, 'longitude': 77.5945627}
    places = GMapPlaces(pos)
    places.search()
