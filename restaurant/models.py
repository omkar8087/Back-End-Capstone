from django.db import models

class menu(models.Model):
    item = models.CharField(max_length=100)
    price = models.IntegerField()

class booking(models.Model):
    tableno = models.IntegerField()
    persons = models.IntegerFiled()
