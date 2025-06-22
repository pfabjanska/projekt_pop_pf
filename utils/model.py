from utils.controller import Services, Client, Worker

services = [
    Services("BikeTur", 'Turek'),
    Services("Cozmo Bike", 'Warszawa'),
    Services("Bike Atelier", 'Katowice'),
    Services("Rotech", 'Kutno')
]



clients = [
    Client("Andrzej Grodzik","BikeTur", "Poznań"),
    Client("Maja Gaja","Cozmo Bike", "Wołomin"),
    Client("Szymon Kajak","Rotech", "Krośniewice"),
    Client("Milena Kolarka","Bike Atelier", "Sopot")
]


workers = [
    Worker("Ryszard Śliski","Bike Atelier", "Radom"),
    Worker("Ryszard Śliski","Bike Atelier", "Radom"),
    Worker("Ryszard Śliski","Bike Atelier", "Radom"),
    Worker("Marta Kowalska","Cozmo Bike", "Kielce"),
    Worker("Marta Kowalska","Cozmo Bike", "Kielce"),
    Worker("Marta Kowalska","Cozmo Bike", "Kielce"),
    Worker("Stefan Potoczek","Rotech", "Łowicz"),
    Worker("Stefan Potoczek","Rotech", "Łowicz"),
    Worker("Malwina Kalina", "BikeTur", "Szczecin")
    Worker("Malwina Kalina","BikeTur", "Szczecin")
]


