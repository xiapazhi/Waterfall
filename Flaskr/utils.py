from flask import current_app
from . import db


def allowed_file(filename):
    config = current_app.config
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config['ALLOWED_EXTENSIONS']


def get_picture(already=[]):
    sqlite = db.connect_db()
    cursor = sqlite.cursor()
    cursor.execute(f"SELECT * FROM picture LIMIT 15")
    return cursor.fetchall()


def warning(e):
    current_app.logger.warning(e)
