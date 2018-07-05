from mongoengine import Document
from mongoengine import DateTimeField, StringField, ReferenceField, ListField, IntField
from flask_appbuilder.security.mongoengine.manager import SecurityManager
from flask_appbuilder.security.mongoengine.models import User

"""

Define you MongoEngine Models here

"""
class Team(Document):
    name = StringField(max_length = 60, required = True, unique = True)
    desc = StringField(max_length = 60, required = True, unique = True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Proj(Document):
    name = StringField(max_length = 60, required = True, unique = True)
    desc = StringField(max_length = 60, required = True, unique = True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Gender(Document):
    name = StringField(max_length=60, required=True, unique=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __str__(self):
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
    user = ReferenceField(User, required=True, unique=True)
    name = StringField(max_length=60)
    personal_phone = StringField(max_length=20)
    personal_celphone = StringField(max_length=20)
    team = ReferenceField(Team)
    gender = ReferenceField(Gender, required=True)
    prefered_language = ListField(ReferenceField(Languages, required = True))
    prefered_area = ReferenceField(Stack, required = True)
    prefered_activity = ListField(ReferenceField(Action, required = True))
    years_experience = IntField(required=True)

class Client(Document):
    user = ReferenceField(User, required=True, unique=True)
    name = StringField(max_length=60, required=True, unique=True)
    personal_phone = StringField(max_length=20)
    personal_celphone = StringField(max_length=20)
    project = ReferenceField(Proj)

def fillGender():
    male = Gender(name='Male')
    male.save()
    female = Gender(name='Female')
    female.save()

def fillStack():
    back = Stack(name='Back-end')
    back.save()
    front = Stack(name='Front-end')
    front.save()
    full = Stack(name='Fullstack')
    full.save()

def fillLanguages():
    java = Languages(name='Java')
    java.save()
    js = Languages(name='Javascript')
    js.save()
    go = Languages(name='Golang')
    go.save()
    py = Languages(name='Python')
    py.save()
    sw = Languages(name='Swift')
    sw.save()
 
def fillAction():
    req = Action(name='Requirements')
    req.save()
    des = Action(name='Design')
    des.save()
    cod = Action(name='Coding')
    cod.save()
    test = Action(name='Testing')
    test.save()
    proj = Action('Project Management')
    proj.save()
    man = Action('Maintenance')
    man.save()
 

#fillGender()
fillLanguages()
fillAction()
fillStack()
