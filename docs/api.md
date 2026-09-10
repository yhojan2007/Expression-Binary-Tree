# API HTTP

Todas las APIs de datos usan JSON (`Content-Type: application/json`) salvo las páginas HTML. En error, el cuerpo suele ser `{ "error": "mensaje" }` con código **400**, o **404** si se intenta borrar un valor que no está en el AVL.

Base local: `http://127.0.0.1:5000`.

## Páginas

| Método | Ruta | Blueprint | Plantilla |
|---|---|---|---|
| GET | `/` | fábrica Flask | `index.html` |
| GET | `/expresion` | `expresion` | `expresion.html` |
| GET | `/busqueda` | `busqueda` | `AVL.html` |

## Expresión

### `POST /expresion/construir`

Cuerpo:

```json
{ "expresion": "3 + 5 * 2" }
```

Respuesta 200:

```json
{
  "success": true,
  "data": {
    "expresion": "(3+(5*2))",
    "resultado": 13.0,
    "arbol": {
      "valor": "+",
      "es_hoja": false,
      "izquierdo": { "valor": "3", "izquierdo": null, "derecho": null, "es_hoja": true },
      "derecho": {
        "valor": "*",
        "es_hoja": false,
        "izquierdo": { "valor": "5", "izquierdo": null, "derecho": null, "es_hoja": true },
        "derecho": { "valor": "2", "izquierdo": null, "derecho": null, "es_hoja": true }
      }
    }
  }
}
```

Guarda `ultima_expresion` en la sesión Flask (no hace falta para pintar el árbol).

### `POST /expresion/evaluar`

Mismo cuerpo. Respuesta:

```json
{ "success": true, "expresion": "3 + 5 * 2", "resultado": 13.0 }
```

La UI principal usa **construir**, no este endpoint.

## AVL (`/busqueda`)

El árbol se comparte en memoria del proceso.

Números: `7.0` se convierte a `7`; `7.5` se queda decimal.

### `POST /busqueda/insertar`

```json
{ "valor": 10 }
```

Respuesta 200: `{ "success": true, "mensaje": "...", "data": { ... } }`.

`data` incluye `arbol`, `altura`, `total_nodos`, `inorden`, `preorden`, `postorden`.

### `POST /busqueda/buscar`

```json
{ "valor": 20 }
```

```json
{ "success": true, "valor": 20, "encontrado": true }
```

### `POST /busqueda/eliminar`

Si el valor no existe: **404** y `{ "success": false, "mensaje": "..." }`.

Si existe: 200, mensaje y `data` del árbol actualizado.

### `GET /busqueda/estado`

```json
{ "success": true, "data": { "arbol": null, "altura": 0, "total_nodos": 0, "inorden": [], "preorden": [], "postorden": [] } }
```

La página lo llama al cargar para recuperar el árbol si ya había inserciones.

### `POST /busqueda/reiniciar`

Sustituye `arbol_actual` por un `ArbolAVL()` vacío. Cuerpo de petición vacío. Devuelve `data` del árbol vacío.

## Forma del árbol en JSON

Cada nodo:

```json
{
  "valor": "20",
  "izquierdo": null,
  "derecho": null,
  "es_hoja": true
}
```

`valor` siempre va como cadena (así D3 lo pinta igual para números y operadores). `arbol_render.js` toma `izquierdo` y `derecho` como hijos de la jerarquía D3.
