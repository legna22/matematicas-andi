# --- PEGAR ESTO AL FINAL DE TU ARCHIVO PRINCIPAL ---
import socket

def obtener_ip_local():
    """Detecta la IP real de tu Mac en la red Wi-Fi"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No se envía nada realmente, solo se conecta para ver qué IP usa el sistema
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        ip = "127.0.0.1"
    return ip

if __name__ == '__main__':
    # Obtener IP
    mi_ip = obtener_ip_local()
    puerto = 5000
    
    # Imprimir mensaje visual para el usuario
    print("\n" + "═"*60)
    print(" 📱 MODO IPAD ACTIVADO")
    print("═"*60)
    print(f" 1. Asegúrate que tu iPad esté en el mismo Wi-Fi.")
    print(f" 2. Abre Safari en el iPad.")
    print(f" 3. Escribe exactamente esta dirección:")
    print(f"\n    👉  http://{mi_ip}:{puerto}  👈\n")
    print("═"*60 + "\n")

    # host='0.0.0.0' es lo que permite que otros entren
    app.run(host='0.0.0.0', port=puerto, debug=True)