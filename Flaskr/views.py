import os
from .utils import allowed_file
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
        files_dict = request.files.to_dict()
        base_path = os.getcwd()  # os.getcwd() 获取当前文件/包所在绝对路径
        for v in files_dict.values():
            if v and allowed_file(v.name):
                filename = secure_filename(v.name)
                storage_path = os.path.normpath(os.path.join(
                    base_path, config['UPLOAD_FOLDER'], filename))
                v.save(storage_path)
    except Exception as e:
        pass
    return '1233223'
