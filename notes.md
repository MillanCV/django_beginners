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
13. For diferent db's in local/production
14. COnfigure CSRF_TRUSTED_ORIGINS to allow post request from trusted origins
15. python -m pip install whitenoise==6.4.0  to serve static files in production

## Common general settings

 * INSTALLED_APPS += "pages.apps.PagesConfig"
 * "DIRS": [BASE_DIR / "templates"]
 * ALLOWED_HOSTS = ["*"] 
 * STATIC_URL = "static/"
 * STATIC_ROOT = BASE_DIR / "staticfiles", must be followed by 'python manage.py collectstatic"
 * STATICFILES_DIRS = [BASE_DIR / "static"] 
 * Add environment variables
  ```
    from pathlib import Path
    from environs import Env  # new 
  
    env = Env()  # new 
    env.read_env()  # new 
  ```
  * Add database for develop and production:
  ```
  DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="sqlite:///db.sqlite3"),
  }
  ```
  * CSRF_TRUSTED_ORIGINS = ["https://*.fly.dev"]  
  * add white noise to Installed_apps, middleware and update STORAGES
  ```
  STORAGES = { 
    "default": { 
        "BACKEND": "django.core.files.storage.FileSystemStorage", 
    }, 
    "staticfiles": { 
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage", 
    # new 
      }, 
  } 
  ```

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
* static
* 
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
  
### What to test?

* URL exists
* URL returns 200
* URL available by name
* Correct template is used
* Page content matched DB
  
### Database testing

* TestCase allows to tests with a test db
* Classmethod setUpTestData allows to initialize DB

## Hosting and deployment

### Fly.io

* It's a PaaS

#### Steps

1. python -m pip install gunicorn==20.1.0 
   1. gunicor is a production replacement for Django local WSGI server
2. python -m pip freeze > requirements.txt 
3. set ALLOWED_HOSTS
4. add .dockerignore
   1. add venv, sqlite, git...
5. install fly cli
6. flyctl auth login
7. fly launch 
8. flyctl deploy
9. fly open 
10.  fly ssh console --pty -C "python /code/manage.py createsuperuser" 

### Environment variables

* Are variables whose value are set outside the current program an can be loaded in at runtime.
* They can be stored in a secure location:
  * To keep information secure, such as passwords, api keys...
  * Allow to rely on a single settings.py file to load local or production environment variables.



## Database

* Sqlite3 is default DB in Django
  * Created when manage.py migrate or runserver are executed
* Postgresql requires psycopg:
  * python -m pip install "psycopg[binary]"
* Relational database:
  * A place to store and access different types of data, in tables, with columns and rows
    * Columns define what information can be stored
    * Rows contains actual data
    * Frequently data in separate tables have some relation
  * SQL is used to interact with relational databases to perform CRUD operations and define the type of relationships
  * Recommended when data is consisten, structured and relationships are essential.
* Non-relational database:
  * Don't uses the previous structure
  * Types: document-oriented, key-value, graph, wide-column...
    * Recommended when data is not structured, needs to be flexible in size or shape or open to change.

### Django ORM

* Translate automatically models to differents relational DB's
* Allows to define database models whitout writing SQL
* Django automati

#### ORM operations:

* Create record: Model.objects.create(fields)

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
  * We need WhiteNoise package, python -m pip install whitenoise==6.4.0 