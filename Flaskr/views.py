from flask import render_template, current_app, request, redirect, url_for


def test():
    config = current_app.config
    return render_template('test.html', name='YUAN', testParams1={"key": "value"}, testParams2={'key': config['DATABASE']})


def uploadView():

    return render_template('upload.html')


def uploadImgs():
    print(request)
    # print(request.files['file'])
    return '1233223'
