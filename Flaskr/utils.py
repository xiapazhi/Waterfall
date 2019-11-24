from flask import current_app
from . import db


def allowed_file(filename):
    config = current_app.config
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config['ALLOWED_EXTENSIONS']


def get_picture(already=[]):
    try:
        # searchSql = 'SELECT * FROM picture WHERE id NOT IN ( 26,27,28)'
        searchSql = f"SELECT * FROM picture"
        if len(already) > 0:
            alreadyStr = ','.join([str(id) for id in already])
            searchSql = searchSql + " WHERE id NOT IN (" + alreadyStr + ")"
        searchSql = searchSql + " LIMIT 15"
        sqlite = db.connect_db()
        cursor = sqlite.cursor()
        cursor.execute(searchSql)
        return cursor.fetchall()
    except Exception as e:
        warning(e)


def warning(e):
    current_app.logger.warning(e)
