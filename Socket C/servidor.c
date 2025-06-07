/*
Práctica de Sockets TCP - Cliente/Servidor
------------------------------------------

Implementación básica de comunicación cliente-servidor usando sockets TCP en C.
El servidor envía un mensaje de bienvenida a cada cliente que se conecta.

Estructura:
- cliente.c: Programa cliente que recibe mensajes
- servidor.c: Programa servidor que acepta conexiones

Función principal del servidor
-------------------------------
Parámetros:
- argv[1]: Puerto de escucha

Flujo:
1. Verifica parámetros
2. Crea socket TCP
3. Configura dirección
4. Enlaza socket
5. Escucha conexiones
6. Acepta clientes (loop)
7. Envía mensaje
8. Cierra conexiones
*/

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>


int main(int argc, char **argv){
    if(argc > 1){
        int fd, fd2, longitud_cliente, puerto;
        puerto = atoi(argv[1]);

        struct sockaddr_in server;
        struct sockaddr_in client;

        // 1. Configuración del servidor
        server.sin_family = AF_INET;            // Familia TCP/IP
        server.sin_port = htons(puerto);        // Puerto
        server.sin_addr.s_addr = INADDR_ANY;    // Cualquier cliente puede conectarse
        bzero(&(server.sin_zero),8);            // Función que rellena con 0's

        // 2. Creación de socket
        if((fd=socket(AF_INET, SOCK_STREAM, 0))<0){
            perror("Error de apertura de socket");
            exit(-1);
        }

        // 3. Enlace (bind) del socket
        if(bind(fd,(struct sockaddr*)&server, sizeof(struct sockaddr))==-1){
            printf("error en bind()\n");
            exit(-1);
        }

        // 4. Poner en modo escucha
        if(listen(fd,5) == -1){
            printf("Error en listen()\n");
            exit(-1);
        }

        // 5. Bucle principal de conexiones
        while(1){
            longitud_cliente = sizeof(struct sockaddr_in);

            // 6. Aceptar nueva conexión
            if ((fd2 = accept(fd,(struct sockaddr *)&client,&longitud_cliente))==-1){
                printf("Error en accept()\n");
                exit(-1);
            }

            // 7. Enviar mensaje de bienvenida
            send(fd2, "Bienvenido a mi servidor. \n",26,0);

            // 8. Cerrar conexión con cliente
            close(fd2); 
        }
        close(fd); // cierra fd (servidor)
    }
    else{
        printf("No se ingreso el puerto por parametro\n");
    }
    return 0;
}
