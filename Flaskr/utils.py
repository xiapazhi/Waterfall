from flask import current_app

def allowed_file(filename):
    config = current_app.config
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config['ALLOWED_EXTENSIONS']