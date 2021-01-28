from wtforms_alchemy import ModelForm
from sqlalchemy import create_engine
import transaction
from .models.mymodel import User, Holiday
from wtforms import BooleanField, Form, StringField, DateField, validators
from sqlalchemy.orm import sessionmaker

class HolidayForm(Form):
    name = StringField('name', [validators.Length(min=4, max=60)])
    date = DateField('Date', [validators.DataRequired()])

class UserForm(ModelForm):
    class Meta:
        model = User

