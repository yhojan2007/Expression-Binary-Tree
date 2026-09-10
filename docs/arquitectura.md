# Arquitectura

Aplicación Flask con fábrica (`create_app`), dos blueprints y modelos de árbol independientes. El navegador no implementa el parser ni el AVL: solo envía JSON y pinta la respuesta.

## Capas

```text
templates + static/js     presentación (HTML, CSS, D3)
controllers               HTTP: páginas y APIs JSON
models                    estructuras de datos y algoritmos
```

`app.py` llama a `create_app()` y, si se ejecuta como script, levanta el servidor de desarrollo.

`app/__init__.py` registra:

- `expresion_bp` → `app/controllers/expresion_controller.py`
- `busqueda_bp` → `app/controllers/avl_controller.py` (el archivo se llama AVL; el blueprint se llama `busqueda` para coincidir con `url_for` y las URLs `/busqueda/...`)

La ruta `/` se define en la fábrica y renderiza `index.html`.

## Modelos

Un único `Nodo` (`app/models/nodo.py`) sirve a ambos árboles:

- `valor` — número u operador.
- `izquierdo`, `derecho` — hijos.
- `altura` — usada por el AVL (la expresión no la consulta).
- `to_dict()` — JSON anidado para D3: `{ valor, izquierdo, derecho, es_hoja }`.

**Expresión** (`app/models/ABExpresiones/`):

- `Parser` en `construir_arbol.py` tokeniza y construye el árbol.
- `ArbolExpresion` recorre, evalúa y serializa.

**AVL** (`app/models/ABB/ABB_AVL.py`):

- Inserción y borrado de BST.
- Recálculo de altura, factor de balance y rotaciones.
- Recorridos inorden / preorden / postorden para la API (la vista actual muestra sobre todo altura y nodos).

## Frontend

- `base.html` carga `style.css` y D3 v7 desde CDN.
- `expresion.html` y `AVL.html` hacen `fetch` a las APIs y llaman a `dibujarArbolD3` en `arbol_render.js`.
- D3 convierte `{ izquierdo, derecho }` en una jerarquía (`d3.hierarchy` + `d3.tree`) y dibuja enlaces verticales y círculos.

## Estado

El árbol de expresión **no se persiste**: cada «Construir» parsea de nuevo el texto.

El AVL sí se persiste en el proceso: `arbol_actual` en `avl_controller.py`. Es deliberado para una demo en clase; no es un almacén por usuario ni por sesión.

`SECRET_KEY` está fija en código solo para poder usar `session` en la ruta de expresión (`ultima_expresion`). No es un despliegue seguro.

## Dependencias

Flask y su cadena (Jinja, Werkzeug, etc.) están en `requirements.txt`. D3 no se instala con pip: llega por CDN al cargar la página.
