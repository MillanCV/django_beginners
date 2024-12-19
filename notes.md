# Source

Django for beginners

## Why Django

Django is a framework that allows to develop Web Server applications. It is very opinionated and uses a Model-View-Template
approach. Out-of-the-box it brings support for:

* User authentication
* Testing
* Database models, forms, URL routes, templates
* Admin interface
* Security and performance upgrades
* Support for multiple database backends

## Recommended formatter

Black on save (quick check: single quotes are substituted by double quotes)

## Donkey-guide

### Create project

1. python -m venv .venv 
2. source ./.venv/bin/activate    
    *  deactivate        
3. python -m pip install django~=4.2.0             
4. django-admin startproject django_project . 
5. python manage.py runserver 
   * python manage.py runserver 8080 
6. python -m pip install black  
7. git init
    * git config --global user.name "Your Name" 
    * git config --global user.email "yourname@email.com" 
    * git config --global init.defaultBranch main 
8. python manage.py startapp pages 
   * add app to INSTALLED_APPS
   * add app to INSTALLED_APPS
   * add view
   * add url
   * add templates
9. Apply migrations
   1.  python manage.py makemigrations
   2.  python manage.py migrate
10. Create Database Model
11. In case of defined static folder 'python manage.py collectstatic'
12. For tests: python manage.py test 

## Common general settings

 * INSTALLED_APPS += "pages.apps.PagesConfig"
 * "DIRS": [BASE_DIR / "templates"]
 * ALLOWED_HOSTS = ["*"] 
 * STATIC_URL = "static/"
 * STATIC_ROOT = BASE_DIR / "staticfiles", must be followed by 'python manage.py collectstatic"

## Views

### Types

* Function-based views
* Class-based views
* Generic class-based views
  * TemplateView: display a template
  * ListView: display a list

## Urls

### Common settings

* urlpatters: a list of paths
* django.urls.path
* django.urls.include
* Generic views are included using as_view() at the end of the view name

## Templates

### Tags

* url
* block - endblock
* extends
* for - endfor

## Testing

* Unittest: used by default by Django
    * TestCase instances
* Django specific extensions
  * Test client for dummy browser requests
  * Additional assertions
  * Test classes:
    * SimpleTestCase: when DB is not required
    * TestCase: when testing SB
    * TransactionTestCase: when testing DB transactions
    * LiveServerTestCase
  
### Database testing

* TestCase allows to tests with a test db
* Classmethod setUpTestData allows to initialize DB

## Hosting

### Fly.io

* It's a PaaS

#### Steps

1. python -m pip install gunicorn==20.1.0 
2. python -m pip freeze > requirements.txt 
3. add .dockerignore
   1. add venv, sqlite, git...
4. install fly cli
5. flyctl auth login
6. fly launch 
7. flyctl deploy
8. fly open 


## Django ORM

Translate automatically models to differents DB's

### ORM operations:

* Create record: Model.objects.create(fields)

## Database

* Sqlite3 is default DB in Django
  * Created when manage.py migrate or runserver are executed


## Models

* For each db model we want to create we subclass django.db.models.Model
* Once we have a model we run makemigrations and migrate.

### Add models to admin

* in app/admin.py
  ```python 
  from django.contrib import admin

  from .models import Post

  admin.site.register(Post)
  ``` 


## Static files

* Additional files commonly served: CSS, fonts, images, js
* In production, it is more efficient to combine all static files under a single location 