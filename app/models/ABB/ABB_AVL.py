from app.models.nodo import Nodo


class ArbolAVL:
    """
    Implementa un Árbol Binario de Búsqueda (ABB) balanceado (AVL).
    Permite insertar, eliminar, buscar y recorrer los nodos.
    """
    def __init__(self):
        self.raiz: Nodo | None = None
        self.altura: int = 0

    def obtener_altura(self, nodo: Nodo | None) -> int:
        """Devuelve la altura de un nodo.

        Args:
            nodo: Nodo cuya altura se desea obtener.

        Returns:
            La altura del nodo. Devuelve 0 si el nodo es None.
        """
        if nodo is None:
            return 0

        return nodo.altura

    def actualizar_altura(self, nodo: Nodo) -> None:
        """Actualiza la altura de un nodo.

        La altura se obtiene tomando la mayor altura entre
        los subárboles izquierdo y derecho y sumando uno.

        Args:
            nodo: Nodo cuya altura será actualizada.
        """
        altura_izquierda = self.obtener_altura(nodo.izquierdo)
        altura_derecha = self.obtener_altura(nodo.derecho)

        nodo.altura = 1 + max(altura_izquierda, altura_derecha)

    def obtener_factor_balance(self, nodo: Nodo | None) -> int:
        """Calcula el factor de balance de un nodo.

        Formula:

            FB = altura(izquierdo) - altura(derecho)

        Args:
            nodo: Nodo que se desea analizar.

        Returns:
            Factor de balance del nodo.
        """
        if nodo is None:
            return 0

        return (self.obtener_altura(nodo.izquierdo) - self.obtener_altura(nodo.derecho))

    def rotacion_derecha(self, y: Nodo) -> Nodo:
        """Realiza una rotación simple hacia la derecha.
        Se utiliza principalmente para corregir un caso LL.

        Args:
            y: Nodo que será rotado.

        Returns:
            Nueva raíz del subárbol.
        """
        x = y.izquierdo

        if x is None:
            return y

        subarbol = x.derecho

        x.derecho = y
        y.izquierdo = subarbol

        # Primero el que bajó (y), luego la nueva raíz (x).
        self.actualizar_altura(y)
        self.actualizar_altura(x)

        return x

    def rotacion_izquierda(self, x: Nodo) -> Nodo:
        """Realiza una rotación simple hacia la izquierda.
        Se utiliza principalmente para corregir un caso RR.

        Args:
            x: Nodo que será rotado.

        Returns:
            Nueva raíz del subárbol.
        """
        y = x.derecho

        if y is None:
            return x

        subarbol = y.izquierdo

        y.izquierdo = x
        x.derecho = subarbol

        self.actualizar_altura(x)
        self.actualizar_altura(y)

        return y

    def balancear(self, nodo: Nodo) -> Nodo:
        """Balancea un nodo después de una modificación.

        Args:
            nodo: Nodo que se desea balancear.

        Returns:
            Nueva raíz del subárbol balanceado.
        """
        self.actualizar_altura(nodo)

        fb = self.obtener_factor_balance(nodo)

        # Caso LL o LR.
        if fb > 1:
            # Caso LR: Rotación doble (izquierda-derecha).
            if self.obtener_factor_balance(nodo.izquierdo) < 0:
                nodo.izquierdo = self.rotacion_izquierda(nodo.izquierdo)

            return self.rotacion_derecha(nodo)

        # Caso RR o RL.
        if fb < -1:
            # Caso RL: Rotación doble (derecha-izquierda).
            if self.obtener_factor_balance(nodo.derecho) > 0:
                nodo.derecho = self.rotacion_derecha(nodo.derecho)

            return self.rotacion_izquierda(nodo)

        return nodo

    def insertar(self, valor: int) -> None:
        """Inserta un valor y balancea el árbol.

        Args:
            valor: Valor entero que se desea insertar.
        """
        self.raiz = self._insertar(self.raiz, valor)
        self.altura = self.obtener_altura(self.raiz)

    def _insertar(self, nodo: Nodo | None, valor: int) -> Nodo:
        """Inserta recursivamente un valor en el árbol.

        Args:
            nodo: Nodo actual.
            valor: Valor que se desea insertar.

        Returns:
            Nueva raíz del subárbol después de insertar y balancear.
        """
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierdo = self._insertar(nodo.izquierdo, valor)

        elif valor > nodo.valor:
            nodo.derecho = self._insertar(nodo.derecho, valor)

        else:
            # No se permiten valores duplicados.
            return nodo
        # Balancear el nodo actual después de la inserción
        return self.balancear(nodo)

    def eliminar(self, valor: int) -> None:
        """Elimina un valor y balancea el árbol.

        Args:
            valor: Valor entero que se desea eliminar.
        """
        self.raiz = self._eliminar(self.raiz, valor)
        self.altura = self.obtener_altura(self.raiz)

    def _eliminar(self, nodo: Nodo | None, valor: int) -> Nodo | None:
        """Elimina recursivamente un valor del árbol.

        Args:
            nodo: Nodo actual.
            valor: Valor que se desea eliminar.

        Returns:
            Nueva raíz del subárbol después de eliminar y balancear.
        """
        if nodo is None:
            return None

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar(nodo.derecho, valor)
        else:
            # Nodo a eliminar encontrado
            # Caso 1 y 2: 0 o 1 hijo. El hijo (o None) sustituye al nodo.
            if nodo.izquierdo is None:
                return nodo.derecho

            if nodo.derecho is None:
                return nodo.izquierdo

            # Caso # 3: Nodo con dos hijos: obtener el sucesor inorden
            sucesor = self._encontrar_minimo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar(nodo.derecho, sucesor.valor)

        # Balancear el nodo actual después de la eliminación
        return self.balancear(nodo)

    def _encontrar_minimo(self, nodo: Nodo) -> Nodo:
        """Encuentra el nodo con el valor mínimo en un subárbol.

        Args:
            nodo: Nodo raíz del subárbol.

        Returns:
            El nodo con el valor mínimo.
        """
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    def buscar(self, valor: int) -> bool:
        """Busca un valor dentro del árbol.

        Args:
            valor: Valor que se desea buscar.

        Returns:
            True si el valor existe; False en caso contrario.
        """
        nodo = self.raiz

        while nodo is not None:
            if valor == nodo.valor:
                return True

            if valor < nodo.valor:
                nodo = nodo.izquierdo
            else:
                nodo = nodo.derecho

        return False

    def _contar_nodos(self, nodo: Nodo | None) -> int:
        # None aquí significa "no hay nodo", no "empieza desde la raíz".
        if nodo is None:
            return 0
        return 1 + self._contar_nodos(nodo.izquierdo) + self._contar_nodos(nodo.derecho)

    def contar_nodos(self, nodo: Nodo | None = None) -> int:
        """Cuenta el número de nodos en el árbol"""
        if nodo is None:
            nodo = self.raiz

        return self._contar_nodos(nodo)
    
# =========================================
# Recorridos del árbol
# =========================================
    def inorden(self, nodo: Nodo | None = None) -> list:
        """Recorrido Inorden: Izquierda, Raíz, Derecha."""
        if nodo is None:
            nodo = self.raiz
        return self._recorrido_inorden(nodo)

    def _recorrido_inorden(self, nodo: Nodo | None) -> list:
        if nodo is None:
            return []
        return (
            self._recorrido_inorden(nodo.izquierdo)
            + [nodo.valor]
            + self._recorrido_inorden(nodo.derecho)
        )

    def preorden(self, nodo: Nodo | None = None) -> list:
        """Recorrido Preorden: Raíz, Izquierda, Derecha."""
        if nodo is None:
            nodo = self.raiz
        return self._recorrido_preorden(nodo)

    def _recorrido_preorden(self, nodo: Nodo | None) -> list:
        if nodo is None:
            return []
        return (
            [nodo.valor]
            + self._recorrido_preorden(nodo.izquierdo)
            + self._recorrido_preorden(nodo.derecho)
        )

    def postorden(self, nodo: Nodo | None = None) -> list:
        """Recorrido Postorden: Izquierda, Derecha, Raíz."""
        if nodo is None:
            nodo = self.raiz
        return self._recorrido_postorden(nodo)

    def _recorrido_postorden(self, nodo: Nodo | None) -> list:
        if nodo is None:
            return []
        return (
            self._recorrido_postorden(nodo.izquierdo)
            + self._recorrido_postorden(nodo.derecho)
            + [nodo.valor]
        )
# =========================================
    def to_dict(self):
        """Convierte el árbol a diccionario para visualización"""
        return {
            'arbol': self.raiz.to_dict() if self.raiz else None,
            'altura': self.obtener_altura(self.raiz),
            'total_nodos': self.contar_nodos(),
            'inorden': self.inorden(),
            'preorden': self.preorden(),
            'postorden': self.postorden(),
        }
