r"""Fase 2: recorridos de un árbol de expresión construido a mano.

Este script es temporal y se sustituirá por la CLI del proyecto en la Fase 6.
"""

from src.node import Node
from src.tree import ExpressionTree


def build_sample_tree() -> ExpressionTree:
    r"""Construye a mano el árbol de la expresión ``3 + 5 * 2``.

            +
           / \
          3   *
             / \
            5   2
    """
    three = Node("3")
    five = Node("5")
    two = Node("2")

    multiplication = Node("*", five, two)
    root = Node("+", three, multiplication)

    return ExpressionTree(root)


def main() -> None:
    tree = build_sample_tree()

    print(f"Inorden   (infija):  {' '.join(tree.inorder())}")
    print(f"Preorden  (prefija): {' '.join(tree.preorder())}")
    print(f"Postorden (posfija): {' '.join(tree.postorder())}")


if __name__ == "__main__":
    main()
