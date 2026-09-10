# Visualizador de árboles binarios

Proyecto educativo en Flask para construir, evaluar y visualizar dos estructuras:

1. **Árbol de expresión** — convierte una fórmula infija (`3 + 5 * 2`) en un árbol binario, la evalúa y la dibuja.
2. **Árbol AVL** — árbol binario de búsqueda autoequilibrado: insertar, buscar, eliminar y ver cómo quedan las rotaciones.

La interfaz usa plantillas Jinja y **D3.js** para el dibujo. La lógica de los árboles vive en Python, no en el navegador.

## Requisitos

- Python 3.10 o superior (el código usa uniones de tipos `str | int`).
- Un entorno virtual (recomendado).

## Cómo ejecutarlo

En PowerShell, desde la raíz del repositorio:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

En Linux o macOS:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abre [http://127.0.0.1:5000](http://127.0.0.1:5000). Para detener el servidor: `Ctrl+C`.

| Pantalla | URL |
|---|---|
| Inicio | http://127.0.0.1:5000/ |
| Árbol de expresión | http://127.0.0.1:5000/expresion |
| Árbol AVL | http://127.0.0.1:5000/busqueda |

Pruebas rápidas:

- Expresión `3 + 5 * 2` → resultado **13** (el `*` queda debajo del `+`).
- AVL: insertar `10`, `20`, `30` → la raíz queda en **20** (rotación RR).

## Estructura del proyecto

```text
app.py                          # Arranque: create_app() + servidor de desarrollo
requirements.txt
app/
  __init__.py                   # Fábrica Flask y registro de blueprints
  controllers/                  # Rutas HTTP
    expresion_controller.py
    avl_controller.py
  models/
    nodo.py                     # Nodo compartido (izquierdo / derecho / altura)
    ABExpresiones/
      construir_arbol.py        # Parser descendente recursivo
      arbol_expresion.py        # Recorridos y evaluación
    ABB/
      ABB_AVL.py                # ABB + rotaciones AVL
  templates/                    # HTML (Jinja)
  static/
    css/style.css
    js/arbol_render.js          # Dibujo con D3
docs/                           # Documentación detallada
```

Flujo general:

```text
Navegador  →  Flask (blueprint)  →  modelo (Parser / ArbolAVL)
                                    ↓
                                 JSON { arbol, ... }
                                    ↓
                               D3.js dibuja el árbol
```

## Documentación

| Documento | Contenido |
|---|---|
| [docs/README.md](docs/README.md) | Índice de la carpeta `docs` |
| [docs/uso.md](docs/uso.md) | Cómo usar las pantallas y qué se acepta |
| [docs/arquitectura.md](docs/arquitectura.md) | Capas, archivos y responsabilidades |
| [docs/arbol-expresion.md](docs/arbol-expresion.md) | Parser, precedencia, evaluación y recorridos |
| [docs/arbol-avl.md](docs/arbol-avl.md) | BST, factor de balance y rotaciones |
| [docs/api.md](docs/api.md) | Rutas HTTP y formato JSON |

## Limitaciones

- Operadores de expresión: `+`, `-`, `*`, `/` y paréntesis. No hay potencia (`^`) ni menos unario (`-3`); usa `0-3`.
- El AVL no admite duplicados (la segunda inserción se ignora).
- El árbol AVL se guarda en una variable global de proceso: todos los usuarios de esa instancia ven el mismo árbol, y se pierde al reiniciar el servidor.
- El servidor de `app.py` es de desarrollo (`debug=True`), no de producción.

## Licencia

Proyecto académico. Úsalo con fines educativos.
