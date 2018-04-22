from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'halo flask'

    @app.route('/about')
    def about():
        return 'tentang flask'

    @app.route('/beranda')
    def beranda():
        return 'welcome to my website'

    return app

