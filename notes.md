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
   1.  python manage.py migrate
   2.  python manage.py makemigrations
 

## Common general settings

 * INSTALLED_APPS += "pages.apps.PagesConfig"
 * "DIRS": [BASE_DIR / "templates"]
 * ALLOWED_HOSTS = ["*"] 


## Views

### Types

* Function-based views
* Class-based views
* Generic class-based views

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