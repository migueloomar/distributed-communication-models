"""
Sistema de Publicación-Suscripción con Kafka y MySQL
----------------------------------------------------

Arquitectura compuesta por 4 componentes principales que interactúan mediante el patrón Pub/Sub:

1. GENERADOR (Publisher)
---------------------------------
Responsabilidad: 
- Genera datos aleatorios de 4 dominios diferentes (vehículos, jugadores, clima, películas)
- Publica los mensajes en topics Kafka correspondientes

Funcionamiento:
- Usa la librería Faker para generar datos realistas
- Crea estructuras de datos en formato diccionario
- Serializa los datos a strings
- Publica en Kafka cada 1 segundo
- Implementa callbacks para confirmación de entrega

Topics Kafka:
- vehiculo
- jugadores_futbol 
- datos_clima
- datos_peliculas

Flujo de Datos Principal:
generador → Kafka → [procesador | DB] → suscriptor

"""

from confluent_kafka import Producer
import random
import time
import string
from faker import Faker
fake = Faker()

def id_vehiculo():
    """Genera ID de vehículo con formato XXX-XX-XX"""
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=4))
    return f"{letras}-{numeros[:2]}-{numeros[2:]}"

def info_vehiculo_random():
    """Genera datos aleatorios de vehículos usando Faker"""
    return {
        "pasajeros": random.randint(1, 50),
        "velocidad": random.randint(20, 120),
        "conductor": fake.name(),  
        "id_vehiculo": id_vehiculo()  
    }

def info_jugador_random():
    """Genera datos aleatorios de jugadores usando Faker"""
    return {
        "nombre": fake.name(),  
        "edad": random.randint(18, 40),  
        "equipo": fake.company(),  
        "seleccion": fake.country() 
    }

def info_clima_random():
    """Genera datos aleatorios de clima usando Faker"""
    return {
        "ciudad": fake.city(), 
        "temperatura": round(random.uniform(-10, 40), 2), 
        "probabilidad_lluvia": round(random.uniform(0, 100), 2)  
    }

def info_pelicula_random():
    """Genera datos aleatorios de películas usando Faker"""
    return {
        "nombre_pelicula": fake.catch_phrase(),  
        "director": fake.name(),  
        "anio_publicacion": random.randint(1950, 2024)  
    }

def delivery_report(err, msg):
    """Callback para confirmación de envío a Kafka"""
    if err is not None:
        print(f'Error: {err}')

def produce_info():

    """
    Producer Kafka principal
    
    Publica mensajes cada 1 segundo en:
    - vehiculo, jugadores_futbol, datos_clima, datos_peliculas
    """
    p = Producer({'bootstrap.servers': 'localhost:9092'})

    while True:
        info_vehiculo = info_vehiculo_random()
        info_jugador = info_jugador_random()
        info_clima = info_clima_random()
        info_pelicula = info_pelicula_random()
        
        p.produce('vehiculo', key='vayven', value=str(info_vehiculo), callback=delivery_report)
        p.produce('jugadores_futbol', key='jugador', value=str(info_jugador), callback=delivery_report)
        p.produce('datos_clima', key='clima', value=str(info_clima), callback=delivery_report)
        p.produce('datos_peliculas', key='pelicula', value=str(info_pelicula), callback=delivery_report)
        
        p.poll(0.5)
        time.sleep(1)

    p.flush()

produce_info()

produce_info()