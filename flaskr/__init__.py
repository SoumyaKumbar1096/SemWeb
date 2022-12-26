import os
from flask import Flask

#application factory function
def create_app(test_config=None):
    #create and configure the app

    #creates a Flask instance
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #a simple page that says Hello

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app