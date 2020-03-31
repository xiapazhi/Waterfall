# SQLite 数据库操作
import os
import click  # Click 是用 Python 写的一个第三方模块，用于快速创建命令行
import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext

# g 是一个特殊对象，独立于每一个请求。在处理请求过程中，它可以用于储存 可能多个函数都会用到的数据。
# 把连接储存于其中，可以多次使用，而不用在同一个 请求中每次调用 get_db 时都创建一个新的连接。


def init_db():
    db = connect_db()
    with current_app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())  # executescript() 是 SQLite 的方法 用来执行 sql 脚本
    # db.commit()

# 用 @click.command() 装饰一个函数，使之成为命令行接口
# 用 @click.option() 等装饰函数，为其添加命令行选项等
# 使用Flask应用的.cli.command()装饰器添加的命令在执行时自动推入应用上下文。
# 如果使用Click的command()装饰器添加命令，执行时不会自动推入应用上下文，要想达到同样的效果，增加with_appcontext装饰器：
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('初始化数据库成功！')


def connect_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            os.path.normpath(os.path.join(
                current_app.instance_path, current_app.config['DATABASE'])),
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # sqlite3.Row 告诉连接返回类似于字典的行，这样可以通过列名称来操作数据。
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


# close_db 和 init_db_command 函数需要在应用实例中注册，否则无法使用。
# 然而，既然我们使用了工厂函数，那么在写函数的时候应用实例还无法使用。
# 代替地， 我们写一个函数，把应用作为参数，在函数中进行注册。
def init_app_db(app):
    # app.teardown_appcontext() 告诉 Flask 在返回响应后进行清理的时候调用此函数。
    app.teardown_appcontext(close_db)
    # app.cli.add_command() 添加一个新的 可以与 flask 一起工作的命令。
    app.cli.add_command(init_db_command)
