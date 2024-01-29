from django.db import models

# Create your models here.


class Rendezvous(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.DateField((""), auto_now=False, auto_now_add=False)
    statut = models.BooleanField()
    
