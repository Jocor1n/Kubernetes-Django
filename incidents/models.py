from django.db import models

# Create your models here.

class Incident(models.Model):
    titre = models.CharField(max_length=45)
    description = models.CharField(max_length=180)