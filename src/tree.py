from typing import List, Optional
from .node import Node

class ExpressionTree:
    """
    Maneja la estructura del árbol y sus recorridos.
    """
    def __init__(self, root: Optional[Node] = None):
        self.root = root

    def postorder(self, node: Optional[Node]) -> List[str]:
        """Recorrido Postorden: Izquierda, Derecha, Raíz. (Genera notación Posfija)"""
        result = []
        if node:
            result.extend(self.postorder(node.left))
            result.extend(self.postorder(node.right))
            # Formatear números para que no tengan .0 si son enteros
            val = str(int(node.value)) if isinstance(node.value, float) and node.value.is_integer() else str(node.value)
            result.append(val)
        return result

    def inorder(self, node: Optional[Node]) -> List[str]:
        """Recorrido Inorden: Izquierda, Raíz, Derecha. (Genera notación Infija)"""
        result = []
        if node:
            if not node.is_leaf():
                result.append("(")
            result.extend(self.inorder(node.left))
            
            val = str(int(node.value)) if isinstance(node.value, float) and node.value.is_integer() else str(node.value)
            result.append(val)
            
            result.extend(self.inorder(node.right))
            if not node.is_leaf():
                result.append(")")
        return result

    def preorder(self, node: Optional[Node]) -> List[str]:
        """Recorrido Preorden: Raíz, Izquierda, Derecha. (Genera notación Prefija)"""
        result = []
        if node:
            val = str(int(node.value)) if isinstance(node.value, float) and node.value.is_integer() else str(node.value)
            result.append(val)
            result.extend(self.preorder(node.left))
            result.extend(self.preorder(node.right))
        return result
