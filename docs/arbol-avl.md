# Árbol AVL

Implementación en `app/models/ABB/ABB_AVL.py`. Es un **ABB** (menores a la izquierda, mayores a la derecha) que **se reequilibra** después de insertar o borrar para que el factor de balance de cada nodo esté en `[-1, 1]`.

## Definiciones

Altura de `None` = `0`. Altura de una hoja = `1`. En general:

```text
altura(n) = 1 + max(altura(izquierdo), altura(derecho))
```

Factor de balance:

```text
FB(n) = altura(izquierdo) - altura(derecho)
```

- `FB > 1` — el subárbol izquierdo es demasiado alto (casos LL o LR).
- `FB < -1` — el subárbol derecho es demasiado alto (casos RR o RL).

Los duplicados se ignoran: si `valor == nodo.valor`, `_insertar` no crea otro nodo.

## Rotaciones

Rotación **derecha** (caso LL): el hijo izquierdo sube.

```text
    y                 x
   /        →        / \
  x                 T   y
   \
    T
```

Rotación **izquierda** (caso RR): simétrica, el hijo derecho sube.

Casos dobles:

- **LR:** el desequilibrio está a la izquierda, pero el hijo izquierdo está cargado a la derecha → rotación izquierda sobre el hijo y luego derecha sobre el nodo.
- **RL:** simétrico (derecha + izquierda).

Después de rotar se actualizan alturas: primero el nodo que bajó, luego la nueva raíz del subárbol.

## Inserción

Igual que un BST; al volver de la recursión se llama `balancear`. Ejemplo RR: insertar `10`, `20`, `30` deja raíz `20`, hijos `10` y `30`.

## Eliminación

1. Valor menor o mayor: bajar por la rama y, al subir, balancear.
2. Nodo encontrado:
   - 0 o 1 hijo: se sustituye por el hijo (o `None`).
   - 2 hijos: se copia el **sucesor inorden** (mínimo del subárbol derecho) y se elimina ese sucesor en la rama derecha.
3. Tras el cambio, `balancear` en el camino de regreso.

## Búsqueda y recorridos

`buscar` es iterativo (compara y baja a izquierda o derecha).

El inorden de un AVL (y de cualquier BST) sale **ordenado**. Preorden y postorden se exponen en `to_dict()` aunque la plantilla actual destaque altura y total de nodos.

## Complejidad (referencia)

Con el invariante AVL, altura es `O(log n)`. Inserción, borrado y búsqueda son `O(log n)` en el peor caso, frente a `O(n)` de un ABB degenerado (por ejemplo insertar `1, 2, 3, …` sin rotaciones).

## Estado en la aplicación

Una instancia global `arbol_actual` en el controlador. Ver [uso.md](uso.md) y [arquitectura.md](arquitectura.md).
