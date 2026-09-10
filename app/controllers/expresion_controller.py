from flask import Blueprint, render_template, request, jsonify, session
from app.models.ABExpresiones.arbol_expresion import ArbolExpresion

expresion_bp = Blueprint('expresion', __name__)


@expresion_bp.route('/expresion')
def expresion():
    """Página principal del árbol de expresión"""
    return render_template('expresion.html')


@expresion_bp.route('/expresion/construir', methods=['POST'])
def construir_expresion():
    """API para construir el árbol de expresión"""
    try:
        data = request.get_json()
        expresion = data.get('expresion', '')

        if not expresion:
            return jsonify({'error': 'Expresión vacía'}), 400

        # Parsear → árbol → evaluar. El JSON incluye la jerarquía para D3.
        arbol = ArbolExpresion()
        arbol.construir_desde_expresion(expresion)
        session['ultima_expresion'] = expresion

        return jsonify({
            'success': True,
            'data': arbol.to_dict()
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@expresion_bp.route('/expresion/evaluar', methods=['POST'])
def evaluar_expresion():
    """API para evaluar la expresión"""
    try:
        data = request.get_json()
        expresion = data.get('expresion', '')

        arbol = ArbolExpresion()
        arbol.construir_desde_expresion(expresion)
        resultado = arbol.evaluar()

        return jsonify({
            'success': True,
            'expresion': expresion,
            'resultado': resultado
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400
