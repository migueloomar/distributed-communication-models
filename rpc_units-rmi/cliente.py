"""
Cliente XML-RPC para Conversión de Unidades
-------------------------------------------

Sistema de Invocación Remota de Métodos (RMI) que permite ejecutar procedimientos
en un servidor remoto mediante el protocolo XML-RPC (RFC 3529).

Mecanismo de Invocación Remota:
-----------------------------
1. Transparencia de ubicación: El método 'convertir' se ejecuta en el servidor pero
   se invoca como si fuera local (proxy.convertir())
2. Serialización XML: Los parámetros y resultados se convierten automáticamente a XML
3. Comunicación cliente-servidor:
   - Cliente: Genera solicitudes RPC (Stub)
   - Servidor: Procesa solicitudes (Skeleton)
4. Modelo síncrono: El cliente espera la respuesta del servidor

Detalles Técnicos:
-----------------
- Protocolo: XML sobre HTTP
- Puerto: 8000
- Método remoto: convertir(valor, unidad_origen, unidad_destino)
- Tipos soportados: float, string
"""

import xmlrpc.client

def main():
    """
    Implementación del cliente RMI (Remote Method Invocation)
    
    Proceso de Invocación Remota:
    1. Creación del proxy/stub (ServerProxy)
    2. Captura de parámetros locales
    3. Marshalling automático a XML
    4. Transmisión HTTP
    5. Unmarshalling de respuesta
    6. Presentación de resultados
    """
    # 1. Creación del stub/proxy para invocación remota
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")  # Punto final RPC
    
    while True:
        print("\nMenú de Invocación Remota:")
        print("1. Invocar método remoto 'convertir'")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                # 2. Preparación de parámetros para invocación remota
                valor = float(input("Valor a convertir: "))
                unit_origen = input("Unidad origen (pulgadas/pies/yardas/millas): ").lower()
                unit_destino = input("Unidad destino (cm/m/km): ").lower()
                
                # 3. Validación local antes de invocación remota
                if unit_origen not in {"pulgadas", "pies", "yardas", "millas"}:
                    print("Error: Unidad origen no soportada")
                    continue
                    
                if unit_destino not in {"cm", "m", "km"}:
                    print("Error: Unidad destino no soportada")
                    continue
                
                # 4. Invocación remota propiamente dicha
                resultado = proxy.convertir(valor, unit_origen, unit_destino)
                
                # 5. Procesamiento de respuesta remota
                print(f"\nResultado remoto: {resultado}")
                
            except ValueError:
                print("Error: Valor numérico inválido")
            except xmlrpc.client.Fault as err:
                print(f"Error en invocación remota: {err.faultString}")
            except ConnectionError:
                print("Error: No se pudo conectar al servidor remoto")
                
        elif opcion == "2":
            print("Terminando sesión RMI...")
            break
            
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()