from flask import Blueprint, render_template, request, jsonify
from app.models.ABB.ABB_AVL import ArbolAVL

busqueda_bp = Blueprint('busqueda', __name__)

# Un solo árbol en memoria: sirve para la demo, pero lo comparten todos los usuarios.
arbol_actual = ArbolAVL()


def _parse_numero(valor):
    """Normaliza el valor del formulario: 7.0 → 7 para que coincida la búsqueda."""
    numero = float(valor)
    if numero.is_integer():
        return int(numero)
    return numero


@busqueda_bp.route('/busqueda')
def busqueda():
    """Página principal del árbol de búsqueda"""
    return render_template('AVL.html')


@busqueda_bp.route('/busqueda/insertar', methods=['POST'])
def insertar_valor():
    """API para insertar un valor"""
    try:
        data = request.get_json()
        valor = _parse_numero(data.get('valor'))

        arbol_actual.insertar(valor)

        return jsonify({
            'success': True,
            'mensaje': f'Valor {valor} insertado correctamente',
            'data': arbol_actual.to_dict()
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@busqueda_bp.route('/busqueda/buscar', methods=['POST'])
def buscar_valor():
    """API para buscar un valor"""
    try:
        data = request.get_json()
        valor = _parse_numero(data.get('valor'))

        encontrado = arbol_actual.buscar(valor)

        return jsonify({
            'success': True,
            'valor': valor,
            'encontrado': encontrado
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@busqueda_bp.route('/busqueda/eliminar', methods=['POST'])
def eliminar_valor():
    """API para eliminar un valor"""
    try:
        data = request.get_json()
        valor = _parse_numero(data.get('valor'))

        if not arbol_actual.buscar(valor):
            return jsonify({
                'success': False,
                'mensaje': f'El valor {valor} no existe en el árbol'
            }), 404

        arbol_actual.eliminar(valor)

        return jsonify({
            'success': True,
            'mensaje': f'Valor {valor} eliminado correctamente',
            'data': arbol_actual.to_dict()
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@busqueda_bp.route('/busqueda/estado', methods=['GET'])
def obtener_estado():
    """API para obtener el estado actual del árbol"""
    return jsonify({
        'success': True,
        'data': arbol_actual.to_dict()
    })


@busqueda_bp.route('/busqueda/reiniciar', methods=['POST'])
def reiniciar_arbol():
    """API para reiniciar el árbol"""
    global arbol_actual
    arbol_actual = ArbolAVL()

    return jsonify({
        'success': True,
        'mensaje': 'Árbol reiniciado correctamente',
        'data': arbol_actual.to_dict()
    })
