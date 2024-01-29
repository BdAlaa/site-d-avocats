from django.db import models

# Create your models here.
class evaluation(models.Model):
    rating = models.IntegerField()
    stars = models.IntegerField()
    
    
class comments(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField(null=False)
    time = models.DateField()
    
    