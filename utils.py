import os

from flask import flash, redirect, request
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file(path, file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        if not os.path.exists(path):
            os.makedirs(path)
        file.save(os.path.join(path, filename))
        return os.path.join(path, filename)
