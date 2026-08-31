"""Árbol binario de expresión y sus recorridos."""

from __future__ import annotations

from src.node import Node


class ExpressionTree:
    """Árbol binario de expresión.

    Solo guarda una referencia a la raíz: el resto del árbol es alcanzable
    siguiendo los atributos ``left`` y ``right`` de cada nodo.

    Cada recorrido devuelve la lista de valores visitados en orden, que
    corresponde a una de las tres notaciones clásicas:

    - inorden   -> notación infija   (``3 + 5 * 2``)
    - preorden  -> notación prefija  (``+ 3 * 5 2``)
    - postorden -> notación posfija  (``3 5 2 * +``)
    """

    def __init__(self, root: Node | None = None) -> None:
        self.root = root

    def inorder(self) -> list[str]:
        """Devuelve los valores en orden izquierda, raíz, derecha."""
        return self._inorder(self.root)

    def preorder(self) -> list[str]:
        """Devuelve los valores en orden raíz, izquierda, derecha."""
        return self._preorder(self.root)

    def postorder(self) -> list[str]:
        """Devuelve los valores en orden izquierda, derecha, raíz."""
        return self._postorder(self.root)

    def _inorder(self, node: Node | None) -> list[str]:
        if node is None:
            return []
        return [
            *self._inorder(node.left),
            node.value,
            *self._inorder(node.right),
        ]

    def _preorder(self, node: Node | None) -> list[str]:
        if node is None:
            return []
        return [
            node.value,
            *self._preorder(node.left),
            *self._preorder(node.right),
        ]

    def _postorder(self, node: Node | None) -> list[str]:
        if node is None:
            return []
        return [
            *self._postorder(node.left),
            *self._postorder(node.right),
            node.value,
        ]

    def __repr__(self) -> str:
        return f"ExpressionTree(root={self.root!r})"
