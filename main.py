
from tkinter import *
import tkintermapview

import requests
from bs4 import BeautifulSoup

from utils import model



class Services:
    def __init__(self, service_name, service_location, ):
        self.service_name = service_name

        self.service_location = service_location

        self.coordinates = self.get_coordinates()



    def get_coordinates(self) -> list:
        url = f"https://pl.wikipedia.org/wiki/{self.service_location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]


class Client:
    def __init__(self,client_name,client_service,client_location1,client_location2):
        self.client_name =client_name
        self.client_service=client_service
        self.client_location1=client_location1
        self.client_location2=client_location2
        self.coordinates=self.get_coordinates()


    def get_coordinates(self) -> list:
        url = f"https://pl.wikipedia.org/wiki/{self.client_location2}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
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
        print(longitude)
        print(latitude)
        return [latitude, longitude]


def odswiez_liste_serwisow():
    listbox_lista_obiektow.delete(0, END)
    for service in model.services:
        listbox_lista_obiektow.insert(END, f"{service['service_name']} ({service['service_location']})")

def odswiez_liste_klientow():
    listbox_lista_obiektow_klient.delete(0, END)
    for klient in model.clients:
        listbox_lista_obiektow_klient.insert(END, f"{klient['client_name']} ({klient['client_service']})")

def odswiez_liste_pracownikow():
    listbox_lista_obiektow_pracownik.delete(0, END)
    for pracownik in model.workers:
        listbox_lista_obiektow_pracownik.insert(END, f"{pracownik['worker_name']} ({pracownik['worker_service']})")


root = Tk()
root.geometry("1200x760")
root.title("Projekt pop pf")


ramka_lista_obiektow=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0,columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# ramka_lista_serwisów
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista serwisów rowerowych")
label_lista_obiektow.grid(row=0, column=0,columnspan=2)
listbox_lista_obiektow=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
odswiez_liste_serwisow()
button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń obiekt')
button_usun_obiekt.grid(row=2, column=0,)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj obiekt')
button_edytuj_obiekt.grid(row=2, column=2)



#ramka_lista_klientów
label_lista_obiektow_klient=Label(ramka_lista_obiektow, text="Lista klientów")
label_lista_obiektow_klient.grid(row=0, column=3,columnspan=2)
listbox_lista_obiektow_klient=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_klient.grid(row=1, column=3, columnspan=3)
odswiez_liste_klientow()
button_usun_obiekt_klient=Button(ramka_lista_obiektow, text='Usuń obiekt')
button_usun_obiekt_klient.grid(row=2, column=3)
button_edytuj_obiekt_klient=Button(ramka_lista_obiektow, text='Edytuj obiekt')
button_edytuj_obiekt_klient.grid(row=2, column=5)

#ramka_lista_pracowników
label_lista_obiektow_pracownik=Label(ramka_lista_obiektow, text="Lista pracowników")
label_lista_obiektow_pracownik.grid(row=0, column=6,columnspan=2)
listbox_lista_obiektow_pracownik=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_pracownik.grid(row=1, column=6, columnspan=3)
odswiez_liste_pracownikow()
button_usun_obiekt_pracownik=Button(ramka_lista_obiektow, text='Usuń obiekt')
button_usun_obiekt_pracownik.grid(row=2, column=6)
button_edytuj_obiekt_pracownik=Button(ramka_lista_obiektow, text='Edytuj obiekt')
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

button_dodaj_obiekt=Button(ramka_formularz, text='Dodaj obiekt')
button_dodaj_obiekt.grid(row=7, column=0, columnspan=2)



# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23,21.0)
map_widget.set_zoom(6)



root.mainloop()