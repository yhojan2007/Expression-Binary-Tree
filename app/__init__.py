from flask import Flask


def create_app():
    """Crea la aplicación Flask y registra las dos pantallas (expresión y AVL)."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456789'

    # Registrar controladores (Blueprints)
    from app.controllers.expresion_controller import expresion_bp
    from app.controllers.avl_controller import busqueda_bp

    app.register_blueprint(expresion_bp)
    app.register_blueprint(busqueda_bp)

    # Ruta principal
    from flask import render_template

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
