from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Home model
class Home(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Signin model
class Signin(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.id, self.password


# Signup model
class Signup(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.id, self.password, self.username
