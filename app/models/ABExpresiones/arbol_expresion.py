from app.models.nodo import Nodo
from app.models.ABExpresiones.construir_arbol import Parser


class ArbolExpresion:
    """
    Maneja la estructura del árbol, sus recorridos y evaluación.
    """
    def __init__(self, raiz: Nodo | None = None):
        """ Inicializa el árbol con un nodo raíz opcional."""
        self.raiz = raiz

    def construir_desde_expresion(self, expresion: str) -> None:
        """Construye el árbol a partir de una expresión infija."""
        parser = Parser(expresion)
        self.raiz = parser.parse()

    # ===== Recorridos del árbol =====
    def postorden(self, nodo: Nodo | None) -> list[str]:
        """Recorrido Postorden: Izquierda, Derecha, Raíz. (Genera notación Posfija)"""
        resultado = []
        if nodo:
            resultado.extend(self.postorden(nodo.izquierdo))
            resultado.extend(self.postorden(nodo.derecho))
            # La raíz se visita al final: así sale la notación posfija (RPN).
            resultado.append(str(nodo.valor))
        return resultado

    def inorden(self, nodo: Nodo | None) -> list[str]:
        """Recorrido Inorden: Izquierda, Raíz, Derecha. (Genera notación Infija)"""
        resultado = []
        if nodo:
            # Paréntesis solo en operadores, para no perder la precedencia al reconstruir.
            if not nodo.es_hoja():
                resultado.append("(")
            resultado.extend(self.inorden(nodo.izquierdo))
            resultado.append(str(nodo.valor))
            resultado.extend(self.inorden(nodo.derecho))
            if not nodo.es_hoja():
                resultado.append(")")
        return resultado

    def preorden(self, nodo: Nodo | None) -> list[str]:
        """Recorrido Preorden: Raíz, Izquierda, Derecha. (Genera notación Prefija)"""
        resultado = []
        if nodo:
            resultado.append(str(nodo.valor))
            resultado.extend(self.preorden(nodo.izquierdo))
            resultado.extend(self.preorden(nodo.derecho))
        return resultado

    # ==== Funcion para evaluar la expresion del arbol ====
    def evaluador(self, nodo: Nodo | None) -> float:
        """Evalúa la expresión representada por el árbol."""
        if nodo is None:
            raise ValueError("El nodo no puede ser None.")

        # Hoja = operando. El valor se guardó como texto al parsear.
        if nodo.es_hoja():
            return float(nodo.valor)

        izquierda = self.evaluador(nodo.izquierdo)
        derecha = self.evaluador(nodo.derecho)

        if nodo.valor == '+':
            return izquierda + derecha
        elif nodo.valor == '-':
            return izquierda - derecha
        elif nodo.valor == '*':
            return izquierda * derecha
        elif nodo.valor == '/':
            if derecha == 0:
                raise ZeroDivisionError("División por cero.")
            return izquierda / derecha
        else:
            raise ValueError(f"Operador desconocido: {nodo.valor}")

    def evaluar(self) -> float:
        """Evalúa la expresión desde la raíz del árbol."""
        if self.raiz is None:
            raise ValueError("El árbol está vacío.")
        return self.evaluador(self.raiz)

    def to_dict(self) -> dict:
        """Convierte el árbol completo a diccionario"""
        return {
            'expresion': ''.join(self.inorden(self.raiz)) if self.raiz else '',
            'resultado': self.evaluar() if self.raiz else None,
            'arbol': self.raiz.to_dict() if self.raiz else None
        }
