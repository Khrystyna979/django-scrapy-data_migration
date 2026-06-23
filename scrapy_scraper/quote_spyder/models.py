from mongoengine import Document
from mongoengine.fields import ListField, StringField, ReferenceField, BooleanField
import db_config

class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)
    meta = {'collection': 'authors'}
    
class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField('Author', dbref=False)
    quote = StringField()
    meta = {'collection': 'quotes'}
    
class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True, unique=True)
    address = StringField()
    phone_number = StringField()
    preferred_method = StringField(choices=('email', 'sms'), required=True)
    is_sent = BooleanField(default=False)
    meta = {'collection': 'contacts'}