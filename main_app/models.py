from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

RACE_OUTCOMES = [
    ('W', 'Win'),
    ('P', 'Place'),
    ('S', 'Show'),
]

class Horse(models.Model):
    
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    starts = models.IntegerField()
    sire = models.CharField(max_length=150)
    dam = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    trainer = models.CharField(max_length=150)
    outcomes = models.CharField(max_length=1, choices=RACE_OUTCOMES)