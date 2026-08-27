# Expresiones ABB

Calculadora de expresiones matemáticas basada en un **Árbol Binario de Expresión** (*Expression Binary Tree*), desarrollada en Python.

El programa no se limita a devolver un número: tokeniza la entrada, construye un árbol en memoria, lo recorre, lo convierte entre notaciones y lo evalúa de forma recursiva. No utiliza `eval()`.

---

## Descripción

A partir de una expresión infija como `3 + 5 * 2` o `(10 + 2) * 3`, la aplicación:

1. Tokeniza y valida la cadena.
2. Respeta precedencia y asociatividad de operadores.
3. Construye un árbol binario de expresión.
4. Permite visualizar el árbol y recorrerlo (inorden, preorden, postorden).
5. Convierte entre notación infija, prefija y posfija.
6. Evalúa el resultado recorriendo el árbol de forma recursiva.
7. Informa errores de sintaxis, tokens inválidos y división por cero.

Pipeline interno:

```text
String
  → Tokenizer
  → Tokens
  → Parser
  → Árbol de expresión
  → Recorridos / visualización
  → Evaluator
  → Resultado
```

---

## Objetivo educativo

Proyecto pensado para practicar, con código real, conceptos de estructuras de datos y de Python profesional:

- Programación orientada a objetos y diseño modular.
- Árboles binarios, árboles de expresión y referencias entre objetos.
- Recursividad y recorridos (inorden, preorden, postorden).
- Pila (*stack*), parsing, notación infija / prefija / posfija.
- Precedencia y asociatividad de operadores.
- Manejo de excepciones, type hints, PEP 8 y testing con pytest.
- Git con Conventional Commits.

El desarrollo es **progresivo por fases**. La meta no es solo un programa funcional, sino entender por qué cada pieza existe.

---

## Características

| Área | Qué hace |
| --- | --- |
| Tokenización | Números enteros y decimales, `+ - * /`, paréntesis. |
| Validación | Expresiones mal formadas, tokens inválidos, paréntesis desbalanceados. |
| Parser | Construcción del árbol respetando precedencia (`* /` sobre `+ -`) y paréntesis. |
| Árbol | Nodos operador/número con referencias `left` y `right`. |
| Recorridos | Inorden, preorden y postorden (equivalen a infija, prefija y posfija). |
| Evaluación | Recorrido recursivo de subárboles; división por cero controlada. |
| CLI | Menú para ingresar, convertir, evaluar y mostrar el árbol. |
| Visualización | Representación del árbol en terminal. |

Operadores de la versión básica: `+`, `-`, `*`, `/`.

---

## Arquitectura

`main.py` solo orquesta la CLI. La lógica vive en `src/`:

| Módulo | Responsabilidad |
| --- | --- |
| `node.py` | Nodo del árbol (operador o número, hijos izquierdo y derecho). |
| `tree.py` | Árbol de expresión y recorridos. |
| `parser.py` | Tokenización y construcción del árbol (p. ej. Shunting Yard). |
| `evaluator.py` | Evaluación recursiva. |
| `exceptions.py` | Errores de dominio (`MalformedExpressionError`, `InvalidTokenError`, `DivisionByZeroError`). |

Principio: **una responsabilidad por módulo**. El árbol se construye de verdad en memoria; no se delega el cálculo a `eval()`.

---

## Estructura del proyecto

```text
Expresiones ABB/
├── .gitignore
├── README.md
├── main.py                 # CLI (interacción con el usuario)
├── src/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── node.py
│   ├── tree.py
│   ├── parser.py
│   └── evaluator.py
├── tests/
│   ├── __init__.py
│   ├── test_node.py
│   ├── test_tree.py
│   ├── test_parser.py
│   └── test_evaluator.py
└── docs/
    └── PRD.md
```

---

## Conceptos utilizados

- **Nodo y referencias:** cada `Node` apunta a otros objetos (`left`, `right`) o a `None` (hoja o hijo ausente).
- **Árbol de expresión:** hojas = operandos; nodos internos = operadores.
- **Recorridos recursivos:** el caso `if node is None: return` detiene la bajada; al volver se combina el resultado del subárbol.
- **Precedencia:** `3 + 5 * 2` produce `+` en la raíz y `*` a la derecha, no al revés.
- **Pila / Shunting Yard:** conversión infija → posfija (o construcción directa del árbol) respetando operadores y paréntesis.
- **Evaluación postorden conceptual:** primero subárbol izquierdo, luego derecho, luego la operación del nodo.

Ejemplo de árbol para `3 + 5 * 2`:

```text
        +
       / \
      3   *
         / \
        5   2
```

Recorridos:

```text
Inorden  (infija):   3 + 5 * 2
Preorden (prefija):  + 3 * 5 2
Postorden (posfija): 3 5 2 * +
```

Evaluación: `5 * 2 = 10`, luego `3 + 10 = 13`.

---

## Ejemplos

```text
3 + 5           →  8
3 + 5 * 2       →  13
(3 + 5) * 2     →  16
(10 + 2) * 3    →  36
10 / 2 + 3      →  8
```

Errores que la aplicación debe detectar:

```text
3 + * 5         expresión mal formada
(3 + 5          paréntesis sin cerrar
3 + 5)          paréntesis de más
3 / 0           división por cero
3 + abc         token inválido
3 ++ 5          operadores consecutivos inválidos
```

---

## Instalación

Requisito: **Python 3.11** o superior.

```powershell
cd "e:\Proyectos ED\Expresiones ABB"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pytest ruff
```

En Linux o macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pytest ruff
```

---

## Ejecución

```powershell
python main.py
```

Menú previsto:

```text
====================================
 CALCULADORA - ÁRBOL DE EXPRESIÓN
====================================

1. Ingresar expresión
2. Mostrar expresión infija
3. Mostrar expresión prefija
4. Mostrar expresión posfija
5. Evaluar expresión
6. Mostrar árbol
7. Salir

Seleccione una opción:
```

---

## Tests

```powershell
pytest
```

Cobertura prevista:

- **Node:** creación, hojas, hijos.
- **Tree:** inorden, preorden, postorden.
- **Parser:** `3 + 5`, `3 + 5 * 2`, `(3 + 5) * 2`, `10 / 2 + 3`.
- **Evaluator:** resultados correctos y errores (`10 / 0`, `3 + * 5`, `(3 + 5`).

Calidad de código (fase posterior):

```powershell
ruff check .
ruff format .
```

---

## Tecnologías

| Tecnología | Uso |
| --- | --- |
| Python 3.11+ | Lenguaje; type hints modernos (`X \| Y`, `list[str]`). |
| pytest | Pruebas unitarias. |
| Ruff | Linter y formateo (PEP 8). |
| Git | Versionado con Conventional Commits. |

Dependencias de producción: ninguna fuera de la biblioteca estándar. pytest y Ruff son herramientas de desarrollo.

---

## Decisiones de diseño

1. **Sin `eval()`.** El valor educativo está en tokenizar, parsear, armar el árbol y evaluarlo.
2. **CLI delgada.** `main.py` no contiene la lógica del árbol ni del parser.
3. **Excepciones de dominio.** Se usan tipos propios cuando el error es del lenguaje de expresiones; se reutilizan excepciones estándar solo si encajan de verdad.
4. **Construcción explícita del árbol.** El resultado no es solo un número: el árbol queda en memoria para recorrerlo, convertirlo y dibujarlo.
5. **Alcance acotado en la versión básica.** Potencias, módulo, funciones, variables o GUI se posponen hasta que Node, recorridos, parser, evaluador, CLI y tests estén estables.

---

## Estado del desarrollo

El proyecto se construye por fases. No se adelanta tokenización ni parsing hasta dominar nodos, referencias y recorridos.

| Fase | Contenido | Estado |
| --- | --- | --- |
| 1 | `Node`, referencias, árbol mínimo | En curso |
| 2 | Recorridos inorden / preorden / postorden | Pendiente |
| 3 | Tokenización | Pendiente |
| 4 | Parser (precedencia, pila, Shunting Yard) | Pendiente |
| 5 | Evaluador recursivo | Pendiente |
| 6 | CLI | Pendiente |
| 7 | Visualización del árbol | Pendiente |
| 8 | Tests con pytest | Pendiente |
| 9 | PEP 8, type hints, Ruff | Pendiente |
| 10 | Git/GitHub y documentación | En curso |
| 11 | Extensiones (tras la versión básica) | Pendiente |

---

## Posibles mejoras futuras

Cuando la versión básica funcione de extremo a extremo:

- Operadores `**` y `%`.
- Números negativos y notación científica.
- Funciones matemáticas, variables y constantes.
- Historial de expresiones.
- Mejor visualización del árbol.
- API o interfaz gráfica.

---

## Commits

Se usa [Conventional Commits](https://www.conventionalcommits.org/):

```text
feat: add expression node
feat: implement tree traversals
feat: add expression tokenizer
test: add parser tests
fix: handle division by zero
docs: add project documentation
```
