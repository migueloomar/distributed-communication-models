"""
Cliente XML-RPC para Conversión de Unidades
-------------------------------------------

Implementa un cliente para el sistema de Llamada a Procedimiento Remoto (RPC) usando XML-RPC.
Permite invocar métodos remotos en un servidor para conversión de unidades de longitud.

Mecanismo RPC:
- Protocolo: XML-RPC (XML sobre HTTP)
- Serialización: Datos convertidos a XML para transmisión
- Transparencia: El método remoto se ejecuta como si fuera local
"""

import xmlrpc.client

def main():

    """
    Función principal del cliente RPC
    
    Establece conexión con servidor remoto y provee interfaz interactiva
    para invocar el procedimiento remoto 'convertir'.
    """
    
    # 1. Creación del proxy RPC (stub del servidor)
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/") # URI del endpoint RPC

    # 2. Bucle principal de interacción
    while True:
        print("\nMenú:")
        print("1. Convertir longitud")  # Opción para invocar RPC
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:

                # 3. Captura de parámetros para el procedimiento remoto
                valor = float(input("Ingrese el valor (10): "))
                unit_origen = input("Ingrese la unidad de medida de origen (pulgadas, pies, yardas, millas): ")
                
                if unit_origen not in {"pulgadas", "pies", "yardas", "millas"}:
                    print("Unidad de medida de origen no válida.\n")
                    continue
                unit_destino = input("Ingrese la unidad de medida de destino (cm, m, km): ")
                
                if unit_destino not in {"cm", "m", "km"}:
                    print("Unidad de medida de destino no válida.\n")
                    continue

                # 4. Invocación remota (transparente al usuario)
                resultado = proxy.convertir(valor, unit_origen, unit_destino)
                print("El resultado de la operación es:", resultado)
            except ValueError:
                print("Por favor, ingrese un valor numérico.\n")
        elif opcion == "2":
            print("Saliendo del cliente...\n")
            break
        else:
            print("Opción no válida.\n")
main()




