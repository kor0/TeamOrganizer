from flask import render_template
from flask_appbuilder import expose, has_access
from flask_appbuilder import ModelView
from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
from app import appbuilder, db
from .models import Team, Employee, Gender, Proj, Client, Stack, Action, Languages

"""
Views 
"""
class EmployeeModelView(ModelView):
    datamodel = MongoEngineInterface(Employee)

    label_columns = {'team':'Team'}
    list_columns = ['name','prefered_area','team']

    show_fieldsets = [
        ('Summary',{'fields':['name', 'user', 'team']}),
        ('Assets',{'fields':['prefered_activity','prefered_language', 'prefered_area', 'years_experience'],'expanded':False}),
        ]
appbuilder.add_view(EmployeeModelView, "List Employees",category = "Employees")

class ClientModelView(ModelView):
    datamodel = MongoEngineInterface(Client)
appbuilder.add_view(ClientModelView, "List Clients",category = "Clients")

class ProjectModelView(ModelView):
    datamodel = MongoEngineInterface(Proj)
    related_views = [ClientModelView]
appbuilder.add_view(ProjectModelView, "List Projects",category = "Projects")

class TeamModelView(ModelView):
    datamodel = MongoEngineInterface(Team)
    related_views = [EmployeeModelView]
appbuilder.add_view(TeamModelView, "List Teams",category = "Teams")


#class LanguagesModelView(ModelView):
#    datamodel = MongoEngineInterface(Languages)
#appbuilder.add_view(LanguagesModelView, "List Languages",category = "Teams")

#class T3(ModelView):
 #   datamodel = MongoEngineInterface(Stack)
#appbuilder.add_view(T3, "T3",category = "To")


#class T2(ModelView):
 #   datamodel = MongoEngineInterface(Gender)
#appbuilder.add_view(T2, "T2",category = "To")

#
#class T1(ModelView):
 #   datamodel = MongoEngineInterface(Action)
#appbuilder.add_view(T1, "T1",category = "To")
#

#appbuilder.security_cleanup()
"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404
