"""Nodo de un árbol binario de expresión."""

from __future__ import annotations


class Node:
    """Elemento individual de un árbol binario de expresión.

    Un nodo hoja representa un operando (``"3"``, ``"5"``, ``"2.5"``).
    Un nodo interno representa un operador (``"+"``, ``"-"``, ``"*"``, ``"/"``)
    y guarda una referencia a cada uno de sus dos operandos.

    El valor se almacena como texto: en esta fase el nodo solo describe la
    estructura del árbol, mientras que interpretar ese texto como número o
    como operación será responsabilidad del evaluador.
    """

    def __init__(
        self,
        value: str,
        left: Node | None = None,
        right: Node | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        """Indica si el nodo no tiene hijos, es decir, si es un operando."""
        return self.left is None and self.right is None

    def __repr__(self) -> str:
        return f"Node({self.value!r})"
