from . import db

class NewProperty(db.Model):
    __tablename__ = 'new_properties'

    id = db.Column(db.Integer, primary_key=True)
    property_title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    rooms = db.Column(db.String(80))
    bathrooms = db.Column(db.String(80))
    price = db.Column(db.String(80))
    property_type = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(255))
        

    def __init__(self, property_title, description, rooms, bathrooms, price, property_type, location, photo):
        self.property_title = property_title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
        self.photo = photo

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
