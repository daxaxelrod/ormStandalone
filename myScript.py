# settings.py

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# need this to work in 1.9

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from ormApp import models

# similar to views.py
test_object, created = models.TestClass.objects.get_or_create(test_field="initial test field")

print(test_object.test_field)

def create_multiple_test_users(num_to_create):
    for i in num_to_create:
        models.TestClass.objects.create(test_field="dummy string")
        
