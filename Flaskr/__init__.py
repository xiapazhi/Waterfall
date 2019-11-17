# __init__.py 有两个作用：一是包含应用工厂；二是 告诉 Python flaskr 文件夹应当视作为一个包。
import os
import sys
import logging
from flask import Flask
from .routes import initializeRoutes
from flask.logging import default_handler


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # instance_relative_config=True 告诉应用配置文件是相对于 instance folder (实例文件夹)的相对路径。
    # 实例文件夹在 flaskr 包的外面，用于存放本地数据（例如配置密钥和数据库），不应当 提交到版本控制系统。
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        environment = app.config['ENV']
        if environment == 'development':
            app.config.from_pyfile('config.conf', silent=False)
            # config_log(environment)
        else:
            pass
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    initializeRoutes(app)
    return app


def config_log(env):
    if env == 'development':
        pass
    elif env == 'production':
        # file_handler = logging.FileHandler(
        #     filename='log_massage.log', encoding="utf-8")
        # formatter = logging.Formatter(
        #     '%(asctime)s -|- %(levelname)s -|- %(message)s')
        # file_handler.setFormatter(formatter)
        # logging.getLogger().setLevel(logging.warning)
        # logger = logging.getLogger(__name__)
        # logger.addHandler(file_handler)
        pass
