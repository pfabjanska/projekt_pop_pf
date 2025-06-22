from utils.controller import Services, Client, Worker

services = [
    Services("BikeTur", 'Turek'),
    Services("Cozmo Bike", 'Warszawa'),
    Services("Bike Atelier", 'Katowice'),
    Services("Rotech", 'Kutno')
]



clients = [
    Client("Andrzej Grodzik","BikeTur", "Konin"),
    Client("Aaleksandra Kot","BikeTur", "Uniejów"),
    Client("Maja Gaja","Cozmo Bike", "Wołomin"),
    Client("Hubert Piasecki", "Cozmo Bike", "Piaseczno"),
    Client("Szymon Kajak","Rotech", "Krośniewice"),
    Client("Urszula Kamińska","Rotech", "Łęczyca"),
    Client("Milena Kolarka","Bike Atelier", "Bytom"),
    Client("Mateusz Małecki","Bike Atelier", "Zabrze")
]


workers = [
    Worker("Ryszard Śliski","Bike Atelier", "Rybnik"),
    Worker("Kamila Oscypiuk","Bike Atelier", "Tychy"),
    Worker("Jagoda Śmieszek","Bike Atelier", "Jaworzno"),
    Worker("Marta Kowalska","Cozmo Bike", "Otwock"),
    Worker("Kacper Kosiński","Cozmo Bike", "Żyrardów"),
    Worker("Wiktor Wiśniewski","Cozmo Bike", "Łomianki"),
    Worker("Stefan Potoczek","Rotech", "Łowicz"),
    Worker("Izabela Nitka","Rotech", "Dobrzelin"),
    Worker("Malwina Kalina", "BikeTur", "Konin"),
    Worker("Filip Łaski","BikeTur", "Tuliszków")
]


