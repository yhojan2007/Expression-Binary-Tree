# Árbol de expresión

Un **árbol de expresión** representa una fórmula aritmética: los **operadores** van en nodos internos y los **operandos** (números) en las hojas.

Para `3 + 5 * 2` el árbol correcto (con precedencia) es:

```text
      +
     / \
    3   *
       / \
      5   2
```

No es `*(+(3,5), 2)`. El parser existe precisamente para respetar `*`/`/` sobre `+`/`-` y los paréntesis.

Código:

- Tokenizar y armar el árbol: `app/models/ABExpresiones/construir_arbol.py` (`Parser`).
- Recorrer y evaluar: `app/models/ABExpresiones/arbol_expresion.py` (`ArbolExpresion`).

## Gramática

Análisis descendente recursivo, un método por nivel de precedencia:

```text
expression  :=  term   (('+' | '-') term)*
term        :=  factor (('*' | '/') factor)*
factor      :=  número | '(' expression ')'
```

`1+2+3` se asocia a la izquierda: `(1+2)+3`. Igual `8/4/2` → `(8/4)/2`.

Los números se reconocen con `\d+\.?\d*` (enteros o decimales). Cualquier carácter que no sea dígito, operador o paréntesis hace fallar la reconstrucción de tokens.

## Evaluación

`evaluador` recorre el árbol:

1. Si el nodo es hoja, `float(valor)`.
2. Si no, evalúa hijo izquierdo y derecho y aplica `+`, `-`, `*`, `/`.
3. División por cero lanza `ZeroDivisionError`.

La página llama a construir + evaluar en un solo POST (`/expresion/construir`). Existe también `/expresion/evaluar` si solo se necesita el número.

## Recorridos

Sobre el árbol de `3+5*2`:

| Recorrido | Orden | Resultado |
|---|---|---|
| Preorden | raíz, izq, der | `+ 3 * 5 2` (prefija) |
| Inorden | izq, raíz, der | `(3+(5*2))` (infija, con paréntesis en operadores) |
| Postorden | izq, der, raíz | `3 5 2 * +` (posfija / RPN) |

El inorden añade paréntesis en nodos que no son hoja para no perder la precedencia al reconstruir el texto.

## Cómo se conecta con la web

`ArbolExpresion.construir_desde_expresion` instancia el `Parser`, guarda la raíz y `to_dict()` entrega:

```json
{
  "expresion": "(3+(5*2))",
  "resultado": 13.0,
  "arbol": { "valor": "+", "izquierdo": { "...": "..." }, "derecho": { "...": "..." } }
}
```

El campo `arbol` es lo que D3 pinta.

## Límites del parser

No hay menos unario ni potencia. Un token `+` o `-` al inicio de un factor se considera inesperado (`-3+5` falla). No hay variables (`x+1`).
