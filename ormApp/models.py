from django.db import models

class TestClass(models.Model):
    test_field = models.CharField(max_length=255)
