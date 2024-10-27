from django.db import models

# Create your models here.
class LoggedIn(models.Model):
    name = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    extra1 = models.CharField(max_length=122)


class Questions(models.Model):
    questn = models.CharField(max_length=122)
    questnId = models.CharField(max_length=122)
    qname = models.CharField(max_length=122)
    extra2 = models.CharField(max_length=122)

class Templeate(models.Model): #used in getting the branch and year
    year = models.CharField(max_length=122)
    branch = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    extra3 = models.CharField(max_length=122)

class Answer(models.Model):
    qustn = models.CharField(max_length=122)
    qustnId = models.CharField(max_length=122)
    extra4 = models.CharField(max_length=122)




