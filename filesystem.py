import os

def list_files(path: str = ".") -> None:
    """Lista archivos y carpetas en la ruta dada."""
    if not os.path.exists(path):
        print(f"Uy.... La ruta {path} no existe")
        return

    print(f"\nContenido de: {os.path.abspath(path)}\n")
    for entry in os.listdir(path):
        full = os.path.join(path, entry)
        if os.path.isdir(full):
            print(f"[DIR ] {entry}")
        else:
            print(f"[FILE] {entry}")

def read_file(filepath: str) -> None:
    """Lee un archivo de texto y muestra su contenido."""
    if not os.path.exists(filepath):
        print(f"Uy.... El archivo {filepath} no existe")
        return
    if os.path.isdir(filepath):
        print(f"{filepath} es un directorio, no un archivo")
        return

    print(f"\nContenido de: {filepath}\n")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            print(f.read())
    except Exception as e:
        print(f"Error al leer el archivo: {e}")


if __name__ == "__main__":
    # 1. Listar la carpeta actual
    list_files("./mini-mcp-server")

    # 2. Intentar leer un archivo llamado "ejemplo.txt"
    read_file("./mini-mcp-server/ejemplo.txt")
