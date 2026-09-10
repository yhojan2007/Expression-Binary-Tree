# Guía de uso

## Arranque

Sigue las instrucciones del [README](../README.md). Con el servidor en marcha, la barra superior enlaza **Inicio**, **Árbol de Expresión** y **Árbol de Búsqueda**.

En el lienzo del árbol puedes hacer zoom con la rueda del ratón y arrastrar para desplazar la vista.

## Árbol de expresión

Ruta: `/expresion`.

1. Escribe una expresión infija, por ejemplo `3 + 5 * 2`.
2. Pulsa **Construir Árbol** (o Enter).
3. El servidor parsea, evalúa y devuelve el árbol. La página muestra el resultado numérico y el dibujo.

Operadores permitidos: `+`, `-`, `*`, `/` y paréntesis. Se admiten enteros y decimales (`1.5 * 2`). Los espacios se ignoran.

Ejemplos:

| Entrada | Resultado | Comentario |
|---|---|---|
| `3 + 5 * 2` | 13 | La multiplicación pesa más que la suma |
| `(3 + 5) * 2` | 16 | Los paréntesis cambian la raíz del árbol |
| `8 - 3 - 2` | 3 | Asociación a la izquierda: `(8-3)-2` |
| `10 / 4` | 2.5 | División en punto flotante |

No válido (el servidor responde con error):

- Letras o símbolos ajenos (`hola`, `3^2`).
- Menos unario (`-3 + 5`). Escribe `0 - 3 + 5`.
- Paréntesis desbalanceados, operadores sueltos (`3+`, `3++2`) o división por cero.

En el dibujo, los operadores se colorean en naranja y los números en azul.

## Árbol AVL (pantalla «Árbol de Búsqueda»)

Ruta: `/busqueda`. El modelo es un **AVL** (ABB autoequilibrado), aunque el título de la página habla de ABB.

1. Introduce un número.
2. **Insertar** lo coloca en el árbol y reequilibra si hace falta.
3. **Buscar** indica si el valor existe (alerta).
4. **Eliminar** lo quita (con confirmación) y vuelve a balancear.
5. **Reiniciar** deja el árbol vacío.

Los enteros se guardan como enteros (`7.0` → `7`) para que insertar y buscar coincidan. Los decimales no enteros se conservan (`7.5`).

Ejemplo de balanceo: inserta `10`, luego `20`, luego `30`. Sin AVL sería una cadena hacia la derecha; con AVL la raíz pasa a ser `20`.

La tarjeta de estadísticas muestra **altura** (definición AVL: hoja = 1) y **número de nodos**.

Los valores duplicados no se insertan. El mensaje de éxito de la API no distingue ese caso: el árbol simplemente no cambia.

El árbol vive en memoria del proceso Flask. Si cierras el servidor o recargas el código en modo debug, se pierde. Varias pestañas contra la misma instancia comparten el mismo árbol.
