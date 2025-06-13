services: list[dict] = [
    {'service_name': 'HappyBike', 'service_location': 'Turek'},
    {'service_name': 'BikeProject', 'service_location': 'Warszawa'},
    {'service_name': 'Sportset', 'service_location': 'Kutno'},
    {'service_name': 'Rowerologia', 'service_location': 'Gdańsk'}
]

clients: list[dict] = [
    {'client_name': 'Andrzej Grodzik', 'client_service': 'HappyBike', 'client_location1': 'Poznań', 'client_location2': 'Turek'},
    {'client_name': 'Maja Gaja','client_service':'BikeProject', 'client_location1':'Warszawa', 'client_location2':'Kutno'},
    {'client_name': 'Szymon Kajak','client_service':'Sportset', 'client_location1':'Warszawa', 'client_location2':'Kutno'},
    {'client_name': 'Milena Kolarka','client_service':'Rowerologia','client_location1':'Gdańsk'}
]

workers: list[dict] = [
    {'worker_name': 'Ryszard Śliski', 'worker_service': 'HappyBike', 'worker_location': 'Koło'},
    {'worker_name': 'Marta Kowalska', 'worker_service': 'BikeProject', 'worker_location': 'Wołomin'},
    {'worker_name': 'Stefan Potoczek', 'worker_service': 'Sportset', 'worker_location': 'Łowicz'},
    {'worker_name': 'Malwina Kalina', 'worker_service': 'Rowerologia', 'worker_location':'Szczecin'}
]