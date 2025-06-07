/*
Servidor UDP Básico en C
-----------------------------

Este módulo implementa un servidor UDP simple que recibe mensajes en el puerto 12345.
Muestra los mensajes recibidos en la consola y finaliza la conexión.

Características Clave:
-----------------------------
- Crea un socket UDP (SOCK_DGRAM)
- Enlaza (bind) el socket al puerto 12345
- Recibe mensajes de hasta 50 bytes
- Muestra los mensajes en la salida estándar
- Manejo básico de errores

Tecnologías:
-----------------------------
- Sockets BSD (sys/socket.h)
- Protocolo UDP (no orientado a conexión)
- Network Byte Order (htons)
*/

#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
#include <netinet/in.h> 

int main(){
	char buffer[50] = {0};					    // Buffer para almacenar los mensajes recibidos
	struct sockaddr_in servaddr = {0};     		// Estructura para la dirección del servidor

	// 1. Creación del socket UDP
	int sockfd = socket(AF_INET, SOCK_DGRAM, 0);
	if(sockfd == -1){
		perror("failed to create socket");
		exit(EXIT_FAILURE);
	}

	// 2. Configuración de la dirección del servidor
	servaddr.sin_family = AF_INET;				// Familia IPv4
	servaddr.sin_port = htons(12345);			// Puerto 12345 (network byte order)
	servaddr.sin_addr.s_addr = INADDR_ANY;		// Escucha en todas las interfaces

    // 3. Enlace (bind) del socket a la dirección	
	int rc = bind(sockfd, (const struct sockaddr *)&servaddr, 
		sizeof(servaddr));
		
	if(rc == -1){
		perror("failed to bind");
		close(sockfd);
		exit(EXIT_FAILURE);
	}

	// 4. Recepción de mensajes
	socklen_t len = 0;
	int n = recvfrom(sockfd, (char *)buffer, 50, MSG_WAITALL,
		0, &len);

    // 5. Procesamiento del mensaje recibido
	buffer[n] = '\n';
	printf("%s", buffer);
	
    // 6. Cierre del socket
	close(sockfd);
    return 0;
}