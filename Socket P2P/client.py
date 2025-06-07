"""
Cliente P2P Basado en UDP
-----------------------------

Implementa un cliente para comunicación peer-to-peer (P2P) usando sockets UDP.
Permite enviar y recibir mensajes de forma interactiva con otro peer.

Características Clave:
-----------------------------
- Protocolo UDP para comunicación directa
- Entrada de mensajes interactiva
- Recepción asíncrona de respuestas
- Cierre seguro de conexiones

Flujo Básico:
1. Crea socket UDP
2. Envía mensajes ingresados por el usuario
3. Espera y muestra respuestas
4. Repite hasta interrupción (Ctrl+C)
"""

import socket

# Configuración de conexión
server_address = ('localhost', 12345)   # Dirección del peer remoto

# 1. Creación del socket UDP para comunicación P2P
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        # 2. Captura y envío de mensaje
        message = input("Ingrese un mensaje: ").encode()
        print('Enviando {!r}'.format(message))
        sent = sock.sendto(message, server_address)

        # 3. Recepción de respuesta
        print('Esperando respuesta...')
        data, server = sock.recvfrom(4096)
        print('Recibimos {!r} desde {}'.format(data, server))

finally:
    # 4. Liberación de recursos
    print('Cerrando el socket')
    sock.close()
