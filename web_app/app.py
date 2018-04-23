from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'halo flask, ini hot reload yaaa !!!!'

    return app

