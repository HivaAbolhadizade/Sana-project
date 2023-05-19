from django.db import models
from django.contrib.auth.models import User





class Students(models.Model):
    name = models.CharField(max_length=100)
    score = models.FloatField(max_length=20)
    clas = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name