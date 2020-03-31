# __init__.py 有两个作用：一是包含应用工厂；二是 告诉 Python flaskr 文件夹应当视作为一个包。
import os
import sys
import logging
from flask import Flask
from flask_apscheduler import APScheduler
from .routes import initializeRoutes
from flask.logging import default_handler
from .db import init_app_db
from .utils import test, check_picture
from .scheduler import init_scheduler


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
        else:  # production
            app.config.from_pyfile('config.conf', silent=False)
            config_log(app)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    init_app_db(app)
    initializeRoutes(app)

    init_scheduler(app)

    return app


def config_log(app):
    logging.basicConfig(filename=os.path.join(
        app.instance_path, 'logger.log'))
