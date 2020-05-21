from django.db import models
from django.contrib.auth.models import User

class person(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  bio=models.TextField()
  dp=models.ImageField()
  