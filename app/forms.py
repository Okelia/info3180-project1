from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PropertyForm(FlaskForm):
    property_title = TextField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rooms = TextField('No. of Rooms', validators=[DataRequired()])
    bathrooms = TextField('No. of Bathrooms', validators=[DataRequired()])
    price = TextField('Price', validators=[DataRequired()])
    property_type = SelectField("Property Type", choices=[('Apartment'), ('House')])
    location = TextField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only'])])
    name= TextField()
