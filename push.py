import os
import subprocess
import sys

# URL de tu nuevo repositorio
REPO_URL = "https://github.com/ddss20/matematicas-and.git"

def ejecutar_comando(comando):
    """Ejecuta un comando de terminal y muestra el resultado."""
    print(f"🔄 Ejecutando: {' '.join(comando)}")
    try:
        resultado = subprocess.run(comando, check=True, text=True, capture_output=True)
        print("✅ Éxito.")
        return True
    except subprocess.CalledProcessError as e:
        # Ignoramos errores de "remote already exists" o cosas menores
        if "remote origin already exists" in e.stderr:
            print("ℹ️  El origen ya existía, actualizando...")
        elif "nothing to commit" in e.stdout:
            print("ℹ️  Nada nuevo que guardar.")
        else:
            print(f"⚠️  Nota: {e.stderr.strip()}")
        return False

def crear_gitignore():
    """Crea el archivo .gitignore si no existe."""
    contenido = """
__pycache__/
*.py[cod]
env/
venv/
.venv/
.VSCode/
*.sqlite3
    """
    if not os.path.exists(".gitignore"):
        with open(".gitignore", "w") as f:
            f.write(contenido.strip())
        print("✅ Archivo .gitignore creado correctamente.")
    else:
        print("ℹ️  El archivo .gitignore ya existía.")

def main():
    print("🚀 INICIANDO SUBIDA AUTOMÁTICA A GITHUB...")
    print("-" * 40)

    # 1. Crear .gitignore para no subir basura
    crear_gitignore()

    # 2. Comandos de Git en orden
    comandos = [
        ["git", "init"],                           # Iniciar repo
        ["git", "add", "."],                       # Agregar todos los archivos
        ["git", "commit", "-m", "Subida automatica del proyecto completo"], # Guardar cambios
        ["git", "branch", "-M", "main"],           # Renombrar rama a main
    ]

    for cmd in comandos:
        ejecutar_comando(cmd)

    # 3. Configurar la URL remota (Truco: Borramos y agregamos para asegurar que sea la nueva)
    print("🔄 Configurando conexión con GitHub...")
    subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
    subprocess.run(["git", "remote", "add", "origin", REPO_URL], check=True)

    # 4. Subir (Push)
    print("-" * 40)
    print("📤 SUBIENDO ARCHIVOS A GITHUB...")
    print("⚠️  ATENCIÓN: Si se abre una ventana o navegador, INICIA SESIÓN.")
    
    try:
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("\n🎉 ¡FELICIDADES! PROYECTO SUBIDO CON ÉXITO.")
        print(f"🔗 Ver aquí: {REPO_URL}")
    except subprocess.CalledProcessError:
        print("\n❌ ERROR AL SUBIR: Es posible que necesites iniciar sesión.")
        print("Intenta ejecutar manualmente en la terminal: git push -u origin main")

if __name__ == "__main__":
    main()