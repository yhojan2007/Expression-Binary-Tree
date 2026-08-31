class MalformedExpressionError(Exception):
    """Excepción lanzada cuando la expresión matemática tiene errores de sintaxis."""
    pass

class DivisionByZeroTreeError(Exception):
    """Excepción lanzada al intentar dividir por cero durante la evaluación del árbol."""
    pass
