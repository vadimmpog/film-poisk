from database import db


class Model:
    errors = []

    def __init__(self):
        self.id = None

    def validate(self):
        self.errors = []
        return len(self.errors) == 0

    def save(self):
        if self.validate():
            if self.id is None:
                db.session.add(self)
            db.session.commit()
            return True
        else:
            return False

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(db.Model, Model):
    __tablename__ = 'user'
    pass


class Cinema(db.Model, Model):
    __tablename__ = 'cinema'
    pass


class Movie(db.Model, Model):
    __tablename__ = 'movie'
    pass

