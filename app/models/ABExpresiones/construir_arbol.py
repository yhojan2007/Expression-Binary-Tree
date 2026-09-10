import re
from app.models.nodo import Nodo


class Parser:
    """
    Convierte una lista de tokens en un árbol de expresión
    utilizando un analizador sintáctico descendente recursivo (Recursive Descent Parser).
    """
    def __init__(self, expression: str):
        self.tokens = self._tokenize(expression)
        self.pos = 0

    def _tokenize(self, expression: str) -> list[str]:
        # Remover espacios en blanco
        expression = expression.replace(" ", "")
        if not expression:
            raise ValueError("La expresión está vacía.")

        # Buscar números (enteros o decimales) y operadores
        tokens = re.findall(r'\d+\.?\d*|[+\-*/()]', expression)

        # Validar si hay caracteres inválidos
        reconstructed = "".join(tokens)
        if reconstructed != expression:
            raise ValueError("La expresión contiene caracteres inválidos.")

        return tokens

    # ==========================
    def parse(self) -> Nodo:
        """Inicia el proceso de parseo y devuelve la raíz del árbol."""
        if not self.tokens:
            raise ValueError("No hay tokens para parsear.")
        self.pos = 0
        raiz = self._parse_expression()
        # Si sobran tokens (por ejemplo un ')' extra), la expresión no es válida.
        if self.pos < len(self.tokens):
            raise ValueError("Expresión malformada: paréntesis desbalanceados o sintaxis incorrecta.")
        return raiz

    def _parse_expression(self) -> Nodo:
        """Maneja sumas y restas (menor precedencia)"""
        # expression := term (('+' | '-') term)*
        nodo = self._parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('+', '-'):
            operator = self.tokens[self.pos]
            self.pos += 1
            nodo_derecho = self._parse_term()

            # El operador queda como raíz; lo ya parseado pasa a ser hijo izquierdo.
            # Así 1+2+3 se asocia a la izquierda: (1+2)+3
            new_nodo = Nodo(operator)
            new_nodo.izquierdo = nodo
            new_nodo.derecho = nodo_derecho
            nodo = new_nodo

        return nodo

    def _parse_term(self) -> Nodo:
        """Maneja multiplicaciones y divisiones (mayor precedencia)"""
        # term := factor (('*' | '/') factor)*
        nodo = self._parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('*', '/'):
            operator = self.tokens[self.pos]
            self.pos += 1
            nodo_derecho = self._parse_factor()

            new_nodo = Nodo(operator)
            new_nodo.izquierdo = nodo
            new_nodo.derecho = nodo_derecho
            nodo = new_nodo

        return nodo

    def _parse_factor(self) -> Nodo:
        """Maneja números y paréntesis (mayor precedencia)"""
        if self.pos >= len(self.tokens):
            raise ValueError("Expresión malformada: falta un operando.")

        token = self.tokens[self.pos]
        
        if token == '(':
            self.pos += 1
            nodo = self._parse_expression()
            if self.pos >= len(self.tokens) or self.tokens[self.pos] != ')':
                raise ValueError("Expresión malformada: paréntesis desbalanceados.")
            self.pos += 1
            return nodo
        
        elif re.match(r'\d+\.?\d*', token):  # Número
            self.pos += 1
            return Nodo(token)

        else:
            raise ValueError(f"Expresión malformada: token inesperado '{token}'.")
