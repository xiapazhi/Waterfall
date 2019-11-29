from flask import current_app
from . import db
import random


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


def warning(e):
    current_app.logger.warning(e)
