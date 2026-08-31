from typing import Optional
from .node import Node
from .exceptions import DivisionByZeroTreeError

class Evaluator:
    """
    Recorre el árbol de expresión recursivamente para evaluar el resultado matemático.
    """
    def evaluate(self, node: Optional[Node]) -> float:
        if node is None:
            return 0.0

        # Si es una hoja, es un número (operando)
        if node.is_leaf():
            return float(node.value)

        # Evaluar recursivamente los subárboles izquierdo y derecho
        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)

        # Aplicar la operación correspondiente
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            if right_val == 0:
                raise DivisionByZeroTreeError("Error matemático: Intento de división por cero.")
            return left_val / right_val

        raise ValueError(f"Operador desconocido: {node.value}")
