from typing import Optional, Union

class Node:
    """
    Representa un nodo en el árbol de expresión matemática.
    Puede contener un operador (str) o un operando (float).
    """
    def __init__(self, value: Union[str, float]):
        self.value: Union[str, float] = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

    def is_leaf(self) -> bool:
        """Devuelve True si es un operando (no tiene hijos)."""
        return self.left is None and self.right is None
