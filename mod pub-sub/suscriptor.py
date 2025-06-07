"""
Sistema de Publicación-Suscripción con Kafka y MySQL
----------------------------------------------------

Arquitectura compuesta por 4 componentes principales que interactúan mediante el patrón Pub/Sub:

4. SUSCRIPTOR (Interfaz de Consulta)
---------------------------------
Responsabilidad:
- Permite consultar los datos almacenados

Funcionamiento:
- Interfaz interactiva por consola
- Conexión directa a MySQL
- Consultas SELECT a tablas específicas
- Soporta consultas múltiples
- Muestra resultados en crudo

Flujo de Datos Principal:
generador → Kafka → [procesador | DB] → suscriptor

"""

import mysql.connector

def mostrar_bd(temas):
    """
    Consultor de base de datos para suscriptores
    
    Muestra contenido de tablas según selección:
    - Conecta a MySQL local
    - Ejecuta queries SELECT
    - Muestra resultados por consola
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Suscripciones"
        )

        cursor = connection.cursor()

        for table in temas:
            query = f"SELECT * FROM {table}"
            cursor.execute(query)

            print(f"\nMostrando datos de la tabla {table}:")
            for row in cursor.fetchall():
                print(row)

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def main():
    """
    Interfaz de suscripción
    
    Permite seleccionar temas (tablas) a visualizar:
    - Menú interactivo
    - Soporte múltiples selecciones
    - Opción de salida
    """
    print("Seleccione tablas para suscribirse (separadas por comas):")
    print("1. Vehículos")
    print("2. Jugadores de fútbol")
    print("3. Clima")
    print("4. Películas")
    print("'exit' para salir")

    while True:
        opciones = input("Ingrese números (ej. 1,2): ")
        
        if opciones.lower() == "exit":
            break
        
        temas = []
        for opcion in opciones.split(','):
            if opcion.strip() == "1":
                temas.append("vayven")
            elif opcion.strip() == "2":
                temas.append("futbolistas")
            elif opcion.strip() == "3":
                temas.append("servicio_meteorologico")
            elif opcion.strip() == "4":
                temas.append("peliculas")
            else:
                print(f"Opción '{opcion.strip()}' no válida")

        mostrar_bd(temas)

main()