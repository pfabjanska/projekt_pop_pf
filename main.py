from tkinter import *

import tkintermapview

services: list =[]
clients:list=[]
workers:list=[]


class Services:
    def _init_(self, service_name, service_location, ):
        self.service_name = service_name

        self.service_location = service_location

        self.coordinates = self.get_coordinates()
        # self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.service_location}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]


class Client:
    def _init_(self,client_name,client_service,client_location1,client_location2):
        self.client_name =client_name
        self.client_service=client_service
        self.client_location1=client_location1
        self.client_location2=client_location2
        self.coordinates=self.get_coordinates()
        # self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup
        url = f"https://pl.wikipedia.org/wiki/{self.client_location2}"
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
        latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
        print(longitude)
        print(latitude)
        return [latitude, longitude]


class Workers:
    def _init_(self,worker_name,worker_service,worker_location):
        self.worker_name =worker_name
        self.worker_service=worker_service
        self.worker_location=worker_location

        self.coordinates=self.get_coordinates()
        # self.marker=map_widget.set_marker(self.coordinates[0],self.coordinates[1])

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

# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_obiektow, text="Lista serwisów rowerowych")
label_lista_obiektow.grid(row=0, column=0,columnspan=2)
listbox_lista_obiketow=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiketow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly_obiektu=Button(ramka_lista_obiektow, text='Pokaż szczegóły')
button_pokaz_szczegoly_obiektu.grid(row=2, column=0,)
button_usun_obiekt=Button(ramka_lista_obiektow, text='Usuń obiekt')
button_usun_obiekt.grid(row=2, column=1,)
button_edytuj_obiekt=Button(ramka_lista_obiektow, text='Edytuj obiekt')
button_edytuj_obiekt.grid(row=2, column=2)

#ramka_lista_pracowników
label_lista_obiektow_klient=Label(ramka_lista_obiektow, text="Lista klientów")
label_lista_obiektow_klient.grid(row=0, column=3,columnspan=2)
listbox_lista_obiektow_klient=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_klient.grid(row=1, column=3, columnspan=3)
button_pokaz_szczegoly_obiektu_klient=Button(ramka_lista_obiektow, text='Pokaż szczegóły')
button_pokaz_szczegoly_obiektu_klient.grid(row=2, column=3)
button_usun_obiekt_klient=Button(ramka_lista_obiektow, text='Usuń obiekt')
button_usun_obiekt_klient.grid(row=2, column=4)
button_edytuj_obiekt_klient=Button(ramka_lista_obiektow, text='Edytuj obiekt')
button_edytuj_obiekt_klient.grid(row=2, column=5)

#ramka_lista_pracowników
label_lista_obiektow_pracownik=Label(ramka_lista_obiektow, text="Lista pracowników")
label_lista_obiektow_pracownik.grid(row=0, column=6,columnspan=2)
listbox_lista_obiektow_pracownik=Listbox(ramka_lista_obiektow, width=40, height=10)
listbox_lista_obiektow_pracownik.grid(row=1, column=6, columnspan=3)
button_pokaz_szczegoly_obiektu_pracownik=Button(ramka_lista_obiektow, text='Pokaż szczegóły')
button_pokaz_szczegoly_obiektu_pracownik.grid(row=2, column=6)
button_usun_obiekt_pracownik=Button(ramka_lista_obiektow, text='Usuń obiekt')
button_usun_obiekt_pracownik.grid(row=2, column=7)
button_edytuj_obiekt_pracownik=Button(ramka_lista_obiektow, text='Edytuj obiekt')
button_edytuj_obiekt_pracownik.grid(row=2, column=8)

# ramka_formularz
label_formularz=Label(ramka_formularz, text="Formularz")
label_formularz.grid(row=0, column=0, columnspan=2)
label_pracownik=Label(ramka_formularz, text="Pracownik:")
label_pracownik.grid(row=1, column=0, sticky=W)
label_klient=Label(ramka_formularz, text="Klient:")
label_klient.grid(row=2, column=0,sticky=W)
label_miejsce_zamieszkania=Label(ramka_formularz, text="Miejsce zamieszkania:")
label_miejsce_zamieszkania.grid(row=3, column=0, sticky=W)
label_location=Label(ramka_formularz, text="Lokalizacja serwisu:")
label_location.grid(row=4, column=0,sticky=W)
label_serwis=Label(ramka_formularz, text="Serwis rowerowy:")
label_serwis.grid(row=5, column=0,sticky=W)

entry_pracownik=Entry(ramka_formularz)
entry_pracownik.grid(row=1, column=1)
entry_klient=Entry(ramka_formularz)
entry_klient.grid(row=2, column=1)
entry_miejsce_zamieszkania=Entry(ramka_formularz)
entry_miejsce_zamieszkania.grid(row=3, column=1)
entry_location=Entry(ramka_formularz)
entry_location.grid(row=4, column=1)
entry_serwis=Entry(ramka_formularz)
entry_serwis.grid(row=5, column=1)

button_dodaj_obiekt=Button(ramka_formularz, text='Dodaj obiekt')
button_dodaj_obiekt.grid(row=6, column=0, columnspan=2)

# ramka_szczegoly_obiektow
label_szczegoly_obiektow=Label(ramka_szczegoly_obiektow, text="Szczegóły obiektu:")
label_szczegoly_obiektow.grid(row=0, column=4)
label_szczegoly_pracownik=Label(ramka_szczegoly_obiektow, text="Pracownik:")
label_szczegoly_pracownik.grid(row=1, column=0)
label_szczegoly_pracownik_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_pracownik_wartosc.grid(row=1, column=1)
label_szczegoly_klient=Label(ramka_szczegoly_obiektow, text="Klient:")
label_szczegoly_klient.grid(row=1, column=2)
label_szczegoly_miejsce_zamieszkania_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_miejsce_zamieszkania_wartosc.grid(row=1, column=3)
label_szczegoly_miejsce_zamieszkania=Label(ramka_szczegoly_obiektow, text="Miejsce zamieszkania:")
label_szczegoly_miejsce_zamieszkania.grid(row=1, column=4)
label_szczegoly_klient_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_klient_wartosc.grid(row=1, column=5)
label_szczegoly_location=Label(ramka_szczegoly_obiektow, text="Lokalizacja serwisu:")
label_szczegoly_location.grid(row=1, column=6)
label_szczegoly_location_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_location_wartosc.grid(row=1, column=7)
label_szczegoly_serwis=Label(ramka_szczegoly_obiektow, text="Serwis rowerowy:")
label_szczegoly_serwis.grid(row=1, column=8)
label_szczegoly_serwis_wartosc=Label(ramka_szczegoly_obiektow, text="....")
label_szczegoly_serwis_wartosc.grid(row=1, column=9)

# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500, corner_radius=5)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23,21.0)
map_widget.set_zoom(6)



root.mainloop()