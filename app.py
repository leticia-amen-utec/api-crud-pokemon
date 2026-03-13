from flask import Flask, jsonify, request


app = Flask(__name__)

# Lista en memoria donde guardamos los Pokemon mientras la app esta corriendo.
pokemons = [
    {
        "id": 1,
        "nombre": "Pikachu",
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "caracteristicas": {
            "peso": 6.0,
            "altura": 0.4,
            "fuerza": 55,
            "edad": 5,
        },
        "habilidades": ["Impactrueno", "Cola ferrea"],
        "tipo": "Electrico",
        "habitat": "Bosques",
    }
]


def buscar_pokemon(pokemon_id):
    # Recorre la lista y devuelve el Pokemon que tenga ese id.
    for pokemon in pokemons:
        if pokemon["id"] == pokemon_id:
            return pokemon
    return None


@app.route("/")
def inicio():
    # Ruta simple para comprobar que la API esta funcionando.
    return jsonify({"mensaje": "API CRUD de Pokemon funcionando"})


@app.route("/pokemons", methods=["GET"])
def obtener_pokemons():
    # Devuelve todos los Pokemon guardados.
    return jsonify(pokemons)


@app.route("/pokemons/<int:pokemon_id>", methods=["GET"])
def obtener_pokemon(pokemon_id):
    # Busca un Pokemon por id.
    pokemon = buscar_pokemon(pokemon_id)

    if pokemon is None:
        return jsonify({"error": "Pokemon no encontrado"}), 404

    return jsonify(pokemon)


@app.route("/pokemons", methods=["POST"])
def crear_pokemon():
    # Lee los datos JSON enviados en el body del request.
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debes enviar datos en formato JSON"}), 400

    # Crea un nuevo Pokemon usando los datos recibidos.
    nuevo_pokemon = {
        "id": len(pokemons) + 1,
        "nombre": datos.get("nombre", ""),
        "imagen": datos.get("imagen", ""),
        "caracteristicas": {
            "peso": datos.get("caracteristicas", {}).get("peso", 0.0),
            "altura": datos.get("caracteristicas", {}).get("altura", 0.0),
            "fuerza": datos.get("caracteristicas", {}).get("fuerza", 0),
            "edad": datos.get("caracteristicas", {}).get("edad", 0),
        },
        "habilidades": datos.get("habilidades", []),
        "tipo": datos.get("tipo", ""),
        "habitat": datos.get("habitat", ""),
    }

    # Guarda el nuevo Pokemon en la lista.
    pokemons.append(nuevo_pokemon)
    return jsonify(nuevo_pokemon), 201


@app.route("/pokemons/<int:pokemon_id>", methods=["PUT"])
def actualizar_pokemon(pokemon_id):
    # Primero buscamos el Pokemon que se quiere editar.
    pokemon = buscar_pokemon(pokemon_id)

    if pokemon is None:
        return jsonify({"error": "Pokemon no encontrado"}), 404

    # Obtiene los nuevos datos enviados por el usuario.
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debes enviar datos en formato JSON"}), 400

    # Actualiza solo los campos que llegaron en el JSON.
    pokemon["nombre"] = datos.get("nombre", pokemon["nombre"])
    pokemon["imagen"] = datos.get("imagen", pokemon["imagen"])
    pokemon["caracteristicas"]["peso"] = datos.get("caracteristicas", {}).get(
        "peso", pokemon["caracteristicas"]["peso"]
    )
    pokemon["caracteristicas"]["altura"] = datos.get("caracteristicas", {}).get(
        "altura", pokemon["caracteristicas"]["altura"]
    )
    pokemon["caracteristicas"]["fuerza"] = datos.get("caracteristicas", {}).get(
        "fuerza", pokemon["caracteristicas"]["fuerza"]
    )
    pokemon["caracteristicas"]["edad"] = datos.get("caracteristicas", {}).get(
        "edad", pokemon["caracteristicas"]["edad"]
    )
    pokemon["habilidades"] = datos.get("habilidades", pokemon["habilidades"])
    pokemon["tipo"] = datos.get("tipo", pokemon["tipo"])
    pokemon["habitat"] = datos.get("habitat", pokemon["habitat"])

    return jsonify(pokemon)


@app.route("/pokemons/<int:pokemon_id>", methods=["DELETE"])
def eliminar_pokemon(pokemon_id):
    # Busca el Pokemon que se quiere eliminar.
    pokemon = buscar_pokemon(pokemon_id)

    if pokemon is None:
        return jsonify({"error": "Pokemon no encontrado"}), 404

    # Lo elimina de la lista en memoria.
    pokemons.remove(pokemon)
    return jsonify({"mensaje": "Pokemon eliminado correctamente"})


if __name__ == "__main__":
    # Inicia el servidor local en modo debug.
    app.run(debug=True)
