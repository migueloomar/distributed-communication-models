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

Receptor Multicast
------------------
Recibe mensajes de un grupo multicast configurable.
Requiere unión explícita al grupo.
"""

import socket
import struct

# Misma configuración que el emisor
MULTICAST_GROUP = '224.1.1.1'
PORT = 5007

# 1. Creación de socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Configuración especial multicast:
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite reuso de dirección

# 3. Unión al grupo multicast:
sock.bind(('', PORT))     # Escucha en todos los interfaces
mreq = struct.pack('4sL', 
                   socket.inet_aton(MULTICAST_GROUP), 
                   socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

try:
    while True:
        # 4. Recepción continua de mensajes
        print("Esperando recibir mensaje...")
        data, address = sock.recvfrom(1024)
        print(f"Mensaje recibido de {address}: {data.decode()}")
finally:
    # 5. Liberación segura del socket
    print("Cerrando socket")
    sock.close()
