"""
Sistema de Publicación-Suscripción con Kafka y MySQL
----------------------------------------------------

Arquitectura compuesta por 4 componentes principales que interactúan mediante el patrón Pub/Sub:

2. PROCESADOR (Subscriber)
---------------------------------
Responsabilidad:
- Consume mensajes de Kafka 
- Transforma y muestra los datos en consola

Funcionamiento:
- Se suscribe a los 4 topics
- Deserializa los mensajes (string → dict)
- Convierte los datos a DataFrames pandas
- Muestra información formateada en tablas
- Procesa un mensaje cada 5 segundos

Flujo de Datos Principal:
generador → Kafka → [procesador | DB] → suscriptor

"""

from confluent_kafka import Consumer, KafkaError
import pandas as pd
import time

def process_info(msg):

    """
    Procesador de mensajes Kafka
    
    Transformaciones:
    - Deserializa mensaje (string → dict)
    - Convierte a DataFrame pandas
    - Muestra en consola
    """

    info = eval(msg.value())
    print(f'Procesando información: {info}')

    df = pd.DataFrame([info])
    print(df.to_string(index=False)) 

def consume_info():

    """
    Consumer Kafka para procesamiento
    
    Configuración:
    - Grupo: mygroup
    - Offset: earliest
    - Topics: vehiculo, jugadores_futbol, datos_clima, datos_peliculas
    """
    
    c = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    })

    c.subscribe(['vehiculo', 'jugadores_futbol', 'datos_clima', 'datos_peliculas'])

    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            process_info(msg)
            time.sleep(5)  

    except KeyboardInterrupt:
        pass
    finally:
        c.close()

consume_info()

