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
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Signup model
class Signup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

