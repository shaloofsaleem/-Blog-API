
<!-- PROJECT LOGO -->



## About The Project

# -Blog-API-

<br>
<p align='center'>
 <img src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*go4vEjAqgznYnJoksYJ_0A.png" width='70%' > 
</p>
<br>

A blog API in Django is an API that allows developers to interact with a blog's data, such as posts, comments, and categories, using Django as the backend. To create a blog API in Django, you can use the Django Rest Framework, which is a powerful tool for building APIs in Django. This framework allows you to create views, serializers, and routers that handle the data and interactions with the API. The views handle the logic of the API and how it responds to requests, the serializers handle the data and how it is formatted when sent and received, and the routers handle the URL patterns and routing for the API. Once the API is developed, it can be integrated into a web or mobile application to allow users to interact with the blog data

- Install DRF by adding it to your project's requirements.txt file or by running pip install djangorestframework..
- To add JSON Web Token (JWT) authentication to a Django REST Framework (DRF) API, you can use the djangorestframework_simplejwt package. Here is a    general guide to adding JWT authentication to your API:
-Install the djangorestframework_simplejwt package by adding it to your project's requirements.txt file or by running pip install            djangorestframework_simplejwt.
-  Add 'rest_framework_simplejwt' to your INSTALLED_APPS in your settings.py file.

## Main Topics
- Creating serializers
-  Setting URLs
-  Setting up JWt authentication in Django rest framework
-  Creating models for the Blog app
-  Serializer for a Blog application
-  Post method  for a Blog application
-  Get method for Blog Application
-  Patch method for a blog application
-  Delete method for Blog Application
-  Adding pagination to Blogs


<br>

### Built With

![Python](https://img.shields.io/badge/Python%20-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)


![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Github Pages](https://img.shields.io/badge/GitHub%20Pages-%23327FC7.svg?style=for-the-badge&logo=github&logoColor=white)

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

<br>

## Running this project

This is a sample for Django Project.
To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv venv
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source venv/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```
## Create a Project
```
python manage.py startproject blog
```

### Create apps
```
python manage.py startapp account
python manage.py startapp home
```
 ### Create Folder
- API (Create url.py) -> easy acess url

### Create apps
```
python manage.py startapp account
python manage.py startapp home
```

###  Create file serializer.py 
- In Create apps
```
from rest_framework import serializers
```
 ### account  app create
 - Register
 - Login
###  Create JWT  
- Documtation Link
```
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
```
Apply migrations and create your database
```
python manage.py migrate
```
Create a user with manage.py
```
python manage.py createsuperuser
```

Now you can run the project with this command

```
python manage.py runserver
```

<br>


Django rest framework is one of the most popular web framework for building rest APIs in Django.
We will be seeing how we can create CRUD APIs in the Django rest framework. Also, we will be seeing how we can implement JWT authentication, pagination and search functionality in this application. You will be learning some of the core concepts of the Django rest framework like serializer, APIView, response, and status code in the Django rest framework.

