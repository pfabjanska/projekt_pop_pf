
from tkinter import *
from tkinter.ttk import*
import tkintermapview

import requests
from bs4 import BeautifulSoup

from utils import model

tryb_edycji = None  # "serwis", "klient", "pracownik"
wybrany_indeks = None


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
    def __init__(self, service_name, service_location, coordinates=None ):
        self.service_name = service_name
        self.service_location = service_location
        self.coordinates = coordinates if coordinates else self.get_coordinates()


    def get_coordinates(self) -> list:
        full_address = f"{self.service_name}, {self.service_location}"
        latitude, longitude = get_coordinates_nominatim(full_address)
        print(latitude, longitude)
        return [latitude, longitude] if latitude is not None else [0.0, 0.0]


class Client:
    def __init__(self,client_name,client_service,client_location1,):
        self.client_name =client_name
        self.client_service=client_service
        self.client_location1=client_location1
        self.coordinates=self.get_coordinates()


    def get_coordinates(self) -> list:
        try:
            url = f"https://pl.wikipedia.org/wiki/{self.client_location1}"
            response = requests.get(url).text
            response_html = BeautifulSoup(response, "html.parser")
            longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
            latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
            print(latitude, longitude)
            return [latitude, longitude]
        except Exception:
            return None




class Worker:
    def __init__(self,worker_name,worker_service,worker_location):
        self.worker_name =worker_name
        self.worker_service=worker_service
        self.worker_location=worker_location
        self.coordinates=self.get_coordinates()


    def get_coordinates(self) -> list:
        try:
            url = f"https://pl.wikipedia.org/wiki/{self.worker_location}"
            response = requests.get(url).text
            response_html = BeautifulSoup(response, "html.parser")
            longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
            latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
            print(latitude, longitude)
            return [latitude, longitude]
        except Exception:
            return None


def odswiez_liste_serwisow():
    listbox_lista_obiektow.delete(0, END)
    for service in model.services:
        listbox_lista_obiektow.insert(END, f"{service.service_name} ({service.service_location})")

def odswiez_liste_klientow():
    listbox_lista_obiektow_klient.delete(0, END)
    for klient in model.clients:
        listbox_lista_obiektow_klient.insert(END, f"{klient.client_name} ({klient.client_service})")

def odswiez_liste_pracownikow():
    listbox_lista_obiektow_pracownik.delete(0, END)
    for pracownik in model.workers:
        listbox_lista_obiektow_pracownik.insert(END, f"{pracownik.worker_name} ({pracownik.worker_service})")

def dodaj_serwis():
    nazwa = entry_serwis.get()
    lokalizacja = entry_location.get()
    if nazwa and lokalizacja:
        nowy_serwis=Services( nazwa,lokalizacja)
        model.services.append(nowy_serwis)
        odswiez_liste_serwisow()
        entry_serwis.delete(0, END)
        entry_location.delete(0, END)

def dodaj_klienta():
    imie = entry_klient.get()
    miejsce = entry_miejsce_zamieszkania_klienta.get()
    serwis = entry_serwis.get()
    if imie and miejsce and serwis:
        nowy_klient=Client( imie, serwis, miejsce)
        model.clients.append(nowy_klient)
        odswiez_liste_klientow()
        entry_klient.delete(0, END)
        entry_miejsce_zamieszkania_klienta.delete(0, END)
        entry_serwis.delete(0, END)

def dodaj_pracownik():
    imie = entry_pracownik.get()
    miejsce = entry_miejsce_zamieszkania_pracownika.get()
    serwis = entry_serwis.get()
    if imie and miejsce and serwis:
        nowy_pracownik=Worker(imie, serwis, miejsce)
        model.workers.append(nowy_pracownik)
        odswiez_liste_pracownikow()
        entry_pracownik.delete(0, END)
        entry_miejsce_zamieszkania_pracownika.delete(0, END)
        entry_serwis.delete(0, END)



def usun_serwis():
    index = listbox_lista_obiektow.curselection()
    if index:
        del model.services[index[0]]
        odswiez_liste_serwisow()

def usun_klienta():
    index = listbox_lista_obiektow_klient.curselection()
    if index:
        del model.clients[index[0]]
        odswiez_liste_klientow()

def usun_pracownika():
    index = listbox_lista_obiektow_pracownik.curselection()
    if index:
        del model.workers[index[0]]
        odswiez_liste_pracownikow()

def edytuj_serwis():
    global tryb_edycji, wybrany_indeks
    index = listbox_lista_obiektow.curselection()
    if index:
        tryb_edycji = "serwis"
        wybrany_indeks = index[0]
        dane = model.services[wybrany_indeks]
        entry_serwis.delete(0, END)
        entry_serwis.insert(0, dane.service_name)
        entry_location.delete(0, END)
        entry_location.insert(0, dane.service_location)

def edytuj_klienta():
    global tryb_edycji, wybrany_indeks
    index = listbox_lista_obiektow_klient.curselection()
    if index:
        tryb_edycji = "klient"
        wybrany_indeks = index[0]
        dane = model.clients[wybrany_indeks]
        entry_klient.delete(0, END)
        entry_klient.insert(0, dane.client_name)
        entry_serwis.delete(0, END)
        entry_serwis.insert(0, dane.client_service)
        entry_miejsce_zamieszkania_klienta.delete(0, END)
        entry_miejsce_zamieszkania_klienta.insert(0, dane.client_location1)


def edytuj_pracownika():
    global tryb_edycji, wybrany_indeks
    index = listbox_lista_obiektow_pracownik.curselection()
    if index:
        tryb_edycji = "pracownik"
        wybrany_indeks = index[0]
        dane = model.workers[wybrany_indeks]
        entry_pracownik.delete(0, END)
        entry_pracownik.insert(0, dane.worker_name)
        entry_miejsce_zamieszkania_pracownika.delete(0, END)
        entry_miejsce_zamieszkania_pracownika.insert(0, dane.worker_location)
        entry_serwis.delete(0, END)
        entry_serwis.insert(0, dane.worker_service)


def zapisz_obiekt():
    global tryb_edycji, wybrany_indeks
    if tryb_edycji == "serwis":
        nazwa = entry_serwis.get()
        lokalizacja = entry_location.get()
        if nazwa and lokalizacja:
            if wybrany_indeks is not None:
                model.services[wybrany_indeks].service_name =nazwa
                model.services[wybrany_indeks].service_location =lokalizacja
                model.services[wybrany_indeks].coordinates=model.services[wybrany_indeks].get_coordinates()
            else:
                model.services.append({'service_name': nazwa, 'service_location': lokalizacja})
            odswiez_liste_serwisow()

    elif tryb_edycji == "klient":
        name = entry_klient.get()
        location = entry_miejsce_zamieszkania_klienta.get()
        service = entry_serwis.get()
        if name and location and service:
            nowy_klient = Client(name, service, location)
            if wybrany_indeks is not None:
                model.clients[wybrany_indeks]=nowy_klient

            else:
                model.clients.append(nowy_klient)
            odswiez_liste_klientow()

    elif tryb_edycji == "pracownik":
        name = entry_pracownik.get()
        service = entry_serwis.get()
        location = entry_miejsce_zamieszkania_pracownika.get()
        if name and location and service:
            nowy_pracownik = Worker(name, service, location)
            if wybrany_indeks is not None:
                model.workers[wybrany_indeks] = nowy_pracownik
            else:
                model.workers.append(nowy_pracownik)
            odswiez_liste_pracownikow()

    # Reset formularza
    entry_pracownik.delete(0, END)
    entry_klient.delete(0, END)
    entry_miejsce_zamieszkania_klienta.delete(0, END)
    entry_miejsce_zamieszkania_pracownika.delete(0, END)
    entry_location.delete(0, END)
    entry_serwis.delete(0, END)
    tryb_edycji = None
    wybrany_indeks = None

def pokaz_wszystkie_serwisy():
    mapa.set_zoom(6)
    mapa.set_position(52.23, 21.0)
    mapa.delete_all_marker()
    for serwis in model.services:
        lat, lon = serwis.coordinates
        mapa.set_marker(lat, lon, text=serwis.service_name)

def pokaz_wszystkich_pracownikow():
    mapa.set_zoom(6)
    mapa.set_position(52.23, 21.0)
    mapa.delete_all_marker()
    for pracownik in model.workers:
        lat, lon = pracownik.coordinates
        mapa.set_marker(lat, lon, text=pracownik.worker_name)

def pokaz_klientow_serwisu(serwis_nazwa):
    mapa.delete_all_marker()
    serwis = next((s for s in model.services if s.service_name == serwis_nazwa), None)
    if serwis:
        lat_s, lon_s = serwis.coordinates
        mapa.set_position(lat_s, lon_s)
        mapa.set_zoom(9)
        klienci = [k for k in model.clients if k.client_service == serwis_nazwa]
        for klient in klienci:
            lat, lon = klient.coordinates
            mapa.set_marker(lat, lon, text=klient.client_name)
    else:
        print("Nie znaleziono serwisu")

def pokaz_pracownikow_serwisu(serwis_nazwa):
    mapa.delete_all_marker()
    serwis = next((s for s in model.services if s.service_name == serwis_nazwa), None)
    if serwis:
        lat_s, lon_s = serwis.coordinates
        mapa.set_position(lat_s, lon_s)
        mapa.set_zoom(9)
        pracownicy = [p for p in model.workers if p.worker_service == serwis_nazwa]
        for pracownik in pracownicy:
            lat, lon = pracownik.coordinates
            mapa.set_marker(lat, lon, text=pracownik.worker_name)


        print(f"Pokazuję pracowników dla serwisu: {serwis_nazwa}")
        print(f"Pracownicy w model.workers: {[p.worker_service for p in model.workers]}")
        print(f"Wybrane osoby: {[p.worker_name for p in pracownicy]}")

    else:
        print("Nie znaleziono serwisu")

root = Tk()
root.geometry("1200x760")
root.title("Projekt pop pf")
root.grid_rowconfigure(0, weight=3)
root.grid_rowconfigure(1, weight=2)

root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=2)


ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_map_interact=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0, sticky='nsew')
ramka_formularz.grid(row=0, column=1, sticky='nsew')
ramka_map_interact.grid(row=1, column=1, sticky='nsew')
ramka_mapa.grid(row=1, column=0,sticky='nsew')

# ramka_lista_serwisów
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista serwisów rowerowych")
label_lista_obiektow.grid(row=0, column=0,columnspan=2)
listbox_lista_obiektow=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
odswiez_liste_serwisow()
button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń serwis', command=usun_serwis)
button_usun_obiekt.grid(row=2, column=0,)
button_dodaj_obiekt = Button(ramka_lista_obiektow, text='Nowy serwis', command=dodaj_serwis)
button_dodaj_obiekt.grid(row=2, column=1,)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj serwis',command=edytuj_serwis)
button_edytuj_obiekt.grid(row=2, column=2)



#ramka_lista_klientów
label_lista_obiektow_klient=Label(ramka_lista_obiektow, text="Lista klientów")
label_lista_obiektow_klient.grid(row=0, column=3,columnspan=2)
listbox_lista_obiektow_klient=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_klient.grid(row=1, column=3, columnspan=3)
odswiez_liste_klientow()
button_usun_obiekt_klient=Button(ramka_lista_obiektow, text='Usuń klienta', command=usun_klienta)
button_usun_obiekt_klient.grid(row=2, column=3)
button_dodaj_obiekt_klient = Button(ramka_lista_obiektow, text='Nowy klient', command=dodaj_klienta)
button_dodaj_obiekt_klient.grid(row=2, column=4,)
button_edytuj_obiekt_klient=Button(ramka_lista_obiektow, text='Edytuj klienta', command=edytuj_klienta)
button_edytuj_obiekt_klient.grid(row=2, column=5)

#ramka_lista_pracowników
label_lista_obiektow_pracownik=Label(ramka_lista_obiektow, text="Lista pracowników")
label_lista_obiektow_pracownik.grid(row=0, column=6,columnspan=2)
listbox_lista_obiektow_pracownik=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_pracownik.grid(row=1, column=6, columnspan=3)
odswiez_liste_pracownikow()
button_usun_obiekt_pracownik=Button(ramka_lista_obiektow, text='Usuń pracownika', command=usun_pracownika)
button_usun_obiekt_pracownik.grid(row=2, column=6)
button_dodaj_obiekt_pracownik=Button(ramka_lista_obiektow, text='Nowy pracownik', command=dodaj_pracownik)
button_dodaj_obiekt_pracownik.grid(row=2, column=7)
button_edytuj_obiekt_pracownik=Button(ramka_lista_obiektow, text='Edytuj pracownika', command=edytuj_pracownika)
button_edytuj_obiekt_pracownik.grid(row=2, column=8)

# ramka_formularz
label_formularz=Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=0, columnspan=2)
label_pracownik=Label(ramka_formularz, text="Pracownik:")
label_pracownik.grid(row=1, column=0, sticky=W)
label_klient=Label(ramka_formularz, text="Klient:")
label_klient.grid(row=2, column=0,sticky=W)
label_miejsce_zamieszkania_klienta=Label(ramka_formularz, text="Miejsce zamieszkania klienta:")
label_miejsce_zamieszkania_klienta.grid(row=3, column=0, sticky=W)
label_miejsce_zamieszkania_pracownika=Label(ramka_formularz, text="Miejsce zamieszkania pracownika:")
label_miejsce_zamieszkania_pracownika.grid(row=4, column=0, sticky=W)
label_location=Label(ramka_formularz, text="Lokalizacja serwisu:")
label_location.grid(row=5, column=0,sticky=W)
label_serwis=Label(ramka_formularz, text="Serwis rowerowy:")
label_serwis.grid(row=6, column=0,sticky=W)

entry_pracownik=Entry(ramka_formularz)
entry_pracownik.grid(row=1, column=1)
entry_klient=Entry(ramka_formularz)
entry_klient.grid(row=2, column=1)
entry_miejsce_zamieszkania_klienta=Entry(ramka_formularz)
entry_miejsce_zamieszkania_klienta.grid(row=3, column=1)
entry_miejsce_zamieszkania_pracownika=Entry(ramka_formularz)
entry_miejsce_zamieszkania_pracownika.grid(row=4, column=1)
entry_location=Entry(ramka_formularz)
entry_location.grid(row=5, column=1)
entry_serwis=Entry(ramka_formularz)
entry_serwis.grid(row=6, column=1)

button_dodaj_obiekt=Button(ramka_formularz, text='Zapisz dane', command=zapisz_obiekt)
button_dodaj_obiekt.grid(row=7, column=0, columnspan=2)

#ramka_zarzAdzanie_mapa
ramka_map_interact.grid_columnconfigure(1, weight=1)
label_map_interact=Label(ramka_map_interact,text="Zarządzanie mapą:",)
label_map_interact.grid(row=0, column=0)
button_serwisy = Button(ramka_map_interact, text="Pokaż serwisy", command=pokaz_wszystkie_serwisy)
button_serwisy.grid(row=1, column=0,)
button_pracownicy = Button(ramka_map_interact, text="Pokaż wszystkich pracowników", command=pokaz_wszystkich_pracownikow)
button_pracownicy.grid(row=2, column=0,)
selected_service = StringVar()
lista_serwisow = Combobox(ramka_map_interact, textvariable=selected_service, values=[s.service_name for s in model.services])
lista_serwisow.grid(row=3, column=0)
button_klienci = Button(ramka_map_interact, text="Pokaż klientów serwisu", command=lambda: pokaz_klientow_serwisu(selected_service.get()))
button_klienci.grid(row=4, column=0)
button_pracownicy_serwisu = Button(ramka_map_interact, text="Pokaż pracowników serwisu", command=lambda: pokaz_pracownikow_serwisu(selected_service.get()))
button_pracownicy_serwisu.grid(row=5, column=0)



# ramka_mapa
mapa = tkintermapview.TkinterMapView(ramka_mapa, width=800, height=550,)
mapa.set_position(52.23,21.0)
mapa.set_zoom(6)
mapa.grid(row=0, column=0,)

root.mainloop()