"""
Servidor XML-RPC para Conversión de Unidades
--------------------------------------------

Implementa un servidor de Llamada a Procedimiento Remoto (RPC) usando XML-RPC.
Expone el método 'convertir' como procedimiento remoto accesible vía HTTP.

Mecanismo RPC:
- Protocolo: XML-RPC (RFC 3529)
- Transporte: HTTP en puerto 8000
- Serialización: XML para parámetros y respuestas
"""

from xmlrpc.server import SimpleXMLRPCServer


def convertir(valor, unit_origen, unit_destino):
    """
    Procedimiento remoto para conversión de unidades
    
    Parámetros:
    - valor: Número a convertir (serializado como XML-RPC double)
    - unit_origen: Unidad origen (serializada como string)
    - unit_destino: Unidad destino (serializada como string)
    
    Retorno:
    - Resultado (serializado como XML-RPC double)
    - Mensaje error (serializado como string)
    """
    # 1. Factores de conversión (lógica local)
    factor_de_conversion = {
        "pulgadas": 2.54,
        "pies": 30.48,
        "yardas": 91.44,
        "millas": 160934.4
    }

    # 2. Cálculo de conversión
    valor_convertido = valor * factor_de_conversion.get(unit_origen, 1)

    unidades = {
        "cm": valor_convertido,
        "m": valor_convertido / 100,
        "km": valor_convertido / 100000
    }

    # 3. Retorno de resultado (serializado automáticamente a XML)
    resultado = unidades.get(unit_destino)

    if resultado is None:
        return "Unidad de medida no válida.\n"
    else:
        return resultado

def main():

    """
    Configuración del servidor RPC
    
    Inicia servidor y registra procedimientos remotos
    """

    try:
        # 1. Inicialización del servidor RPC
        server = SimpleXMLRPCServer(("localhost", 8000))

        # 2. Registro del procedimiento remoto
        server.register_function(convertir, "convertir")

        # 3. Bucle infinito de atención
        print("Servidor en espera de conexiones...\n")
        server.serve_forever()

    # Interrumpe el bucle
    except KeyboardInterrupt:
        print("Cerrando servidor...")

main()





