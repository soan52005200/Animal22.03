import os

from sqlalchemy import exists

from app import app, full_path_photos, db
from models.animal import Animal, TYPES_ANIMALS


if __name__ == "__main__":

    db.create_all() # создаем таблицы в бд

    session = db.session

    for i, url_photo in enumerate(full_path_photos):
        name_photo = url_photo.split('/')[3]
        type_animal = url_photo.split('/')[2]
        name_photo = name_photo.split('.')[0]
        if not session.query(exists().where(Animal.name_photo == name_photo)).scalar():
            animal: Animal = Animal(name_photo=name_photo, count_liked=0, count_unliked=0)
            if type_animal == "others":
                animal.type_animal = TYPES_ANIMALS[2]
            elif type_animal == "dogs":
                animal.type_animal = TYPES_ANIMALS[0]
            elif type_animal == "cats":
                animal.type_animal = TYPES_ANIMALS[1]
            session.add(animal)
            session.commit()
    session.close()

    app.run()
