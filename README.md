# SFIA-2
DEVOPS

# HZ Random Party Themes Generator
1. [Brief](#brief)
  + [My Solution](#solution)
2. [Trello Board](#trello)
  + [User Stories](#userstories)
  + [Initial Trello](#initialtrello)
  + [Progress Trello](#progresstrello)
  + [Final Trello](#finaltrello)
3. [Risk Assessment](#riskassessment)

4. [Architecture](#architecture)
  + [Application Flowchart](#appflow)
  + [Initial Database](#initialdatabase)
  + [Final Database](#finaldatabase)
  + [Wesbite Sitemap](#sitemap)
  + [Website Wireframe](#wireframe)
  
5. [Implementation/ Visual Representation of App](#implementation)
  
6. [Testingn App](#testing)
  + [Unit Testing](#unittesting)
  + [Coverage Testing](#coveragetesting)
  
7. [Deployment](#deployment)

8. [Retrospect](#retrospect)

9. [Authors](#authors)

10. [Acknowledgements](#acknowledgements) 


<a name ="brief"></a>
## 1. The Product Brief
To create:
  1. An application that generates “Objects” upon a set of predefined rules
  2. A micro-service orientated architecture for the application
  3. Utilisation of Flask,Jinja2 for front-end website and integrated API's while Python and MySQL for back-end
  4. Generating Random Objects
  5. Utilising Feature-Branch Model and creating an Ansible Playbook

<a name ="solution"></a>
## My Solution
My application is created using Boostrap, Jinja2 and Flask for the Front-End and Python and MySQL for the Back-End Development.It is a website where user's can organise a party and each time, random party theme, outfit colour, location and ticket price would be generated. Lucky winner can also have free entry ticket to the party. User's input is also taken into consideration as if a user is a child, the theme of the party generated would be suitable for children for example "Princess Party" where as for adults it would display different results for example "Halloween Parrty". The website is user-friendly and responsive for better user experience.  

<a name ="trello"></a>
## 2. Trello Board
Trello Board was used to plan, organize and prioritize my project so that not only all user requirements are fully met but to also meet project deadline. 


<a name ="userstories"></a>
### User Stories

[userstories]: https://i.imgur.com/B7WRuif.png

![userstories][userstories]

<a name ="initialtrello"></a>
### Inital Trello Board
Initial Trello board has all the product backlog, sprint backlog which is then broken down into small and manageable tasks. Once each task is completed, it is then moved to Done and during that process if any errors were encountered, those were listed in bugs.

[initialtrello]: https://i.imgur.com/SZcPjPZ.png

![initialtrello][initialtrello]

<a name ="progresstrello"></a>
## Progress Trello Board

[progresstrello]: https://i.imgur.com/SV1Qasy.png

![progresstrello][progresstrello]


<a name ="finaltrello"></a>
## Final Trello Board

[finaltrello]: 

![finaltrello][finaltrello]


<a name ="riskassessment"></a>
## 3. Risk Assessment
Risk Assessment was carried out to consider what could go wrong during the project and deciding on which control measures are to be taken in such situations. As a result, these control measures would help eliminate and reduce any risk involved during the project.

Below is the Initial Risk Assessment displayed in the Table:

[riskassessmentmatrix]: https://i.imgur.com/u2w7SrF.png

![riskassessmentmatrix][riskassessmentmatrix]


[riskassessment]: https://i.imgur.com/CmbI4ip.png

![riskassessment][riskassessment]


Below is the Final Risk Assessment displayed in the Table:

[finalriskassessment]:https://i.imgur.com/euUrgjE.png

![finalriskassessment][finalriskassessment]



<a name ="architecture"></a>
## 4. Architecture
Before bulding the application, design stage was considered, which involved series of steps to help me define and plan my application. 


<a name ="appflow"></a>
## Application flowchart
Application flowchart showing the design process of the application

[appflow]: https://i.imgur.com/2ybSWtt.jpg

![appflow][appflow]


Micro-service orientated architecture for the application

[mic]: https://i.imgur.com/iWms8EJ.png

![mic][mic]

<a name ="initialdatabase"></a>
## Initial Database
Below is the initial Database for my project where I had minimum of one table that stores the randomly generated objects/sentence that appears on the front-end. 

[initialdatabase]: https://i.imgur.com/gZMfgTu.png

![initialdatabase][initialdatabase]



<a name ="finaldatabase"></a>
## Final Database

This is my final Database where I also added users table, so that user's can also submit theme/message in case they couldn't find a fun theme for the party.As it is important to get feedback from the users to support their needs and demands.


[finaldatabase]: https://i.imgur.com/CZEOumu.png

![finaldatabase][finaldatabase]


<a name ="sitemap"></a>
## Website Sitemap
Sitemap was created which is a blueprint to show the structure of the website and how the pages are linked. 

[sitemap]: https://i.imgur.com/UaMzCeN.png

![sitemap][sitemap]

<a name ="wireframe"></a>
## Website Wireframe
Wireframe was created to help arrange the elements on the website and to achieve the optimum outcome. The wireframe was created considering the project brief of creating random objects while using micro-service architecture.

Below shows the initial wireframe of the home page.

[initialwireframe]: https://i.imgur.com/0YzOmpH.png

![initialwireframe][initialwireframe]


Below shows the final wireframe of the home page.

[finalwireframe]: https://i.imgur.com/5P1tCh2.png

![finalwireframe][finalwireframe]


<a name ="implementation"></a>
## 5. Visual Representation of App 

### Link to The Party Themes Generator :
### Manager Node
http://35.197.228.70/
### Worker Node
http://35.246.125.202/

## Home Page

[home]: https://i.imgur.com/u8pKOVK.png

![home][home]


## Submit Theme Page

[submittheme]: https://i.imgur.com/SOfLJam.png

![submittheme][submittheme]


## About Us Page

[about]: https://i.imgur.com/poLPNex.png

![about][about]

<a name ="testing"></a>
## 6. Testing
Testing the application to ensure it runs successfully. 
Two types of tests were carried out including unit testing and coverage testing.

<a name ="unittesting"></a>
## Unit Testing
+ Testing URL to check whether the app has been deployed successfully and each web page is up and running. 
+ Testing Database to ensure data gets inserted and deleted successfully via the web application to ensure there are no errors runnung the Dynamic Web Application and to validate each unit of the software performs as it is designed to do so.

### Unit Testing URLs:
All the web pages were tested and even pages that don't exist were tested too to ensure that the user can access what is accessible to them and can't access what is not accessible to them.

Below shows the result of the URL Testing carried out:

[urltest]: https://i.imgur.com/4VaNPx5.png

![urltest][urltest]

### Unit Testing Database:
Database tested to allow user to input as desinged to while submitting theme, storing the random theme generated into the database to ensure the database is fully functional.

Below shows all the testing/ queries carried out for Database:

[dbtest]: https://i.imgur.com/t41D9TX.png

![dbtest][dbtest]

### Combining both URL and Database Testing:

[bothtest]: https://i.imgur.com/zUUj4iz.png

![bothtest][bothtest]


<a name ="coveragetesting"></a>
## Coverage Testing
Coverage Testing carried out to generate metric that will show how much of the source is tested to assess the test suite quality.

### URL Coverage Testing:
 
 [urlcoverage]:  https://i.imgur.com/e1vUekQ.png

![urlcoverage][urlcoverage]

### Database Coverage Testing:
 
  [dbcoverage]: https://i.imgur.com/9n7xJWp.png

![dbcoverage][dbcoverage]


### Combining both URL and Database Coverage Testing:
 The coverage metrics went down when both URL and Database were tested together due to the complexity of the application and by importing more libraries.
 
  [bothcoverage]: https://i.imgur.com/gWuL9Ac.png

![bothcoverage][bothcoverage]

<a name ="deployment"></a>
## 7. Deployment
The App was deployed using Jenkinns,Github and Docker hub. Github webhooks was also integrated to trigger the build whenever the developer commits any change to the branch where docker hub is connected to github so all the build process of images and pushing them onto the docker hub is done automatically.

 As Jenkins is connected to Github, this way when webhook was added to the job, it ensured that the build was triggered automatically everytime the code is commited to the Github.Therefore, Jenkins triggers the build automatically and then deploys ansible playbook which installs Docker on Manager and worker node and automates docker swarm. 

This prevents human error as ansible is a configuration management tool therefore, it deploys the same software to as many worker nodes automatically without installing them manually which not only saves time but also prevents human error.

Below is the diagram demonstrating the Technology Overview:

[deployment]:  https://i.imgur.com/mpcDAR1.png

![deployment][deployment]


## How the process works:

1. Jenkins waiting to trigger the build once change was fully committed:

[build]: https://i.imgur.com/IakNROG.png

![build][build]

2. Jenkins Build triggered automatically once change was committed:

[build2]: https://i.imgur.com/sZwSVBP.png

![build2][build2]

3. App Deployed successfully using Jenkins while automatically triggering build when code is committed to GitHub. Build process deploys the App onto the Development Environment:

[build3]: https://i.imgur.com/NNTYw8N.png

![build3][build3]


[build4]: https://i.imgur.com/gF56IrY.png

![build4][build4]

4. Deploying Ansible File to Install Docker on manager and worker node and automate docker swarm

[build5]: https://i.imgur.com/9wktd6W.png

![build5][build5]

5. Automatically deploying the stack 

[build6]: https://i.imgur.com/KeyBBbt.png

![build6][build6]

### 6. Tests the App using Pytest

[build7]: https://i.imgur.com/J2tbgwh.png

![build7][build7]