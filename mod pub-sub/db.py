"""
Sistema de Publicación-Suscripción con Kafka y MySQL
----------------------------------------------------

Arquitectura compuesta por 4 componentes principales que interactúan mediante el patrón Pub/Sub:

3. DB (Subscriber/Persistencia)
---------------------------------
Responsabilidad:
- Consume mensajes de Kafka
- Almacena los datos en MySQL

Funcionamiento:
- Misma suscripción que el procesador
- Router de mensajes por tipo de dato
- Inserciones en tablas correspondientes:
  * vayven (vehículos)
  * futbolistas (jugadores)
  * servicio_meteorologico (clima)
  * peliculas (películas)
- Manejo transaccional (commit/rollback)

Flujo de Datos Principal:
generador → Kafka → [procesador | DB] → suscriptor

"""

import mysql.connector
from confluent_kafka import Consumer, KafkaError

def insert_vehiculo(data):

    """Inserta datos de vehículos en tabla vayven"""

    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="Suscripciones"
        )

        cursor = connection.cursor()

        # tabla de vehículos
        sql = "INSERT INTO vayven (pasajeros, velocidad, conductor, id_vehiculo) VALUES (%s, %s, %s, %s)"
        val = (
            data["pasajeros"],
            data["velocidad"],
            data["conductor"],
            data["id_vehiculo"]
        )
        cursor.execute(sql, val)

        connection.commit()
        print(f"Datos de vehículo insertados correctamente")

    except Exception as e:
        print(f"Error al insertar datos de vehículo en la base de datos: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_jugador(data):

    """Inserta datos de jugadores en tabla futbolistas"""

    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="Suscripciones"
        )

        cursor = connection.cursor()

        # tabla de jugadores
        sql = "INSERT INTO futbolistas (nombre, edad, equipo, seleccion) VALUES (%s, %s, %s, %s)"
        val = (
            data["nombre"],
            data["edad"],
            data["equipo"],
            data["seleccion"]
        )
        cursor.execute(sql, val)

        connection.commit()
        print(f"Datos de jugador insertados correctamente")

    except Exception as e:
        print(f"Error al insertar datos de jugador en la base de datos: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_clima(data):

    """Inserta datos climáticos en tabla servicio_meteorologico"""

    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="Suscripciones"
        )

        cursor = connection.cursor()

        # tabla de clima
        sql = "INSERT INTO servicio_meteorologico (ciudad, temperatura, probabilidad_lluvia) VALUES (%s, %s, %s)"
        val = (
            data["ciudad"],
            data["temperatura"],
            data["probabilidad_lluvia"]
        )
        cursor.execute(sql, val)

        connection.commit()
        print(f"Datos de clima insertados correctamente")

    except Exception as e:
        print(f"Error al insertar datos de clima en la base de datos: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_pelicula(data):

    """Inserta datos de películas en tabla peliculas"""

    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="Suscripciones"
        )

        cursor = connection.cursor()

        # tabla de películas
        sql = "INSERT INTO peliculas (nombre_pelicula, director, anio_publicacion) VALUES (%s, %s, %s)"
        val = (
            data["nombre_pelicula"],
            data["director"],
            data["anio_publicacion"]
        )
        cursor.execute(sql, val)

        connection.commit()
        print(f"Datos de película insertados correctamente")

    except Exception as e:
        print(f"Error al insertar datos de película en la base de datos: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def process_info(msg):

    """Router de mensajes Kafka a funciones de inserción"""

    data = eval(msg.value().decode("utf-8")) 

    if "id_vehiculo" in data:
        insert_vehiculo(data)
    elif "nombre" in data:
        insert_jugador(data)
    elif "ciudad" in data:
        insert_clima(data)
    elif "nombre_pelicula" in data:
        insert_pelicula(data)

def consume_info():

    """Consumer Kafka para persistencia en DB"""

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

    except KeyboardInterrupt:
        pass

    finally:
        c.close()

consume_info()
