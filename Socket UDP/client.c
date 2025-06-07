/*
Cliente UDP Básico en C
-----------------------------

Este módulo implementa un cliente UDP simple que envía un mensaje "hello from client"
a un servidor local en el puerto 12345. Usa sockets BSD para la comunicación.

Características Clave:
-----------------------------
- Crea un socket UDP (SOCK_DGRAM)
- Configura dirección del servidor (localhost:12345)
- Envía un mensaje de prueba
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
	    
	char * hello = "hello from client";				// Mensaje fijo que se enviará al servidor
	struct sockaddr_in servaddr = {0};				// Estructura para la dirección del servidor
	
	// 1. Creación del socket UDP
	int sockfd = socket(AF_INET, SOCK_DGRAM, 0);	
	if(sockfd == -1){
		perror("failed to create socket");
		exit(EXIT_FAILURE);
	}
	
	// 2. Configuración de la dirección del servidor
	servaddr.sin_family = AF_INET;					// Familia IPv4
	servaddr.sin_port = htons(12345);				// Puerto 12345 (convertido a network byte order)
	servaddr.sin_addr.s_addr = INADDR_ANY;			// Usa la dirección local
    
	// 3. Envío del mensaje al servidor	
	int len = sendto(sockfd, (const char *)hello, strlen(hello),
		0, (const struct sockaddr *)&servaddr, sizeof(servaddr));

	if(len ==-1){
		perror("failed to send");
	}

    // 4. Cierre del socket
	close(sockfd);
	
    return 0;
}