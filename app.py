from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos en memoria
usuarios = []

# Ruta de inicio (home)
@app.route('/')
def home():
    return "¡Servicio Web Flask desplegado con éxito!"

# CREATE: Crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": datos['nombre'],
        "edad": datos['edad']
    }
    usuarios.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario creado", "usuario": nuevo_usuario}), 201

# READ: Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios), 200

# READ: Obtener un usuario por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        return jsonify(usuario), 200
    return jsonify({"mensaje": "Usuario no encontrado"}), 404

# UPDATE: Actualizar un usuario por ID
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    datos = request.get_json()
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        usuario.update({
            "nombre": datos.get('nombre', usuario['nombre']),
            "edad": datos.get('edad', usuario['edad'])
        })
        return jsonify({"mensaje": "Usuario actualizado", "usuario": usuario}), 200
    return jsonify({"mensaje": "Usuario no encontrado"}), 404

# DELETE: Eliminar un usuario por ID
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = next((u for u in usuarios if u['id'] == id), None)
    if usuario:
        usuarios.remove(usuario)
        return jsonify({"mensaje": "Usuario eliminado"}), 200
    return jsonify({"mensaje": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
