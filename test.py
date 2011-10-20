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
from sys import exit as sys_exit

PROJECT_FOLDER = 'test-project'
APP_FOLDER = 'test-app'

rmtree(PROJECT_FOLDER, ignore_errors=True)
management.execute_from_command_line(
    ['django-start.py', 'project', '--no-prompt', PROJECT_FOLDER])
system('virtualenv env')
system('source env/bin/activate')
chdir('project')
system('python manage.py require')
system('python manage.py sync')
system('python manage.py test ff0000')
management.execute_from_command_line(
    ['django-start.py', 'app', '--no-prompt', APP_FOLDER])

with open('urls.py', 'a') as f:
    f.write("\nurlpatterns.insert(0, url(r'^%s/', include('%s.urls')))\n" %
        (APP_FOLDER, APP_FOLDER))

with open('settings/__init__.py', 'a') as f:
    f.write("\nINSTALLED_APPS += ('%s',)\n" % APP_FOLDER)

system('python manage.py sync')
app_test_result = system('python manage.py test %s' % APP_FOLDER)

# NOTE! Just running 'test' fails for a bug in Django test DummyCache
# See: https://github.com/django/django/pull/5 

chdir('../../')
rmtree(PROJECT_FOLDER)
if app_test_result > 0: # error in the tests!
    sys_exit(1)
else:
    sys_exit(0)