import os
import uuid
import time

from flask import render_template, url_for, request, jsonify, flash
from werkzeug.utils import secure_filename

from app import app, db, full_path_photos, ALLOWED_EXTENSIONS
import json

from constants import TEMP_PATH
from models.animal import Animal


@app.route('/get_type', methods=['GET', 'POST'])
def get_type_animal():
    if request.method == 'POST':
        try:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = str(uuid.uuid1()) + "_" + str(time.time()) + "." + filename.split('.')[1]
                file.save(os.path.join(TEMP_PATH, filename))  # сохраняем файл
        except FileNotFoundError as e:
            print(e)
            flash("Ошибка чтения файла", "error")  # всплывающее сообщение
    return render_template("get_type_animal.html")

#   По идее надо добавить только это кусок кода чтоб работало с нейронкой
#     classified = classify_animal_image(os.path.join(TEMP_PATH, filename)
#     if classified == 'cat':
#         os.replace(tempPath, CATS_PATH + "/" + fileName)
#     elif classified == 'dog':
#         os.replace(tempPath, DOGS_PATH + "/" + fileName)
#     else:
#         os.replace(tempPath, OTHERS_PATH + "/" + fileName)
#


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def home_page():
    return render_template("index.html")


@app.route('/rate_animals', methods=['GET', 'POST'])
def rate_animals():
    if request.method == 'POST':
        name_photo = request.form.get('img_animal')  # запрос к данным формы
        like = request.form.get('like')
        session = db.session
        if like is not None:
            animal: Animal = session.query(Animal).get(name_photo)
            animal.count_liked += 1
            session.add(animal)
            session.commit()
        else:
            animal: Animal = session.query(Animal).get(name_photo)
            animal.count_unliked += 1
            session.add(animal)
            session.commit()
        session.close
    #print(full_path_photos)
    return render_template("rate_animal.html", data=json.dumps(full_path_photos))


@app.route('/about_animals', methods=['GET'])
def about_animal():
    return render_template("about_animals.html", data=json.dumps(full_path_photos))



