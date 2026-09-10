# Documentación

Material de apoyo del visualizador de árboles binarios. El [README](../README.md) de la raíz explica cómo instalar y arrancar; aquí está el detalle de uso, diseño y algoritmos.

| Documento | Para qué leerlo |
|---|---|
| [uso.md](uso.md) | Operar las dos pantallas y conocer las restricciones de entrada |
| [arquitectura.md](arquitectura.md) | Cómo está organizado Flask, los modelos y el frontend |
| [arbol-expresion.md](arbol-expresion.md) | Gramática, parser, evaluación y notaciones |
| [arbol-avl.md](arbol-avl.md) | Inserción, borrado, factor de balance y rotaciones |
| [api.md](api.md) | Contrato HTTP entre el navegador y el backend |

Convención de nombres en el código: los hijos del nodo se llaman `izquierdo` y `derecho` (igual que el JSON que consume D3). La altura AVL de una hoja es `1`; un nodo `None` aporta altura `0`.
