from tkinter import *
import tkintermapview
import requests
from bs4 import BeautifulSoup

services=[]
clients=[]
workers=[]

class LocationEntity:
    def get_coordinates(self, location):
        try:
            url = f"https://pl.wikipedia.org/wiki/{location}"
            response = requests.get(url).text
            soup = BeautifulSoup(response, "html.parser")
            longitude = float(soup.select(".longitude")[1].text.replace(",", "."))
            latitude = float(soup.select(".latitude")[1].text.replace(",", "."))
            return [latitude, longitude]
        except:
            print(f"Nie znaleziono współrzędnych dla lokalizacji: {location}")
            return [0.0, 0.0]

class Service(LocationEntity):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.coordinates = self.get_coordinates(location)

class Client(LocationEntity):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.coordinates = self.get_coordinates(location)

class Worker(LocationEntity):
    def __init__(self, name, location, service_name):
        self.name = name
        self.location = location
        self.service_name = service_name
        self.coordinates = self.get_coordinates(location)

root = Tk()
root.geometry("1200x760")
root.title("Projekt pop pf")

ramka_lista = Frame(root)
ramka_formularz = Frame(root)
ramka_mapy = Frame(root)

ramka_lista.grid(row=0, column=0, padx=10)
ramka_formularz.grid(row=0, column=1, padx=10)
ramka_mapy.grid(row=1, column=0, columnspan=2, pady=10)

# ======================================
# Listy
# ======================================
listbox_services = Listbox(ramka_lista, width=40, height=10)
listbox_services.grid(row=1, column=0)
Label(ramka_lista, text="Serwisy rowerowe").grid(row=0, column=0)

listbox_clients = Listbox(ramka_lista, width=40, height=10)
listbox_clients.grid(row=1, column=1)
Label(ramka_lista, text="Klienci").grid(row=0, column=1)

listbox_workers = Listbox(ramka_lista, width=40, height=10)
listbox_workers.grid(row=1, column=2)
Label(ramka_lista, text="Pracownicy").grid(row=0, column=2)

# ======================================
# Formularze
# ======================================
Label(ramka_formularz, text="Dodaj nowy serwis").grid(row=0, column=0, columnspan=2)
entry_service_name = Entry(ramka_formularz)
entry_service_name.grid(row=1, column=1)
Label(ramka_formularz, text="Nazwa serwisu").grid(row=1, column=0)
entry_service_location = Entry(ramka_formularz)
entry_service_location.grid(row=2, column=1)
Label(ramka_formularz, text="Lokalizacja serwisu").grid(row=2, column=0)

def add_service():
    name = entry_service_name.get()
    location = entry_service_location.get()
    s = Service(name, location)
    services.append(s)
    listbox_services.insert(END, f"{s.name} - {s.location}")
    update_map_services()

Button(ramka_formularz, text="Dodaj serwis", command=add_service).grid(row=3, column=0, columnspan=2, pady=5)

Label(ramka_formularz, text="Dodaj klienta").grid(row=4, column=0, columnspan=2)
entry_client_name = Entry(ramka_formularz)
entry_client_name.grid(row=5, column=1)
Label(ramka_formularz, text="Imię i nazwisko").grid(row=5, column=0)
entry_client_location = Entry(ramka_formularz)
entry_client_location.grid(row=6, column=1)
Label(ramka_formularz, text="Lokalizacja klienta").grid(row=6, column=0)

def add_client():
    name = entry_client_name.get()
    location = entry_client_location.get()
    c = Client(name, location)
    clients.append(c)
    listbox_clients.insert(END, f"{c.name} - {c.location}")
    update_map_clients()

Button(ramka_formularz, text="Dodaj klienta", command=add_client).grid(row=7, column=0, columnspan=2, pady=5)

Label(ramka_formularz, text="Dodaj pracownika").grid(row=8, column=0, columnspan=2)
entry_worker_name = Entry(ramka_formularz)
entry_worker_name.grid(row=9, column=1)
Label(ramka_formularz, text="Imię i nazwisko").grid(row=9, column=0)
entry_worker_location = Entry(ramka_formularz)
entry_worker_location.grid(row=10, column=1)
Label(ramka_formularz, text="Lokalizacja").grid(row=10, column=0)
entry_worker_service = Entry(ramka_formularz)
entry_worker_service.grid(row=11, column=1)
Label(ramka_formularz, text="Serwis przypisany").grid(row=11, column=0)

def add_worker():
    name = entry_worker_name.get()
    location = entry_worker_location.get()
    service_name = entry_worker_service.get()
    w = Worker(name, location, service_name)
    workers.append(w)
    listbox_workers.insert(END, f"{w.name} - {w.location} [{w.service_name}]")
    update_map_workers()

Button(ramka_formularz, text="Dodaj pracownika", command=add_worker).grid(row=12, column=0, columnspan=2, pady=5)

# ======================================
# Mapa
# ======================================
map_widget = tkintermapview.TkinterMapView(ramka_mapy, width=1300, height=400, corner_radius=0)
map_widget.grid(row=0, column=0)
map_widget.set_position(52.23, 21.01)
map_widget.set_zoom(6)

service_markers = []
client_markers = []
worker_markers = []

def update_map_services():
    global service_markers
    for m in service_markers:
        m.delete()
    service_markers = [map_widget.set_marker(s.coordinates[0], s.coordinates[1], text=s.name) for s in services]

def update_map_clients():
    global client_markers
    for m in client_markers:
        m.delete()
    client_markers = [map_widget.set_marker(c.coordinates[0], c.coordinates[1], text=c.name) for c in clients]

def update_map_workers():
    global worker_markers
    for m in worker_markers:
        m.delete()
    worker_markers = [map_widget.set_marker(w.coordinates[0], w.coordinates[1], text=w.name) for w in workers]



root.mainloop()