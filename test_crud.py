import requests

URL = "http://127.0.0.1:5000"

def crear_usuario(nombre, edad):
    response = requests.post(f"{URL}/usuarios", json={"nombre": nombre, "edad": edad})
    print("Crear usuario:", response.json())

def obtener_usuarios():
    response = requests.get(f"{URL}/usuarios")
    print("Obtener todos los usuarios:", response.json())

def obtener_usuario(id):
    response = requests.get(f"{URL}/usuarios/{id}")
    print(f"Obtener usuario {id}:", response.json())

def actualizar_usuario(id, nombre, edad):
    response = requests.put(f"{URL}/usuarios/{id}", json={"nombre": nombre, "edad": edad})
    print(f"Actualizar usuario {id}:", response.json())

def eliminar_usuario(id):
    response = requests.delete(f"{URL}/usuarios/{id}")
    print(f"Eliminar usuario {id}:", response.json())

if __name__ == "__main__":
    # Probar operaciones CRUD
    crear_usuario("Juan", 25)
    crear_usuario("Ana", 30)
    obtener_usuarios()
    obtener_usuario(1)
    actualizar_usuario(1, "Juan Carlos", 26)
    eliminar_usuario(2)
    obtener_usuarios()
