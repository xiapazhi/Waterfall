# 和 router 直接关联的写在这里 其他的写在 utils 哈哈哈哈哈
import os
import json
from . import db
from .utils import allowed_file, get_picture, warning
from werkzeug.utils import secure_filename
# secure_filename('../../../../home/username/.bashrc') ==> 'home_username_.bashrc'
from flask import render_template, current_app, flash, request, redirect, url_for


def test():
    config = current_app.config
    current_app.logger.info('测试 INFO testing')
    current_app.logger.warning('测试 WARNING testing')
    return render_template('test.html', name='YUAN', testParams1={"key": "value"}, testParams2={'key': config['DATABASE']})


def uploadView():

    return render_template('upload.html')


def uploadImgs():
    try:
        config = current_app.config
        sqlite = db.connect_db()
        cursor = sqlite.cursor()
        files_dict = request.files.to_dict()
        base_path = os.getcwd()  # os.getcwd() 获取当前文件/包所在绝对路径
        for v in files_dict.values():
            if v and allowed_file(v.name):
                filename = secure_filename(v.name)
                cursor.execute(
                    f"SELECT count(*) AS num FROM picture WHERE name='{filename}'")
                if cursor.fetchone()["num"] == 0:
                    storage_path = os.path.normpath(os.path.join(
                        base_path, config['UPLOAD_FOLDER'], filename))
                    v.save(storage_path)
                    cursor.execute(
                        f"INSERT INTO picture(name) VALUES('{filename}')")
                    sqlite.commit()
        db.close_db()
    except Exception as e:
        warning(e)
    return ''

# pictures = get_picture()
    # return render_template('test.html', init_pictures=pictures)


def view_page():
    pictures = get_picture()
    picture_ids = []
    for p in pictures:
        picture_ids.append(p['id'])
    return render_template('view.html', init_pictures=pictures, pictureIds=picture_ids)


def view_more():
    try:
        alreadyIds = json.loads(request.data)
        pictures = get_picture(alreadyIds['alreadyIds'])
        data = []
        for row in pictures:
            data.append({
                'id':row['id'],
                'name':row['name']
            })
        pictures_json = json.dumps(data)
        return pictures_json
    except Exception as e:
        warning(e)
