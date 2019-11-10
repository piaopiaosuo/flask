import os

from flask import Flask


def create_app(test_config=None, *args):
    print(*args)
    # create and configure the app
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__, )
    app.config.from_mapping(
    #     SECRET_KEY='abcd',
    #     DEBUG=True,
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    #     accesslog="log/access.log",
    #     errorlog="log/debug.log",
    #     loglevel="debug"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        print(123)
        # app.config.from_pyfile('config.py', silent=True)
        app.config.from_object("config.ProductionConfig")
        print(app.config)
        print(567)
    else:
        # load the test config if passed in
        # app.config.from_mapping(test_config)
        app.config.from_pyfile('config.py', silent=True)
        # app.config.from_object("config.ProductionConfig")
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
