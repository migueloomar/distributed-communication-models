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

Emisor Multicast
----------------
Envía mensajes a un grupo multicast configurable.
Permite salir con el comando 'exit'.
"""

import socket

# Configuración de dirección y puerto multicast (rango válido)
MULTICAST_GROUP = '224.1.1.1'   # Dirección de grupo clase D
PORT = 5007                     # Puerto UDP válido

# 1. Creación de socket UDP estándar
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        # 2. Captura interactiva de mensaje
        message = input("Escribe un mensaje: ")

        # 3. Condición de salida controlada
        if message.lower() == 'exit':
            break 

        # 4. Envío multicast al grupo
        print(f"Enviando mensaje multicast a {MULTICAST_GROUP}:{PORT}")
        sock.sendto(message.encode(), (MULTICAST_GROUP, PORT))
        
finally:
    # 5. Liberación segura del socket
    print("Cerrando socket")
    sock.close()
