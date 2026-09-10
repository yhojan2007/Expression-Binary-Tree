class Nodo:
    """
    Representa un nodo en el árbol (expresión o AVL).
    """
    def __init__(self, valor: str | int | float):
        self.valor: str | int | float = valor
        self.izquierdo: Nodo | None = None
        self.derecho: Nodo | None = None
        self.altura: int = 1

    def es_hoja(self) -> bool:
        """Devuelve True si el nodo no tiene hijos."""
        return self.izquierdo is None and self.derecho is None

    def to_dict(self) -> dict:
        """Convierte el nodo a diccionario para JSON."""
        return {
            'valor': str(self.valor),
            'izquierdo': self.izquierdo.to_dict() if self.izquierdo else None,
            'derecho': self.derecho.to_dict() if self.derecho else None,
            'es_hoja': self.es_hoja()
        }
