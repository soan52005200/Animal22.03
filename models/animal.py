from app import db

TYPES_ANIMALS = ['dog', 'cat', 'other']

class Animal(db.Model):
    __tablename__ = 'photo_animals'
    name_photo = db.Column(db.String(100), primary_key=True)
    count_liked = db.Column(db.Integer, nullable=False)
    count_unliked = db.Column(db.Integer, nullable=False)
    type_animal = db.Column(db.String(10), nullable=False)

