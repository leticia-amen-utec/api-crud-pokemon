# Mini Proyecto en Python: API CRUD de Pokemon

API CRUD simple hecha con Flask para gestionar Pokemon en memoria.

## Requisitos

- Python 3
- Flask

## Instalacion

```bash
pip install -r requirements.txt
```

Si prefieres instalar Flask directamente:

```bash
pip install flask
```

## Como correr la API

```bash
python app.py
```

La API queda disponible en:

```bash
http://127.0.0.1:5000
```

## Rutas

### Obtener todos los Pokemon

```http
GET /pokemons
```

### Obtener un Pokemon por ID

```http
GET /pokemons/1
```

### Crear un Pokemon

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
  "habitat": "Montñas"
}
```

### Actualizar un Pokemon

```http
PUT /pokemons/1
Content-Type: application/json
```

### Eliminar un Pokemon

```http
DELETE /pokemons/1
```

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
