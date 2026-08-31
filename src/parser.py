import re
from typing import List
from .node import Node
from .exceptions import MalformedExpressionError

class Parser:
    """
    Se encarga de tokenizar y construir el árbol a partir de una expresión infija
    utilizando un analizador sintáctico descendente recursivo (Recursive Descent Parser).
    """
    def __init__(self, expression: str):
        self.tokens = self._tokenize(expression)
        self.pos = 0

    def _tokenize(self, expression: str) -> List[str]:
        # Remover espacios en blanco
        expression = expression.replace(" ", "")
        if not expression:
            raise MalformedExpressionError("La expresión está vacía.")
        
        # Buscar números (enteros o decimales) y operadores
        tokens = re.findall(r'\d+\.?\d*|[+\-*/()]', expression)
        
        # Validar si hay caracteres inválidos
        reconstructed = "".join(tokens)
        if reconstructed != expression:
            raise MalformedExpressionError("La expresión contiene caracteres inválidos.")
        
        return tokens

    def parse(self) -> Node:
        """Inicia el parsing y devuelve el nodo raíz del árbol."""
        if not self.tokens:
            raise MalformedExpressionError("No hay tokens para parsear.")
        self.pos = 0
        root = self._parse_expression()
        if self.pos < len(self.tokens):
            raise MalformedExpressionError("Expresión malformada: paréntesis desbalanceados o sintaxis incorrecta.")
        return root

    def _parse_expression(self) -> Node:
        """Maneja sumas y restas (menor precedencia)"""
        node = self._parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('+', '-'):
            operator = self.tokens[self.pos]
            self.pos += 1
            right_node = self._parse_term()
            
            new_node = Node(operator)
            new_node.left = node
            new_node.right = right_node
            node = new_node
            
        return node

    def _parse_term(self) -> Node:
        """Maneja multiplicaciones y divisiones (mayor precedencia)"""
        node = self._parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('*', '/'):
            operator = self.tokens[self.pos]
            self.pos += 1
            right_node = self._parse_factor()
            
            new_node = Node(operator)
            new_node.left = node
            new_node.right = right_node
            node = new_node
            
        return node

    def _parse_factor(self) -> Node:
        """Maneja números y paréntesis"""
        if self.pos >= len(self.tokens):
            raise MalformedExpressionError("Expresión incompleta.")
        
        token = self.tokens[self.pos]
        
        if token == '(':
            self.pos += 1
            node = self._parse_expression()
            if self.pos >= len(self.tokens) or self.tokens[self.pos] != ')':
                raise MalformedExpressionError("Paréntesis de cierre faltante.")
            self.pos += 1
            return node
        
        elif re.match(r'^\d+\.?\d*$', token):
            self.pos += 1
            return Node(float(token))
            
        else:
            raise MalformedExpressionError(f"Token inesperado: {token}")
