from django.db import models

# Create your models here.
class User(models.Model):
    nameStr = models.CharField(max_length=4)
    create_date = models.DateTimeField('date create')
    privilege = models.IntegerField(default=3)
