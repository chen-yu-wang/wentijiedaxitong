from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Problem(models.Model):
    content = models.CharField(max_length=150)
    belong = models.ForeignKey("Student")
    zannum = models.IntegerField(default=0)
    cainum = models.IntegerField(default=0)

class Answer(models.Model):
    content = models.CharField(max_length=150)
    belong = models.ForeignKey("Problem")
    zannum = models.IntegerField(default=0)
    cainum = models.IntegerField(default=0)
    belongs =  models.ForeignKey("Student")
