from django.db import models

# Create your models here.

class JGdates(models.Model):
    year = models.IntegerField(unique=True) # 년도
    date1 = models.CharField(max_length=5) #1학기 개강  MM/DD 형식
    date2 = models.CharField(max_length=5) #1학기 종강  MM/DD 형식
    date3 = models.CharField(max_length=5) #2학기 개강  MM/DD 형식
    date4 = models.CharField(max_length=5) #2학기 종강  MM/DD 형식
