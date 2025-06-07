"""
Sistema de Comunicación Multicast UDP
-------------------------------------

Implementa un modelo publisher-subscriber usando sockets multicast:
- emisor.py: Envía mensajes a un grupo multicast
- receptor.py: Recibe mensajes del grupo multicast
- constantes.py: Configuración compartida

Características Clave:
-----------------------------
- Comunicación uno-a-muchos (multidifusión IP)
- Rango de direcciones 224.0.0.0 a 239.255.255.255
- Protocolo UDP para baja latencia
- Gestión adecuada de recursos de red

Configuración Multicast Compartida
---------------------------------
Centraliza parámetros de comunicación.
"""

class Constantes:
    # Defino la dirección multicast, que debe estar en el rango [224.0.0.0 - 239.255.255.255]
    DIRECCION = "224.0.0.1"
    # Defino el puerto UDP válido, que debe estar en el rango [1024 - 65535]
    PUERTO = 9797
    # Defino el tamaño del datagrama
    TALLA_BUFFER = 256
    # Defino una cadena que indica el fin de la comunicación
    FIN_MENSAJES = "EXIT"
