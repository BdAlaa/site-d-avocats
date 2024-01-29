from django.db import models

# Create your models here.
class Lawyer(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    practice_area = models.CharField(max_length=50, null=False)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50, null=False)
    website = models.CharField(max_length=50, blank=True, null=True)
    langue = models.CharField(max_length=10 , null=False, default='arab')
    experiance = models.TextField(blank=True)
    password = models.CharField(max_length=128)
   