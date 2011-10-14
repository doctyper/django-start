#!/usr/bin/env python
# NOTE: This file is a draft for a test suite that runs everything
# django-start is supposed to do, so whenever you change django-start
# you can run ./test.py and see if no errors are raised.
#
# TODO: Still needs a series of 'assert' to check that, apart from errors
# django-start does what it is supposed to do
#
from django_start import management
from shutil import rmtree
from os import chdir, system

PROJECT_FOLDER = 'test-project'

rmtree(PROJECT_FOLDER, ignore_errors=True)
management.execute_from_command_line(
    ['django-start.py', 'project', '--no-prompt', PROJECT_FOLDER])
chdir(PROJECT_FOLDER)
system('virtualenv env')
system('source env/bin/activate')
chdir('project')
system('python manage.py require')
system('python manage.py sync')
# NOTE! The next command fails because there is a bug in Django test DummyCache
# See: https://github.com/django/django/pull/5 
# system('python manage.py test') 

# TODO: Add the test to create an 'app' as well.

chdir('../../')
rmtree(PROJECT_FOLDER)
