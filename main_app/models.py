from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

RACE_OUTCOMES = [
    ("W", "Win"),
    ("P", "Place"),
    ("S", "Show"),
]

RACE_GRADES = [
    ("G1", "GRADE ONE"),
    ("G2", "GRADE TWO"),
    ("G3", "GRADE THREE"),
]


# class Race(models.Model):
#     name = models.CharField(max_length=200)
#     host_track = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)
#     field_size = models.IntegerField()
#     grade = models.CharField(max_length=2, choices=RACE_GRADES)
#     distance = models.CharField(max_length=200)
#     race_date = models.DateField()
#     entries = models.TextField(max_length=500)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('detail', kwargs={'race_id' : self.id})


class Horse(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    starts = models.IntegerField()
    sire = models.CharField(max_length=150)
    dam = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    trainer = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"horse_id": self.id})

    def most_recent_run(self):
        return self.outcome_set.filter(date=date.today()).count() >= len(RACE_OUTCOMES)


class Jockey(models.Model):
    name = models.CharField(max_length=150)
    starts = models.IntegerField()
    age = models.IntegerField()
    bio = models.TextField(max_length=500, default="")
    horses = models.ManyToManyField(Horse)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("jockeys_detail", kwargs={"pk": self.id})

    def most_recent_run(self):
        return self.outcome_set.filter(date=date.today()).count() >= len(RACE_OUTCOMES)


class Outcome(models.Model):
    date = models.DateField("Most Recent Race")
    outcome = models.CharField(
        max_length=1,
        choices=RACE_OUTCOMES,
        default=RACE_OUTCOMES[0][0],
    )

    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_outcome_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ["-date"]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="", blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
