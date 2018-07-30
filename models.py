from django.db import models

# Create your models here.
class Penalty(models.Model):
    SEMESTER_CHOICES = (
        (1, 'Spring'),
        (2, 'Fall')
    )
    title = models.CharField(max_length=50)
    date_penalized = models.DateTimeField()
    semester = models.PositiveIntegerField(choices=SEMESTER_CHOICES)
    points = models.IntegerField(default=0)

    def penalized(self):
        self.date_penalized = timezone.now()
        self.save

    def __str__(self):
        return self.title


class Profile(models.Model):
    Intro = models.CharField(max_length=200)
    b_day = models.DateField()
    lang = models.CharField(max_length=20)
    date = models.DateField('date joined')
    github_link = models.URLField(max_length=200)

