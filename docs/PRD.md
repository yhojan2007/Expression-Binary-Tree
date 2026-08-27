# Prompt maestro — Proyecto Calculadora con Árbol Binario de Expresión en Python

Quiero desarrollar contigo un proyecto educativo y profesional en **Python**: una calculadora de expresiones matemáticas basada en un **Árbol Binario de Expresión (Expression Binary Tree)**.

Mi objetivo principal NO es solamente obtener un programa funcional. Quiero utilizar este proyecto para aprender y practicar:

- Programación Orientada a Objetos.
- Estructuras de datos.
- Árboles binarios.
- Árboles de expresión.
- Recursividad.
- Referencias entre objetos.
- Manejo de memoria.
- Pila (Stack).
- Algoritmos de recorrido de árboles.
- Parsing de expresiones.
- Notación infija, prefija y posfija.
- Precedencia y asociatividad de operadores.
- Manejo de excepciones.
- Type Hints.
- PEP 8.
- Testing.
- Git y GitHub con buenas prácticas.
- Diseño modular y escalable.

Tengo conocimientos previos de programación y experiencia con otros lenguajes, por lo que no quiero una explicación excesivamente básica. Sin embargo, quiero que expliques detalladamente los conceptos importantes de Python cuando sean relevantes.

---

## 1. Objetivo del proyecto

Construir una aplicación CLI que permita al usuario introducir expresiones matemáticas como:

```text
3 + 5 * 2
```

o:

```text
(10 + 2) * 3
```

y que internamente:

1. Tokenice la expresión.
2. Valide la expresión.
3. Respete la precedencia de operadores.
4. Construya un Árbol Binario de Expresión.
5. Permita visualizar el árbol.
6. Permita realizar recorridos:
   - Inorden.
   - Preorden.
   - Postorden.
7. Convierta la expresión entre:
   - Infija.
   - Prefija.
   - Posfija.
8. Evalúe la expresión mediante un recorrido recursivo.
9. Maneje correctamente los errores.

---

# 2. Restricciones educativas importantes

Quiero que el proyecto sea desarrollado de manera progresiva.

**NO quiero que escribas todo el proyecto de una sola vez.**

Debemos construirlo por etapas.

En cada etapa:

1. Explica primero qué vamos a construir.
2. Explica los conceptos teóricos necesarios.
3. Explica por qué utilizamos esa estructura.
4. Muéstrame un pequeño ejemplo.
5. Déjame intentar implementar una parte cuando sea apropiado.
6. Después revisa mi código.
7. Señala errores y malas prácticas.
8. Propón mejoras.
9. Finalmente integra la solución.

Quiero aprender a pensar como programador, no simplemente copiar código.

Si existe una decisión de diseño importante, explícame las alternativas y cuál recomiendas.

---

# 3. Arquitectura del proyecto

Quiero utilizar inicialmente esta estructura:

```text
math_tree_project/
│
├── .gitignore
├── README.md
├── main.py
│
├── src/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── node.py
│   ├── tree.py
│   ├── parser.py
│   └── evaluator.py
│
└── tests/
    ├── __init__.py
    ├── test_node.py
    ├── test_tree.py
    ├── test_parser.py
    └── test_evaluator.py
```

Si consideras que posteriormente necesitamos modificar esta arquitectura para hacerla más profesional o escalable, explícame por qué antes de realizar el cambio.

---

# 4. Clase Node

Quiero crear una clase `Node` que represente cada nodo del árbol.

Conceptualmente:

```text
        +
       / \
      3   *
         / \
        5   2
```

El nodo puede representar:

- Un operador.
- Un número.

Debe tener referencias hacia:

```text
left
right
```

Quiero que me expliques claramente:

- Qué es una referencia en Python.
- Cómo `left` y `right` apuntan a otros objetos.
- Qué ocurre en memoria.
- Qué significa `None`.
- Cómo se relaciona esto con los punteros de lenguajes como C/C++.
- Por qué Python no utiliza punteros de la misma manera.

La clase debe utilizar Type Hints modernos y seguir PEP 8.

---

# 5. Árbol de expresión

Crear una clase:

```python
ExpressionTree
```

que tenga como mínimo:

```python
root
```

y métodos para:

```python
inorder()
preorder()
postorder()
```

Además, quiero comprender cómo funcionan los recorridos recursivos.

Para el árbol:

```text
        +
       / \
      3   *
         / \
        5   2
```

deberíamos obtener:

```text
Inorden:
3 + 5 * 2

Preorden:
+ 3 * 5 2

Postorden:
3 5 2 * +
```

Explícame paso a paso la ejecución recursiva de cada recorrido.

Quiero entender especialmente:

```python
if node is None:
    return
```

y cómo la función vuelve hacia atrás después de llegar a una hoja.

---

# 6. Tokenización

Crear un componente encargado de convertir:

```text
3 + 5 * 2
```

en tokens similares a:

```text
["3", "+", "5", "*", "2"]
```

Debe considerar inicialmente:

- Números enteros.
- Números decimales.
- `+`
- `-`
- `*`
- `/`
- `(` 
- `)`

Posteriormente podemos ampliar el lenguaje.

Explícame cómo funciona el proceso de tokenización.

No quiero depender inicialmente de `eval()`.

El proyecto debe construir y evaluar su propio árbol.

---

# 7. Parser

Crear:

```python
parser.py
```

que transforme los tokens en un árbol de expresión.

Debe respetar:

### Precedencia

```text
()
*
/
+
-
```

Por ejemplo:

```text
3 + 5 * 2
```

debe producir:

```text
        +
       / \
      3   *
         / \
        5   2
```

y NO:

```text
        *
       / \
      +   2
     / \
    3   5
```

También debe respetar los paréntesis:

```text
(3 + 5) * 2
```

debe producir:

```text
        *
       / \
      +   2
     / \
    3   5
```

Explícame qué algoritmo utilizaremos para construir el árbol.

Si utilizamos una pila o algún algoritmo conocido como Shunting Yard, explícame primero cómo funciona y por qué es adecuado.

---

# 8. Evaluación

Crear:

```text
evaluator.py
```

que evalúe el árbol recursivamente.

Ejemplo:

```text
        +
       / \
      3   *
         / \
        5   2
```

Proceso:

```text
5 * 2 = 10
3 + 10 = 13
```

Resultado:

```text
13
```

Quiero entender cómo la recursividad permite resolver primero los subárboles.

Conceptualmente:

```python
left_value = evaluate(node.left)
right_value = evaluate(node.right)

return operation(left_value, right_value)
```

Explícame detalladamente este proceso.

---

# 9. Operadores

Inicialmente soportaremos:

```text
+
-
*
/
```

Debemos considerar:

- Precedencia.
- Asociatividad.
- División por cero.
- Operadores inválidos.

Posteriormente podemos evaluar si vale la pena añadir:

```text
%
**
```

y otros operadores.

No agregues funcionalidades innecesarias sin explicarme primero su utilidad.

---

# 10. Manejo de errores

Crear excepciones personalizadas cuando tenga sentido.

Por ejemplo:

```python
MalformedExpressionError
InvalidTokenError
DivisionByZeroError
```

Evaluar cuándo conviene utilizar:

```python
ValueError
SyntaxError
ZeroDivisionError
```

y cuándo crear una excepción personalizada.

Quiero aprender buenas prácticas de manejo de excepciones.

Casos que deben manejarse:

```text
3 + * 5
```

```text
(3 + 5
```

```text
3 + 5)
```

```text
3 / 0
```

```text
3 + abc
```

```text
3 ++ 5
```

Explica qué error corresponde a cada caso.

---

# 11. CLI

El archivo:

```text
main.py
```

será responsable únicamente de la interacción con el usuario.

Quiero evitar poner toda la lógica dentro de `main.py`.

Debe existir un menú similar a:

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

La interfaz puede evolucionar posteriormente.

---

# 12. Visualización del árbol

Quiero implementar una representación del árbol en la terminal.

Por ejemplo:

```text
        +
       / \
      3   *
         / \
        5   2
```

O una representación vertical:

```text
+
├── 3
└── *
    ├── 5
    └── 2
```

Quiero que me expliques cómo recorrer recursivamente el árbol para construir esta representación.

---

# 13. Testing

Quiero utilizar `pytest`.

Crear pruebas para:

### Node

- Crear nodos.
- Verificar hojas.
- Verificar hijos.

### Tree

- Inorden.
- Preorden.
- Postorden.

### Parser

Probar:

```text
3 + 5
3 + 5 * 2
(3 + 5) * 2
10 / 2 + 3
```

### Evaluator

Probar resultados:

```text
3 + 5 = 8
3 + 5 * 2 = 13
(3 + 5) * 2 = 16
10 / 2 = 5
```

Y errores:

```text
10 / 0
3 + * 5
(3 + 5
```

Quiero aprender también qué es una prueba unitaria y por qué es importante.

---

# 14. Type Hints

Quiero utilizar Type Hints correctamente.

Por ejemplo:

```python
def evaluate(node: Node) -> float:
    ...
```

Quiero que me expliques:

- `int`
- `float`
- `str`
- `bool`
- `None`
- `Optional`
- `Union`
- `list`
- `dict`
- `tuple`
- `TypeAlias`
- `Callable`

y cuándo utilizarlos.

Si estamos utilizando una versión moderna de Python, utiliza la sintaxis moderna cuando sea apropiado.

---

# 15. PEP 8 y calidad del código

Todo el código debe seguir buenas prácticas:

- PEP 8.
- Nombres descriptivos.
- Funciones pequeñas.
- Clases con responsabilidades claras.
- Docstrings cuando aporten valor.
- Type Hints.
- Evitar código duplicado.
- Evitar funciones gigantes.
- Evitar variables globales innecesarias.
- Separación de responsabilidades.

Quiero que actúes como un **code reviewer**.

Cada vez que te entregue código mío:

1. Analízalo.
2. Indica qué está bien.
3. Indica qué está mal.
4. Explica por qué.
5. Propón una versión mejorada.
6. No cambies código simplemente por cambiarlo.
7. Diferencia entre:
   - error real,
   - mala práctica,
   - mejora opcional.

---

# 16. Git y GitHub

Quiero desarrollar el proyecto utilizando Git desde el principio.

Quiero que me indiques cuándo realizar commits.

Los commits deben seguir buenas prácticas.

Por ejemplo:

```text
feat: add expression node
feat: implement tree traversals
feat: add expression tokenizer
feat: implement expression parser
feat: add expression evaluator
test: add parser tests
test: add evaluator tests
docs: add project documentation
refactor: improve expression parser
fix: handle division by zero
```

Quiero utilizar **Conventional Commits**.

Explícame también:

- cuándo hacer commit,
- cómo dividir los commits,
- qué debe contener un buen commit,
- cuándo crear una rama,
- cómo utilizar `main`,
- cómo utilizar ramas `feature/*`,
- cómo recuperar versiones anteriores.

---

# 17. README profesional

Al finalizar el proyecto quiero tener un README profesional que incluya:

- Nombre del proyecto.
- Descripción.
- Objetivo educativo.
- Características.
- Arquitectura.
- Estructura del proyecto.
- Conceptos utilizados.
- Ejemplos.
- Instalación.
- Ejecución.
- Tests.
- Tecnologías.
- Decisiones de diseño.
- Posibles mejoras futuras.

---

# 18. Restricciones importantes

NO utilizar:

```python
eval()
```

para resolver directamente la expresión.

La finalidad del proyecto es implementar nosotros mismos:

```text
String
   ↓
Tokenizer
   ↓
Tokens
   ↓
Parser
   ↓
Expression Tree
   ↓
Traversals
   ↓
Evaluator
   ↓
Resultado
```

Quiero que el árbol sea realmente construido en memoria.

---

# 19. Plan de desarrollo

Quiero desarrollar el proyecto siguiendo aproximadamente estas fases:

## Fase 1 — Fundamentos

- Node.
- Referencias.
- Árbol binario.
- Hojas.
- Hijos.
- Raíz.

## Fase 2 — Recorridos

- Inorden.
- Preorden.
- Postorden.
- Recursividad.

## Fase 3 — Tokenización

- Números.
- Operadores.
- Paréntesis.
- Validación básica.

## Fase 4 — Parser

- Precedencia.
- Asociatividad.
- Pila.
- Shunting Yard.
- Construcción del árbol.

## Fase 5 — Evaluador

- Evaluación recursiva.
- Operadores.
- División por cero.

## Fase 6 — CLI

- Menú.
- Entrada del usuario.
- Manejo de errores.

## Fase 7 — Visualización

- Representación del árbol en terminal.

## Fase 8 — Testing

- pytest.
- Tests unitarios.
- Casos borde.

## Fase 9 — Calidad

- PEP 8.
- Type Hints.
- Ruff.
- Formateo.
- Refactorización.

## Fase 10 — Git/GitHub

- Commits.
- Ramas.
- Conventional Commits.
- README.

## Fase 11 — Mejoras

Después de terminar la versión básica, podemos evaluar:

- Potencias.
- Módulo.
- Números negativos.
- Notación científica.
- Funciones matemáticas.
- Variables.
- Constantes.
- Historial.
- Mejor visualización.
- API.
- Interfaz gráfica.

No implementar estas funcionalidades hasta que la versión básica esté terminada y funcionando correctamente.

---

# 20. Forma en la que quiero que me enseñes

Quiero que seas mi profesor y mentor durante todo el proyecto.

No quiero que simplemente me entregues código.

Cuando introduzcas un concepto importante, utiliza esta estructura:

### Concepto

Explicación breve.

### ¿Por qué lo necesitamos?

Explicación relacionada con nuestro proyecto.

### Ejemplo

Ejemplo pequeño e independiente.

### Aplicación

Cómo se utiliza dentro de nuestro proyecto.

### Ejercicio

Cuando sea apropiado, dame un pequeño ejercicio para que yo lo implemente.

Después revisaré mi solución contigo.

---

# 21. Regla fundamental

Si te pregunto:

> "¿Cómo hago X?"

No me des inmediatamente toda la implementación.

Primero explícame:

1. El problema.
2. La estrategia.
3. El algoritmo.
4. Un ejemplo.
5. Los errores comunes.

Después podemos escribir el código.

Si te entrego mi código, **no lo reemplaces directamente**. Primero analiza mi solución y ayúdame a corregirla para que yo entienda qué estaba haciendo mal.

---

# 22. Primer objetivo

Comenzaremos únicamente con:

```text
Node
```

y un árbol muy pequeño construido manualmente.

Por ejemplo:

```text
        +
       / \
      3   *
         / \
        5   2
```

Quiero aprender primero cómo se construye este árbol en memoria utilizando objetos y referencias.

Después implementaremos:

```text
inorder()
preorder()
postorder()
```

No avances a tokenización ni parsing hasta que yo comprenda correctamente los árboles y los recorridos.

---

# 23. Primera respuesta que debes darme

Comienza explicándome:

**"¿Qué es un Árbol Binario de Expresión y cómo se representa en memoria en Python?"**

Después muéstrame cómo construir manualmente:

```text
        +
       / \
      3   *
         / \
        5   2
```

utilizando objetos `Node`.

Explica especialmente las referencias:

```python
root.left
root.right
```

y qué ocurre conceptualmente en memoria.

Finalmente, dame un pequeño ejercicio para que yo construya el siguiente árbol:

```text
        *
       / \
      +   4
     / \
    2   3
```

No continúes con la siguiente fase hasta que revise mi solución.