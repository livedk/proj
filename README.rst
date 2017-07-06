Example Django project using Celery

Contents

proj/

This is the project iself, created using django-admin.py startproject proj, and then the settings module (proj/settings.py) was modified to add app1 to INSTALLED_APPS

proj/celery.py

This module contains the Celery application instance for this project, we take configuration from Django settings and use autodiscover_tasks to find task modules inside all packages listed in INSTALLED_APPS.

app1/

Example generic app. This is decoupled from the rest of the project by using the @shared_task decorator. This decorator returns a proxy that always points to the currently active Celery instance.

Starting the worker(if virtualenv change to special env)

$ celery -A proj worker -l info