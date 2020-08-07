from django.db import models

# Create your models here.


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    webpage = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    name = models.CharField(max_length=264, unique=True)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class User(models.Model):
    first_name = models.CharField(max_length=264, unique=True)
    last_name = models.CharField(max_length=264, unique=True)
    username = models.CharField(max_length=264, unique=True)
    email = models.CharField(max_length=264, unique=True)
    password = models.CharField(max_length=264, unique=True)
    address = models.CharField(max_length=264, unique=True)
    phone = models.CharField(max_length=264, unique=True)
