import os
import subprocess
import sys
import json

# --- CONFIGURACIÓN ---
PROJECT_DIR = os.getcwd() # Directorio actual
VENV_DIR = os.path.join(PROJECT_DIR, "venv")
VSCODE_DIR = os.path.join(PROJECT_DIR, ".vscode")

# Rutas específicas para Mac/Linux
VENV_PYTHON = os.path.join(VENV_DIR, "bin", "python")
VENV_PIP = os.path.join(VENV_DIR, "bin", "pip")

def print_step(emoji, message):
    print(f"\n{emoji} {message}...")

def run_command(command, cwd=None, env=None, capture_output=False):
    try:
        if capture_output:
            return subprocess.run(command, cwd=cwd, env=env, check=True, capture_output=True)
        else:
            return subprocess.run(command, cwd=cwd, env=env, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando: {' '.join(command)}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ No se encontró el comando: {command[0]}")
        return None

def main():
    print(f"--- 🛠️ CONFIGURADOR DE ENTORNO VS CODE ---")

    # 1. Crear Entorno Virtual (venv)
    if not os.path.exists(VENV_DIR):
        print_step("📦", "Creando entorno virtual (venv)")
        subprocess.run([sys.executable, "-m", "venv", "venv"])
    else:
        print_step("✅", "Entorno virtual ya existe")

    # 2. Configurar VS Code automáticamente (.vscode/settings.json)
    # Esto hace que VS Code reconozca el venv automáticamente
    print_step("⚙️", "Configurando Visual Studio Code")
    if not os.path.exists(VSCODE_DIR):
        os.makedirs(VSCODE_DIR)
    
    settings_path = os.path.join(VSCODE_DIR, "settings.json")
    settings = {
        "python.defaultInterpreterPath": VENV_PYTHON,
        "python.terminal.activateEnvironment": True
    }
    
    with open(settings_path, "w") as f:
        json.dump(settings, f, indent=4)
    print("   -> Archivo .vscode/settings.json creado/actualizado.")

    # 3. Instalar Dependencias
    print_step("⬇️", "Instalando librerías")
    if os.path.exists("requirements.txt"):
        run_command([VENV_PIP, "install", "-r", "requirements.txt"])
    else:
        print("⚠️ No se encontró requirements.txt")

    # 4. Abrir Visual Studio Code
    print_step("💻", "Abriendo Visual Studio Code")
    try:
        # El comando 'code .' abre la carpeta actual en VS Code
        run_command(["code", "."], cwd=PROJECT_DIR)
    except:
        print("⚠️ No se pudo abrir VS Code automáticamente.")
        print("   (Asegúrate de tener instalado el comando 'code' en el PATH de Mac)")
        print("   Puedes abrirlo manualmente y ya estará configurado.")

    # 5. Ejecutar el Servidor Flask
    print_step("🚀", "Iniciando Servidor Flask (Modo Desarrollo)")
    print("   Presiona Ctrl+C para detener el servidor.\n")
    
    env_vars = os.environ.copy()
    env_vars["FLASK_ENV"] = "development"
    env_vars["FLASK_DEBUG"] = "1" # Activa Hot Reload

    try:
        subprocess.run([VENV_PYTHON, "app.py"], env=env_vars)
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido.")

if __name__ == "__main__":
    main()