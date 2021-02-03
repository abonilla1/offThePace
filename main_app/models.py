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

RACE_GRADES = [
    ('G1', 'GRADE ONE'),
    ('G2', 'GRADE TWO'),
    ('G3', 'GRADE THREE'),
]


class Race(models.Model):
    name = models.CharField(max_length=200)
    host_track = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    field_size = models.IntegerField()
    grade = models.CharField(max_length=2, choices=RACE_GRADES)
    distance = models.CharField(max_length=200)
    race_date = models.DateField()
    entries = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'race_id' : self.id})


class Horse(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    starts = models.IntegerField()
    sire = models.CharField(max_length=150)
    dam = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    trainer = models.CharField(max_length=150)
    outcomes = models.CharField(max_length=1, choices=RACE_OUTCOMES)

    race = models.ForeignKey(Race, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'horse_id' : self.id})
    

  
   