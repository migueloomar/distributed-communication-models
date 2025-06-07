# Sistemas Distribuidos - Módulos de Comunicación

Este repositorio contiene implementaciones prácticas de varios modelos de comunicación utilizados en sistemas distribuidos, incluyendo Pub/Sub con Kafka, RPC, sockets TCP/UDP y comunicación P2P.

---

## 🧵 1. Modulo Pub/Sub con Kafka y MySQL

**Tecnologías:** Kafka, Python, MySQL, Faker

**Componentes:**
- `Generador`: Publica datos aleatorios a 4 topics (`vehiculo`, `jugadores_futbol`, `datos_clima`, `datos_peliculas`).
- `Procesador`: Consume y muestra datos como DataFrames.
- `DB`: Guarda los datos en tablas MySQL según el tipo.
- `Suscriptor`: Consulta los datos almacenados vía consola.

**Ventajas:** Escalabilidad, desacoplamiento, tolerancia a fallos.

---

## 📡 2. RPC XML-RPC (rpc_units)

**Cliente-Servidor para Conversión de Unidades (Longitud)**  
Basado en **XML-RPC sobre HTTP**.

- **Servidor:** Expone método `convertir(valor, unidad_origen, unidad_destino)`.
- **Cliente:** Invoca remotamente el método como si fuera local.

---

## 🛰️ 3. RMI con XML-RPC (rpc_units-rmi)

**Invocación Remota de Métodos usando XML-RPC**

Extiende el sistema anterior con principios de RMI:
- Transparencia de ubicación
- Marshalling XML automático
- Modelo cliente-servidor vía HTTP en puerto 8000

---

## 🧷 4. Socket TCP en C

**Cliente y Servidor TCP usando sockets BSD en C**

- `cliente.c`: Conecta al servidor y recibe un mensaje.
- `servidor.c`: Acepta conexiones y envía mensajes de bienvenida.

**Flujo básico:**
1. Crear socket
2. Establecer conexión
3. Enviar/Recibir mensaje

---

## 📢 5. Socket Multicast (UDP)

**Modelo Publisher-Subscriber Multicast en Python**

- `emisor.py`: Envía mensajes a un grupo multicast.
- `receptor.py`: Escucha mensajes del grupo.
- `constantes.py`: Define dirección y puerto compartidos.

**Ventajas:** Comunicación uno-a-muchos, baja latencia, sin conexión directa.

---

## 🤝 6. Socket P2P (UDP)

**Comunicación entre pares usando UDP (Python)**

- `cliente_p2p.py`: Envia mensajes a otro peer.
- `servidor_p2p.py`: Recibe y responde interactivamente.

**Características:**
- Comunicación directa sin servidor
- Flujo interactivo bidireccional

---

## 🌐 7. Socket UDP en C

**Implementación básica de cliente-servidor UDP**

- `cliente_udp.c`: Envía mensaje al servidor (localhost:12345).
- `servidor_udp.c`: Escucha en puerto 12345 y muestra mensajes recibidos.

**Modelo sin conexión:** Utiliza `sendto()` y `recvfrom()`.

---

## 📁 Organización

distributed-communication-models/
├── pubsub_kafka_mysql/
├── rpc_xml/
├── rmi_xmlrpc/
├── socket_tcp_c/
├── socket_multicast_udp/
├── socket_p2p_udp/
├── socket_udp_basico_c/
└── README.md

---

## 🧪 Requisitos

- Python 3.x
- MySQL
- Kafka
- gcc (para módulos en C)

