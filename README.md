Django-start installs a script which allows the easy creation of Django 
projects and applications based the layout used at RED Interactive Agency.

How to use
==========

An in-depth tutorial is available at: http://ff0000.github.com/2011/10/django-hands-on-tutorial/

Creating a project
------------------
  
    pip install django-start
    django-start.py project example
    
This will use the default project template, which includes 
[red-boilerplate](https://github.com/ff0000/red-boilerplate).

Running a project
-----------------

    cd example
    virtualenv env
    source env/bin/activate
    cd project
    python manage.py require
    python manage.py sync
    python manage.py server


How to contribute
=================

Fork the project, make your changes, then run

    python test.py
    
This command will:

* create a test project using the `ff0000` template
* create a test app inside that project using the `blog` template
* run the test suite for the app

If everything runs correctly, then submit a pull request via Github.

You can have the tests run automatically before any commit by adding an executable file `.git/hooks/pre-commit` with this code:

    #!/bin/sh
    python test.py || exit 1


How does it work
================

Creating a project from a template
----------------------------------

Running `django-start.py project <folder_name>` executes the code included in [management/commands/project.py](https://github.com/ff0000/django-start/blob/master/django_start/management/commands/project.py), which does three simple things:
  
1. Creates a new folder called `<folder_name>`.
2. Copies in that folder all the files included in the project template folder. This can be specified with the `--template-dir` option; the default is `templates/project/ff0000`.
3. If a file called `django_start_settings.py` is present in that folder, and if it contains a function called `after_copy`, then that file is loaded and that function executed. 

As an example, in the case of the ff0000 project template, the [after_copy function](https://github.com/ff0000/django-start/blob/master/django_start/templates/project/ff0000/django_start_settings.py) downloads an HTML5 boilerplate from GitHub, prompts the user for some variables and substitutes them in the template. This is just an example, other project templates can perform any other operation.

Creating an app from a template
-------------------------------

Running `django-start.py app <folder_name>` executes the code included in [management/commands/app.py](https://github.com/ff0000/django-start/blob/master/django_start/management/commands/app.py), which does three simple things:

1. Look in the current directory for a folder called `apps` and creates a new subfolder called `<folder_name>`.
2. Copies in that folder all the files included in the `apps` folder of the app template. This can be specified with the `--template-dir` option; the default is `templates/app/blog`.
3. Look in the current directory for a folder called `templates` and creates a new subfolder called `<folder_name>`.
4. Copies in that folder all the files included in the `templates` folder of the app template. This can be specified with the `--template-dir` option; the default is `templates/app/blog`.
5. If a file called `django_start_settings.py` is present in the app template, and if it contains a function called `after_copy`, then that file is loaded and that function executed. 

The logics of `django-start.py app` is very similar to `django-start.py project`. The main difference is that a Django application typically contains both Django logics and HTML templates, and they are stored separately (the former in a folder called `apps`, the latter in `templates`). Typically you would run `django-start.py app` inside the `project` folder of a Django project created with `django-start.py project`.

As an example, in the case of the blgo app template, the [after_copy function](https://github.com/ff0000/django-start/blob/master/django_start/templates/app/blog/django_start_settings.py) prompts the user for some variables and substitutes them in the template. This is just an example, other app templates can perform any other operation.

Creating a new project/app template
-----------------------------------

To add a new app or project template to django-start, simply add it in the `templates` folder, under `app` or `project` respectively. If you need to perform extra actions after the files have been copied, add a file called `django_start_settings.py` with an `after_copy` function (take a look at existing templates).

Finally, to use the newly created template, just indicate its path as the `--template-dir` option, for instance:

    django-start.py --template-dir=/your/custom/template project new_example
