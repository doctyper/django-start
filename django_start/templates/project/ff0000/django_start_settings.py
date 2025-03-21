# This file will contain
# - a description of this project template
# - the list of variables to be substituted
# - the commands to be launched after copying the template files (e.g. git pull)

# Also, this file will NOT be copied
import os
from random import choice
from string import ascii_lowercase, digits

def after_copy(no_prompt=False):
    """Steps to run after the templates has been copied in place."""
    # 1. Import red-boilerplate in place using git
    os.system("find . -name '*.pyc' -exec rm -rf {} \;")
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m'Django project created with django-start'")

    # cURL from GitHub
    os.system("curl -L https://github.com/ff0000/red-boilerplate/zipball/master -o tmp.zip")
    os.system("unzip tmp.zip")
    os.system("mv $(find . -depth 1 -type d -name 'ff0000-red-boilerplate-*')/{*,.*} .")

    # Cleanup
    os.system("find . -depth 1 -type d -name 'ff0000-red-boilerplate-*' -delete")
    os.system("find . -depth 1 -type f -name 'tmp.zip' -delete")

    # Commit
    os.system("git commit -am 'Importing the RED Boilerplate http://github.com/ff0000/red-boilerplate'")

    os.system("git rm --ignore-unmatch README.md")
    os.system("git rm --ignore-unmatch LICENSE.txt")
    os.system("git mv INSTRUCTIONS.md README.md")
    os.system("git commit -m'Restored django-start README.md'")

    # 2. Replace boilerplate variables with prompt values or defaults
    placemarks = [
      ['PROJECT_NAME', 'Project Name', 'Django Project'],
      ['ADMIN_EMAIL',  'Administrator email', 'geeks@ff0000.com'],
    ]
    replace = {}
    for var, help, default in placemarks:
        placemark = '__%s__' % var
        replace[placemark] = None
        while not replace[placemark]:
            if no_prompt:
                replace[placemark] = default
            else:
                prompt = '%s [%s]: ' % (help, default)
                replace[placemark] = raw_input(prompt) or default
    key_seed = ''.join([choice(ascii_lowercase + digits) for x in range(50)])
    replace['__SECRET_KEY_SEED__'] = key_seed

    # FIXME: This resets permissions!! Change with shutil
    # TODO: Also replace variables in file names
    for root, dirs, files in os.walk('.'):
        DONT_REPLACE_IN = ['.svn', '.git',]
        for folder in DONT_REPLACE_IN:
            if folder in dirs:
                dirs.remove(folder)
        for name in files:
            filepath = os.path.join(root, name)
            with open(filepath, 'r') as f:
                data = f.read()
            for old_val, new_val in replace.items():
                data = data.replace(old_val, new_val)
            with open(filepath, 'w') as f:
                f.write(data)

    os.system("git commit -a -m'Replaced boilerplate variables'")
