"""
Servidor P2P Basado en UDP
-----------------------------

Implementa un servidor para comunicación peer-to-peer (P2P) usando sockets UDP.
Recibe mensajes y envía respuestas interactivamente a clientes.

Características Clave:
-----------------------------
- Protocolo UDP para comunicación directa
- Escucha en puerto configurable (12345)
- Respuestas interactivas por consola
- Registro detallado de actividad

Flujo Básico:
1. Crea y enlaza socket UDP
2. Espera mensajes entrantes
3. Muestra mensaje recibido y origen
4. Permite enviar respuesta interactiva
5. Repite indefinidamente
"""

import socket

# Configuración del servidor P2P
server_address = ('localhost', 12345)   # (IP, Puerto) local

# 1. Creación y enlace del socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

while True:
    # 2. Espera de mensajes entrantes
    print('Esperando respuesta...')
    data, address = sock.recvfrom(4096)

    # 3. Procesamiento de mensaje recibido
    print('La respuesta fue: {!r} desde {}'.format(data, address))

    if data:
        # 4. Generación y envío de respuesta
        response = input("Ingrese una respuesta: ").encode()
        sent = sock.sendto(response, address)
        print('Enviado {!r} a {}'.format(response, address))
