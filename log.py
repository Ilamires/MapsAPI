import sys
from io import BytesIO
import requests
from PIL import Image
import PyQt5


class Map:

    def __init__(self):
        self.delta = "0.005"
        self.toponym_longitude = ""
        self.toponym_lattitude = ""

    def cord(self, longitude, lattitude):
        self.toponym_lattitude = str(float(self.toponym_lattitude) + float(lattitude))
        self.toponym_longitude = str(float(self.toponym_longitude) + float(longitude))

    def toponim(self, name):
        toponym_to_find = name
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": toponym_to_find,
            "format": "json"}
        response = requests.get(geocoder_api_server, params=geocoder_params)
        if not response:
            # обработка ошибочной ситуации
            pass
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        self.toponym_longitude, self.toponym_lattitude = toponym_coodrinates.split(" ")

    def maping(self, delta,view):
        self.delta = str(delta)

        map_params = {
            "ll": ",".join([self.toponym_longitude, self.toponym_lattitude]),
            "spn": ",".join([self.delta, self.delta]),
            "l": view
        }

        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=map_params)
        name = 'image.png'
        Image.open(BytesIO(response.content)).save(name)
        return name
