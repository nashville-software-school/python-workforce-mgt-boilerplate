from django.db import models

class Department(models.Model):
    '''
    description: This class creates a department and its properties
    author: Joe Shep
    '''

    name = models.CharField(max_length=20)
    budget = models.IntegerField()
