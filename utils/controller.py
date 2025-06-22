
import requests
from bs4 import BeautifulSoup
def get_coordinates_nominatim(address: str) -> tuple:
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "TwojaAplikacja/1.0 (kontakt@twojadomena.pl)"  # wymagany nagłówek!
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if data:
        lat = float(data[0]['lat'])
        lon = float(data[0]['lon'])
        return lat, lon
    else:
        print(f"Nie znaleziono współrzędnych dla: {address}")
        return None, None

class Services:
    def __init__(self, service_name, service_location, coordinates=None):
        self.service_name = service_name
        self.service_location = service_location
        self.coordinates = coordinates if coordinates else self.get_coordinates()


    def get_coordinates(self) -> list:
        full_address = f"{self.service_name}, {self.service_location}"
        lat, lon = get_coordinates_nominatim(full_address)
        return [lat, lon] if lat is not None else [0.0, 0.0]


class Client:
    def __init__(self,client_name,client_service,client_location1,):
        self.client_name =client_name
        self.client_service=client_service
        self.client_location1=client_location1
        self.coordinates=self.get_coordinates()


    def get_coordinates(self) -> list:
        url = f"https://pl.wikipedia.org/wiki/{self.client_location1}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        return [latitude, longitude]


class Worker:
    def __init__(self,worker_name,worker_service,worker_location):
        self.worker_name =worker_name
        self.worker_service=worker_service
        self.worker_location=worker_location
        self.coordinates=self.get_coordinates()


    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.worker_location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        return [latitude, longitude]