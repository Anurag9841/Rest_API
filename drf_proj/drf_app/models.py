from django.db import models

class student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    description = models.TextField()
    def __str__(self) :
        return self.name

class drink(models.Model):
    name =models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name