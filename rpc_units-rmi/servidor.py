"""
Servidor RMI para Conversión de Unidades
----------------------------------------

Implementa un servidor de Invocación Remota de Métodos (RMI) usando XML-RPC.
Expone métodos remotos para conversión de unidades accesibles desde clientes.

Arquitectura RMI:
-----------------
1. Esqueleto (Skeleton): Recibe y despacha llamadas remotas
2. Objeto Remoto: Implementa la lógica real (convertir)
3. Marshalling: Serializa/deserializa parámetros (XML)
4. Registry: Registra métodos disponibles (convertir)

Protocolo:
---------
- XML-RPC sobre HTTP (RFC 3529)
- Puerto: 8000
- Endpoint: http://localhost:8000/
"""

from xmlrpc.server import SimpleXMLRPCServer

def convertir(valor, unit_origen, unit_destino):
    """
    Método remoto invocable desde clientes
    
    Proceso RMI:
    1. Cliente invoca proxy.convertir()
    2. Solicitud se serializa a XML
    3. Servidor recibe y deserializa
    4. Ejecuta esta función
    5. Resultado se serializa a XML
    6. Cliente recibe y deserializa
    
    Parámetros (serializados como XML-RPC types):
    - valor: double
    - unit_origen: string
    - unit_destino: string
    
    Retorno:
    - double: Valor convertido
    - string: Mensaje error (si aplica)
    """
    # Factores de conversión (implementación real del método remoto)
    factores = {
        "pulgadas": 2.54,       # Factores de conversión a cm
        "pies": 30.48,
        "yardas": 91.44,
        "millas": 160934.4
    }

    try:
        # 1. Conversión a centímetros (unidad intermedia)
        valor_cm = valor * factores[unit_origen.lower()]
        
        # 2. Conversión a unidad destino
        conversiones = {
            "cm": valor_cm,
            "m": valor_cm / 100,
            "km": valor_cm / 100000
        }
        
        return conversiones[unit_destino.lower()]
        
    except KeyError as e:
        return f"Error RMI: Unidad no soportada ({str(e)})"

def main():
    """
    Configuración del servidor RMI
    
    Componentes:
    1. SimpleXMLRPCServer: Esqueleto (Skeleton)
    2. register_function: Registry de métodos
    3. serve_forever: Bucle principal
    """
    try:
        # 1. Inicialización del esqueleto (Skeleton)
        with SimpleXMLRPCServer(("localhost", 8000)) as server:
            
            # 2. Registro del método remoto (Registry)
            server.register_function(convertir, "convertir")
            print("Servidor RMI listo en http://localhost:8000")
            print("Método remoto registrado: convertir(valor, unidad_origen, unidad_destino)")
            
            # 3. Bucle principal de atención
            server.serve_forever()  # Escucha llamadas RMI
            
    except KeyboardInterrupt:
        print("\nServidor RMI deteniéndose...")
    except Exception as e:
        print(f"Error en servidor RMI: {str(e)}")

if __name__ == "__main__":
    main()