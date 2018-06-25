from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, IntField

"""

Define you MongoEngine Models here

"""

class Team(Document):
    name = StringField(max_length = 60, required = True, unique = True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

class Gender(Document):
    name = StringField(max_length=60, required=True, unique=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Tags(Document):
    name = StringField(max_length=60, required=True, unique=True)

    def __unicode__(self):
        return self.name

class Languages(Document):
    name = StringField(max_length=60, required=True, unique=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Stack(Document):
    name = StringField(max_length=60, required=True, unique=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Action(Document):
    name = StringField(max_length=60, required=True, unique=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Employee(Document):
    name = StringField(max_length=60, required=True, unique=True)
    address = StringField(max_length=60)
    personal_phone = StringField(max_length=20)
    personal_celphone = StringField(max_length=20)
    team = ReferenceField(Team, required=True)
    gender = ReferenceField(Gender, required=True)
    tags = ListField(ReferenceField(Tags))
    prefered_language = ReferenceField(Languages, required = True)
    prefered_area = ReferenceField(Stack, required = True)
    prefered_activity = ReferenceField(Action, required = True)
    years_experience = IntField(required=True)



