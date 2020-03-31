from flask import current_app
import os
import sys
from . import db
import random
from . import scheduler

def test():
    print(__name__)

def allowed_file(filename):
    config = current_app.config
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config['ALLOWED_EXTENSIONS']


def get_picture(already=[]):
    try:
        sqlite = db.connect_db()
        cursor = sqlite.cursor()

        searchMaxIdSql = 'SELECT MAX(id) FROM picture'
        cursor.execute(searchMaxIdSql)
        maxIdRaw = cursor.fetchone()
        maxId = maxIdRaw[0]

        searchAllSql = 'SELECT id FROM picture'
        cursor.execute(searchAllSql)
        allPicIdRaw = cursor.fetchall()
        picIdList = []
        for row in allPicIdRaw:
            picIdList.append(row['id'])

        diffNum = len(picIdList) - len(already)
        realSearchIds = []
        searchNum = 0

        if diffNum > 0:
            if diffNum > 30:
                searchNum = 30
            else:
                searchNum = diffNum
            while len(realSearchIds) < searchNum:
                currRandonId = random.randint(1, maxId)
                if picIdList.count(currRandonId) > 0 and already.count(currRandonId) == 0 and realSearchIds.count(currRandonId) == 0:
                    realSearchIds.append(currRandonId)
            # searchSql = 'SELECT * FROM picture WHERE id NOT IN ( 26,27,28)'
        searchSql = f"SELECT * FROM picture"
        if len(already) > 0 or True:
            realSearchIdStr = ','.join([str(id) for id in realSearchIds])
            searchSql = searchSql + " WHERE id IN (" + realSearchIdStr + ")"
        searchSql = searchSql + " LIMIT 15"
        cursor.execute(searchSql)
        return cursor.fetchall()
    except Exception as e:
        warning(e)


def pic_already_have(filename):
    sqlite = db.connect_db()
    cursor = sqlite.cursor()
    cursor.execute(
        f"SELECT count(*) AS num FROM picture WHERE name='{filename}'")
    if cursor.fetchone()["num"] == 0:
        return False
    else:
        return True


def check_picture():
    try:
        with scheduler.scheduler.app.app_context():
            config = current_app.config
            sqlite = db.connect_db()
            cursor = sqlite.cursor()
            base_path = os.path.normpath(
                os.path.join(os.getcwd(),  config['UPLOAD_FOLDER']))
            dirs = os.listdir(base_path)
            for file in dirs:
                file_path = os.path.normpath(
                    os.path.join(base_path, file))
                file_size = os.path.getsize(file_path) / (1024 * 1024)
                if file_size <= 7 and not pic_already_have(file):
                    cursor.execute(
                        f"INSERT INTO picture(name) VALUES('{file}')")
                    sqlite.commit()
            # db.close_db()
    except Exception as e:
        warning(e)


def warning(e):
    current_app.logger.warning(e)
