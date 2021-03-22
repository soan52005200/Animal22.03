import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request

from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
from constants import TEMP_PATH, IMAGES_DIR

# создание экземпляра приложения
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #ограничиваем максимальный размер файла который можно загрузить 16 мегабайтами
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# инициализирует расширения
db = SQLAlchemy(app)

#возможные расширения загружаемых файлов
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# создаем список путей к файлам с картинками животных
full_path_photos = []

for root, dir, files in os.walk(IMAGES_DIR):
    files_in_dir = files
    for file in files_in_dir:
        if root + "/" != TEMP_PATH:
            full_path_photos.append(os.path.join(root[4:], file))


from . import views