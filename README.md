# TeamOrganizer
<b>TOME - Team Organization Made Easy</b>
This projects is made with flask and some architectural patterns for a Software Engineering class.



<h1>Software Requirements Specification (Business Requirements Document)</h1>
<p><i>The SRS states the functions and capabilities that a software system must provide, its characteristics, and the constraints that it must respect. It should describe as completely as necessary the system's behaviours under various conditions, as well as desired system qualities such as perfomance, security and usability. The SRS is the basis for the subsequent project planning, design, and coding, as well as the foundation for system testing and user documentation. However, it should not contain design, construction, testing, or project management details other than known design and implement constraints.</i><p>

    
<h2>1. Introduction</h2>
<p><h3>1.1 Purpose</h3></p>
<p>Organizing teams has been a normal problem throughout Software Development Organizations, mainly as consequence of unbalanced knowledge spread among teams, leading to projects with much better teams than it needs and projects with much worse teams than it requires. As consequence, some projects are bound to end unfinished or with several bugs, while others finish early and the team ends up idle.</p> 

<p><h3>1.2 Document Conventions</h3></p>
<p> This document follows the guideline and template provided by the book <strong>Software Requirements - Third Edition by Karl Wiegers and Joy Beatty (Microsoft - Best Practices)</strong>, found as figure 10-2 at page 191, chapter 10.<p>
    
<p><h3>1.3 Project Scope</h3></p>
<p>Team Organization becomes a critical area in the optimization of overall results in an organization with several teams and projects. This project is designed to help the building of teams, aiming to help managers to assign balanced teams to projects of the proper dificulty (taking as account the team experience and prefered KA's). Projects come and go, TOME helps managers to watch all current projects and allow stakeholders to create new projects.</p>

<p><h3>1.4 References</h3></p>
<ol>
    <li><i>(http://www.nptel.ac.in/courses/Webcourse-contents/IIT%20Kharagpur/Soft%20Engg/pdf/m12L30.pdf)</i> Module 12, Lesson 30 - Organization and Team Structures - CSE ITT Kanpur</li>
    <li><i>(https://aws.amazon.com/elasticbeanstalk/details/)</i> AWS Elastic Beanstalk Features</li>
    <li><i>(https://aws.amazon.com/ec2/details/)</i> Amazon EC2 Product Details</li>
    <li><i>(https://aws.amazon.com/route53/details/)</i> Amazon Route 53 Product Details</li> 
</ol>

<h2>2. Overall Description</h2>
<p><h3>2.1 Product Perspective</h3></p>
<p>Usually every software development organization handles several projects at any time. Software organizations assign different teams of engineers to handle different software projects. Each type of organization structure has its ownadvantages and disadvantages so the issue “how is the organization as a whole structured?” must be taken into consideration so that each software project can be finished before its deadline[1].<p>
    
<p><h3>2.2 User Classes and Characteristics</h3></p>
<p><h4>2.2.1 Employee</h4></p>
<p>The employee registers itself on the system, providing information about it's prefered area of development, the technologies it knows best and how confident it feels with it's expertise. When assigned to a team, the employee receives an email with information about the project and the team it will be working with for the next iterations.</p>

<p><h4>2.2.2 Manager</h4></p>
<p>The manager has access to all manipulations of Teams, Employees and Projects. It is able to analyse the teams and projects and edit them. It is the most important stakeholder at the system requirements, since the main objective of TOME is to make it's job faster and easier.</p>

<p><h4>2.2.3 Client</h4></p>
<p>Clients post their projects with several information about what has to be accomplished. The team helps the client to express the requirements of the system in the long run, frequently updating the project blueprint.</p>

<p><h4>2.2.4 Admin</h4></p>
<p>The admin has full access to the CRUD of the system. It is there only to configure the system, give proper authorization to the users and help maintenance.</p>

<p><h3>2.3 Operating Environment</h3></p>
<p>The system is operating using AWS Elastic Beanstalk[2] + EC2[3] + Route 53[4], which provides high availability and good performance of the system. The system will be hosted with Route 53 to the URL http://pyrrhicbuddha.com. The server is running with Linux operating system, with a virtual environment with mongodb database, flask web framework and flask-app-builder microfamework and the source code.<p>
    
<p><h3>2.4 Design and Implementation Constraints</h3></p>

| Type | Constraint |
| --- | --- |
| Implementation | The project will be implemented in Python. |
| Implementation | The project will use MongoDB and MongoEngine for the database connection. |
| Implementation | The project will use Flask and flask-app-builder to build the main structure of the system. |
| Financial | No budget. |
| Schedule | The project must be launched by 07/07/2018 in order to meet the objectives in the business case. |
| Facilities & Infrastructure | The project team will use existing office space and IT infrastructure such as computing equipment and networks. |

<h2>Goals & Objectives:</h2>

| Timeline | Goal | Measurement |
| --- | --- | --- |
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

<h2>MongoDB <i>(https://github.com/mongodb/mongo)</i></h2>
<p>MongoDB is designed to meet the demands of modern apps with a technology foundation that enables you through:</p>
<ul>
    <li>The document data model – presenting you the best way to work with data.</li>
    <li>A distributed systems design – allowing you to intelligently put data where you want it.</li>
    <li>A unified experience that gives you the freedom to run anywhere – allowing you to future-proof your work and eliminate vendor lock-in.</li>
</ul>
<p>As an open source database, MongoDB can be run anywhere — from laptops and mainframes to a private cloud, public cloud. The developer experience is entirely unaffected by the deployment model chosen; similarly, those teams that want to maintain responsibility for running their own databases can also leverage a unified set of tools that deliver the same experience across different environments.</p>
<h3>Reference:</h3>
<i>https://docs.mongodb.com/manual/</i>

<h2>MongoEngine <i>(https://github.com/MongoEngine/mongoengine)</i></h2>
<p>MongoEngine is an Object-Document Mapper, written in Python for working with MongoDB. 
MongoEngine is currently tested against MongoDB v2.4, v2.6, and v3.0.</p>
<p>In MongoDB, a document is roughly equivalent to a row in an RDBMS. When working with relational databases, rows are stored in tables, which have a strict schema that the rows follow. MongoDB stores documents in collections rather than tables — the principal difference is that no schema is enforced at a database level.</p>

<h3>Schemata:</h3>
<p>MongoEngine allows you to define schemata for documents as this helps to reduce coding errors, and allows for utility methods to be defined on fields which may be present. To define a schema for a document, create a class that inherits from Document. Fields are specified by adding field objects as class attributes to the document class. This is how the schema of the Employee is structured in the models.py of this project:</p>

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

<h3>API Reference:</h3>
<i>http://docs.mongoengine.org/apireference.html</i>

<h2>Flask <i>(https://github.com/pallets/flask)</i></h2>
<p>Flask is a microframework for Python based on Werkzeug and Jinja 2. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. Flask is a lightweight WSGI web application framework. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.</p>

Flask offers suggestions, but doesn't enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.

<h3>API Reference:</h3>
<i>http://flask.pocoo.org/docs/1.0/api/</i>

<h2>flask-app-builder</h2>
Simple and rapid application development framework, built on top of Flask. Includes detailed security, auto CRUD generation for your models, google charts and much more.
<h3>API Reference:</h3>
<i>http://flask-appbuilder.readthedocs.io/en/latest/api.html</i>
