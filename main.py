import sys
from src.parser import Parser
from src.tree import ExpressionTree
from src.evaluator import Evaluator
from src.exceptions import MalformedExpressionError, DivisionByZeroTreeError

def print_menu():
    print("\n" + "="*50)
    print("🌳 CALCULADORA CON ÁRBOLES DE EXPRESIÓN 🌳")
    print("="*50)
    print("1. Ingresar nueva expresión matemática (Infija)")
    print("2. Ver recorrido Posorden (Notación Posfija)")
    print("3. Ver recorrido Preorden (Notación Prefija)")
    print("4. Ver recorrido Inorden (Notación Infija con paréntesis)")
    print("5. Evaluar la expresión (Resolver)")
    print("6. Salir")
    print("="*50)

def main():
    tree = ExpressionTree()
    evaluator = Evaluator()
    
    while True:
        print_menu()
        opcion = input("Elige una opción (1-6): ").strip()
        
        if opcion == '1':
            expr = input("\nIngresa la expresión matemática (ej. 3 + 5 * (2 - 8)): ")
            try:
                parser = Parser(expr)
                tree.root = parser.parse()
                print("✅ Árbol construido correctamente en memoria.")
            except MalformedExpressionError as e:
                print(f"❌ Error de sintaxis: {e}")
            except Exception as e:
                print(f"❌ Error inesperado: {e}")
                
        elif opcion == '2':
            if not tree.root:
                print("⚠️ Primero debes ingresar una expresión (Opción 1).")
            else:
                posfija = " ".join(tree.postorder(tree.root))
                print(f"\n📌 Notación Posfija (Postorden): {posfija}")
                
        elif opcion == '3':
            if not tree.root:
                print("⚠️ Primero debes ingresar una expresión (Opción 1).")
            else:
                prefija = " ".join(tree.preorder(tree.root))
                print(f"\n📌 Notación Prefija (Preorden): {prefija}")
                
        elif opcion == '4':
            if not tree.root:
                print("⚠️ Primero debes ingresar una expresión (Opción 1).")
            else:
                infija = " ".join(tree.inorder(tree.root))
                print(f"\n📌 Notación Infija reconstruida (Inorden): {infija}")
                
        elif opcion == '5':
            if not tree.root:
                print("⚠️ Primero debes ingresar una expresión (Opción 1).")
            else:
                try:
                    resultado = evaluator.evaluate(tree.root)
                    print(f"\n🚀 Resultado de la evaluación: {resultado}")
                except DivisionByZeroTreeError as e:
                    print(f"❌ Error al evaluar: {e}")
                except Exception as e:
                    print(f"❌ Error inesperado durante la evaluación: {e}")
                    
        elif opcion == '6':
            print("\nSaliendo del programa. ¡Hasta luego! 👋")
            sys.exit(0)
            
        else:
            print("⚠️ Opción no válida. Por favor, elige un número del 1 al 6.")

if __name__ == "__main__":
    main()
