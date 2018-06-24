# TeamOrganizer
This projects is made with flask and some architectural patterns for a Software Engineering class.



<h1>Business Requirements</h1>
<b>TOME - Team Organization Made Easy</b>
<h2>Background:</h2>
    Organizing teams has been a normal problem throughout Industry, mainly as consequence of unbalanced knowledge spread among teams, leading to projects with much better teams than it needs and projects with much worse teams than it requires. As consequence, some projects are bound to end unfinished or with several bugs, while others finish early and the team ends up idle. 

<h2>Business Case:</h2>
    Team Organization becomes a critical area in the optimization of overall results in an organization with several teams and projects. This project is designed to auxiliate the building of teams, aiming to help managers to assign balanced teams to projects of the proper dificulty (taking as account the team experience and prefered KA's). Projects come and go, TOME helps managers to watch all vigent projects and allow stakeholders to create new projects.

<h2>Goals & Objectives:</h2>
    |Timeline | Goal | Measurement|
    |---|---|---|
    |speed.1 | Increase the speed managers take to assign a team to a project | Mean Time to Create Team (MTCT) < x minutes |
    |speed.2 | Increase the speed employees take to register their overall information + prefered environment of work | Mean Time to Register Employee (MTRE) < y minutes |
    |speed.3 | Increase the speed stakeholders take to register a new projects | Mean Time to Register Project (MTRP) < z minutes|
    |balance.1 | Increase balance of knowledge of employees in a given team |  Mean Knowledge of Employees/ Dificulty of Project (MKEbDP) < constant x|
    |balance.2 | Increase balance of MKEbPD for all projects | Mean MKEbPD/ Number of Projects (MMbNP) < constant y |
    |team_satisfaction.1 | Increase employee satisfaction of working with prefered KA's | Mean Prefered KA/ Team (MPKAbT) < constant z|

<h2>Assumptions:</h2>
    |Type | Assumption|
    |---|---|
    |Scope | Prefered Technologies (KA's) available are limited to a pre-selected group. Employees won't be able to cite KA's outside this group as Prefence.|
    |Environment | The solution will optmize the standard method of team organization.|

<h2>Constraints:</h2>
    |Type | Constraint|
    |---|---|
    |Financial | No budget.|
    |Schedule | The project must be launched by 07/07/2018 in order to meet the objectives in the business case.|
    |Facilities & Infrastructure | The project team will use existing office space and IT infrastructure such as computing equipment and networks.|

<h2>Functional Requirements:</h2>
    |Type | Requirement|
    |---|---|
    |Correlation | The system will automatically determine which employees are bound to which project.|

<h2>Non-functional Requirements:</h2>
    |Type | Non-Functional Requirement|
    |---|---|
    |Security | The system will protect user data against malicious attacks.|
    |Security | The system will allow only authenticated users to access authorized data.|
    |Information Technology | The system will be designed for enough availability as to be reliable on a academic simulation of the system.|
