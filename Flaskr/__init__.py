# __init__.py 有两个作用：一是包含应用工厂；二是 告诉 Python flaskr 文件夹应当视作为一个包。

import os
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        environment = app.config['ENV']
        if environment == 'development':
            app.config.from_pyfile('config.py', silent=True)
        else:
            pass
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

     # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, sWorld!'

    return app
