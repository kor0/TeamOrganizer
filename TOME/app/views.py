from flask import render_template
from flask_appbuilder import expose, has_access
from flask_appbuilder import ModelView
from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
from app import appbuilder
from .models import Team, Employee, Tags, Gender
"""
    Define you Views here
"""

class EmployeeModelView(ModelView):
    datamodel = MongoEngineInterface(Employee)

    label_columns = {'team':'Team'}
    list_columns = ['name','personal_celphone','team']

    show_fieldsets = [
        ('Summary',{'fields':['name','address','contact_group']}),
        ('Personal Info',{'fields':['personal_phone','personal_celphone'],'expanded':False}),
        ]
appbuilder.add_view(EmployeeModelView, "List Employees",icon = "fa-envelope",category = "Teams")

class TeamModelView(ModelView):
    datamodel = MongoEngineInterface(Team)
    related_views = [EmployeeModelView]
appbuilder.add_view(TeamModelView, "List Teams",icon = "fa-folder-open-o",category = "Teams",
                category_icon = "fa-envelope")

#class GenderView(ModelView):
#    datamodel = MongoEngineInterface(Gender)
#appbuilder.add_view(GenderView, "List Gender",icon = "fa-envelope",category = "Gender")

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

