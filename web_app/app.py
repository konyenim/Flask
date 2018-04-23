from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('setting.py')

    @app.route('/')
    def index():
        return render_template('index.html', TITTLE='nitnot')

    @app.route('/about')
    def about():
        return render_template('about.html', TITTLE='nitnot')

    @app.route('/news')
    def news():
        return render_template('news.html', TITTLE='nitnot')

    return app

