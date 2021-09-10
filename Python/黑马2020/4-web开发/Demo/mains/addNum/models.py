from django.db import models

# Create your models here.

# 建表
class cal(models.Model):
    valueA = models.CharField(max_length=10)
    valueB = models.FloatField(max_length=10)
    result = models.CharField(max_length=10)