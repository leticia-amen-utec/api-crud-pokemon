# Mini Proyecto en Python: API CRUD de Pokémon

API CRUD simple hecha con Flask para gestionar Pokémon en memoria.

## Requisitos

- Python 3
- Flask

## Instalación

```bash
pip install -r requirements.txt
```

Si prefieres instalar Flask directamente:

```bash
pip install flask
```

## Cómo correr la API

```bash
python app.py
```

La API queda disponible en:

```bash
http://127.0.0.1:5000
```

## Rutas

### Obtener todos los Pokémon

```http
GET /pokemons
```

### Obtener un Pokémon por ID

```http
GET /pokemons/1
```

### Crear un Pokémon

```http
POST /pokemons
Content-Type: application/json
```

Ejemplo de body:

```json
{
  "nombre": "Charmander",
  "imagen": "https://ejemplo.com/charmander.png",
  "caracteristicas": {
    "peso": 8.5,
    "altura": 0.6,
    "fuerza": 52,
    "edad": 4
  },
  "habilidades": ["Ascuas", "Lanzallamas"],
  "tipo": "Fuego",
  "habitat": "Montañas"
}
```

### Actualizar un Pokémon

```http
PUT /pokemons/1
Content-Type: application/json
```

### Eliminar un Pokémon

```http
DELETE /pokemons/1
```

## Cómo probar la API

1. Instala las dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecuta la aplicación:

```bash
python app.py
```

3. Abre otra terminal y prueba las rutas.

### Probar en el navegador

Puedes abrir estas rutas en el navegador:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/pokemons`
- `http://127.0.0.1:5000/pokemons/1`

### Probar con Postman

1. Abre Postman.
2. Crea una nueva request.
3. Usa la URL base:

```text
http://127.0.0.1:5000
```

4. Prueba estas rutas:

- `GET /pokemons`
- `GET /pokemons/1`
- `POST /pokemons`
- `PUT /pokemons/1`
- `DELETE /pokemons/1`

### Crear un Pokémon en Postman

- Método: `POST`
- URL: `http://127.0.0.1:5000/pokemons`
- En `Body`, elegir `raw`
- Seleccionar `JSON`

Body de ejemplo:

```json
{
  "nombre": "Bulbasaur",
  "imagen": "https://ejemplo.com/bulbasaur.png",
  "caracteristicas": {
    "peso": 6.9,
    "altura": 0.7,
    "fuerza": 49,
    "edad": 3
  },
  "habilidades": ["Latigo Cepa", "Placaje"],
  "tipo": "Planta",
  "habitat": "Praderas"
}
```

### Actualizar un Pokémon en Postman

- Método: `PUT`
- URL: `http://127.0.0.1:5000/pokemons/1`
- En `Body`, elegir `raw`
- Seleccionar `JSON`

Body de ejemplo:

```json
{
  "nombre": "Ivysaur",
  "tipo": "Planta/Veneno"
}
```

### Eliminar un Pokémon en Postman

- Método: `DELETE`
- URL: `http://127.0.0.1:5000/pokemons/1`

## Ejemplos con curl

Obtener todos:

```bash
curl http://127.0.0.1:5000/pokemons
```

Crear uno nuevo:

```bash
curl -X POST http://127.0.0.1:5000/pokemons ^
  -H "Content-Type: application/json" ^
  -d "{\"nombre\":\"Bulbasaur\",\"imagen\":\"https://ejemplo.com/bulbasaur.png\",\"caracteristicas\":{\"peso\":6.9,\"altura\":0.7,\"fuerza\":49,\"edad\":3},\"habilidades\":[\"Latigo Cepa\",\"Placaje\"],\"tipo\":\"Planta\",\"habitat\":\"Praderas\"}"
```
