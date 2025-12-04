import socket
import sys
import os

# --- BLOQUE DE BÚSQUEDA AUTOMÁTICA ---
# Esto intenta encontrar tu aplicación sin que tengas que editar el código
try:
    # Intenta importar si tu archivo se llama app.py
    from app import app
    print("✅ Archivo 'app.py' encontrado.")
except ImportError:
    try:
        # Si no, intenta importar si se llama main.py
        from main import app
        print("✅ Archivo 'main.py' encontrado.")
    except ImportError:
        print("\n❌ ERROR: No encuentro tu archivo principal.")
        print("Asegúrate de que este script (run_ipad.py) esté en la misma carpeta")
        print("que tu archivo 'app.py' o 'main.py'.")
        sys.exit(1)

def obtener_ip_local():
    """Detecta la IP de tu Mac en el Wi-Fi"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Se conecta brevemente a Google DNS para ver qué IP usa tu tarjeta de red
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        ip = "127.0.0.1"
    return ip

if __name__ == '__main__':
    mi_ip = obtener_ip_local()
    puerto = 5000
    
    print("\n" + "═"*50)
    print(" 🚀 SERVIDOR LISTO PARA IPAD")
    print("═"*50)
    print(f" 1. En tu Mac, la web sigue en:  http://127.0.0.1:{puerto}")
    print(f" 2. En tu iPad, escribe esto:    http://{mi_ip}:{puerto}")
    print("═"*50 + "\n")

    # host='0.0.0.0' abre la puerta a la red
    app.run(host='0.0.0.0', port=puerto, debug=True)