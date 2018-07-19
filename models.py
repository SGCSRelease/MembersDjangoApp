from django.db import models

# Create your models here.
class Penalty(models.Model):
    SEMESTER_CHOICES = (
        (1, 'Spring')
        (2, 'Fall')
    )
    title = models.CharField(max_length=50)
    date_Penalized = models.DateTimeField()
    semester = models.PositiveIntegerField(choices=SEMESTER_CHOICES)
    points = models.IntegerField(default=0)

class Introduction(models.Model):
    text = models.CharField(max_length=200)
    lang = models.CharField(max_length=20)
    date = models.DateTimeField('date joined')
    site = models.URLField(max_length=200)

