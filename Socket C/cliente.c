/*
Práctica de Sockets TCP - Cliente/Servidor
------------------------------------------

Implementación básica de comunicación cliente-servidor usando sockets TCP en C.
El servidor envía un mensaje de bienvenida a cada cliente que se conecta.

Estructura:
- cliente.c: Programa cliente que recibe mensajes
- servidor.c: Programa servidor que acepta conexiones

Función principal del cliente
-----------------------------
Parámetros:
- argv[1]: Dirección IP del servidor
- argv[2]: Puerto de conexión

Flujo:
1. Verifica parámetros
2. Obtiene información del host
3. Crea socket TCP
4. Establece conexión
5. Recibe mensaje
6. Cierra conexión
*/

#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 
#include <unistd.h>

int main(int argc, char *argv[]){
    if(argc>2){
        // def de variables
        char *ip;
        int fd, numbytes, puerto;
        char buf[100];
        puerto = atoi(argv[2]);
        ip=argv[1];

        // 1. Resolución DNS
        struct hostent *he; 
        struct sockaddr_in server;

        if((he=gethostbyname(ip))==NULL){
            printf("gethostbyname() error\n");
            exit(-1);
        }
        
        // 2. Creación de socket TCP
        if ((fd=socket(AF_INET, SOCK_STREAM, 0)) == -1){
            printf("socket() error\n");
            exit(-1);
        }

        // 3. Configuración de conexión
        server.sin_family = AF_INET;
        server.sin_port = htons(puerto);
        server.sin_addr = *((struct in_addr *) he->h_addr);
        bzero(&(server.sin_zero),8);

        // 4. Conexión al servidor
        if(connect(fd, (struct sockaddr *)&server, sizeof(struct sockaddr))==-1){
            printf("connect() error\n");
            exit(-1);
        }

        // 5. Recepción de mensaje
        if((numbytes = recv(fd, buf, 100, 0)) == -1){
            printf("Error en recv()\n");
            exit(-1);
        }

        buf[numbytes]='\0';
        printf("Mensaje del servidor: %s\n", buf);
        // 6. Cierre de conexión
        close(fd);  
    }
    else{
        printf("No se ingreso la ip y puerto por parametro\n");
    }  
}
