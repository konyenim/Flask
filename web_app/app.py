from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('setting.py')

    db = SQLAlchemy(app)
    class Page(db.Model):
        __tablename_='page'
        id = Column(Integer, primary_key=True)
        contents = Column(String)


    db.create_all()


    @app.route('/nitnot')
    def nitnot():
        page = Page.query.filter_by(id=1).first()
        return render_template('index.html', TITTLE='nitnot', CONTENT=page.contents)

    @app.route('/')
    def index():
        return render_template('index.html', TITTLE='nitnot')

    @app.route('/about')
    def about():
        return render_template('about.html', TITTLE='nitnot')

    @app.route('/news')
    def news():
        return render_template('news.html', TITTLE='nitnot')

    @app.route('/testdb')
    def testdb():
        import psycopg2

        con = psycopg2.connect('dbname=Flask user=devuser password=devpassword host=postgres')
        cur = con.cursor()

        cur.execute('select * from page;')

        id, title =cur.fetchall()
        con.close()
        return 'output table page: {} - {}'.format(id, title)

    return app

