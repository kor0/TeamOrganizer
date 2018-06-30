# TeamOrganizer
This projects is made with flask and some architectural patterns for a Software Engineering class.



<h1>Business Requirements</h1>
<b>TOME - Team Organization Made Easy</b>
<h2>Background:</h2>
    Organizing teams has been a normal problem throughout Industry, mainly as consequence of unbalanced knowledge spread among teams, leading to projects with much better teams than it needs and projects with much worse teams than it requires. As consequence, some projects are bound to end unfinished or with several bugs, while others finish early and the team ends up idle. 

<h2>Business Case:</h2>
    Team Organization becomes a critical area in the optimization of overall results in an organization with several teams and projects. This project is designed to help the building of teams, aiming to help managers to assign balanced teams to projects of the proper dificulty (taking as account the team experience and prefered KA's). Projects come and go, TOME helps managers to watch all current projects and allow stakeholders to create new projects.

<h2>Goals & Objectives:</h2>

| Timeline | Goal | Measurement |
| ------------- | ------------- | ------------- |
| time 0, speed.1 | Increase the speed managers take to assign a team to a project | Mean Time to Create Team (MTCT) < x minutes |
| time 0, speed.2 | Increase the speed employees take to register their overall information + prefered environment of work | Mean Time to Register Employee (MTRE) < y minutes |
| time 0, speed.3 | Increase the speed stakeholders take to register a new projects | Mean Time to Register Project (MTRP) < z minutes|
| time 0, balance.1 | Increase balance of knowledge of employees in a given team |  Mean Knowledge of Employees/ Dificulty of Project (MKEbDP) < constant x|
| time 0, balance.2 | Increase balance of MKEbPD for all projects | Mean MKEbPD/ Number of Projects (MMbNP) < constant y | 
| time 0, team_satisfaction.1 | Increase employee satisfaction of working with prefered KA's | Mean Prefered KA/ Team (MPKAbT) < constant z |

<h2>Assumptions:</h2>

| Type | Assumption |
| --- | --- |
| Scope | Prefered Technologies (KA's) available are limited to a pre-selected group. Employees won't be able to cite KA's outside this group as Prefence. |
| Environment | The solution will optmize the standard method of team organization. |

<h2>Constraints:</h2>

| Type | Constraint |
| --- | --- |
| Financial | No budget. |
| Schedule | The project must be launched by 07/07/2018 in order to meet the objectives in the business case. |
| Facilities & Infrastructure | The project team will use existing office space and IT infrastructure such as computing equipment and networks. |

<h2>Functional Requirements:</h2>

| Type | Requirement |
| --- | --- |
| Correlation | The system will automatically determine which employees are bound to which project. |

<h2>Non-functional Requirements:</h2>

| Type | Non-Functional Requirement |
| --- | --- |
| Security | The system will protect user data against malicious attacks. |
| Security | The system will allow only authenticated users to access authorized data. |
| Information Technology | The system will be designed for enough availability as to be reliable on a academic simulation of the system. |


<h1>Architectural Structure</h1>

<h2>Mongo Engine</h2>
<p>MongoEngine is an Object-Document Mapper, written in Python for working with MongoDB. 
MongoEngine is currently tested against MongoDB v2.4, v2.6, and v3.0.</p>
<p>In MongoDB, a document is roughly equivalent to a row in an RDBMS. When working with relational databases, rows are stored in tables, which have a strict schema that the rows follow. MongoDB stores documents in collections rather than tables — the principal difference is that no schema is enforced at a database level.</p>
<p>MongoEngine allows you to define schemata for documents as this helps to reduce coding errors, and allows for utility methods to be defined on fields which may be present.
To define a schema for a document, create a class that inherits from Document. Fields are specified by adding field objects as class attributes to the document class. This is how the schema of the Employee is structured in the models.py of this project:</p>

```python
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
```

<h2>Flask</h2>
Flask is a microframework for Python based on Werkzeug and Jinja 2.
<h2>flask-app-builder</h2>
Simple and rapid application development framework, built on top of Flask. Includes detailed security, auto CRUD generation for your models, google charts and much more.
