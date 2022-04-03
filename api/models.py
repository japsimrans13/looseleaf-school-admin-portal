from stat import S_IXOTH
from django.db import models

# Standard Choices
class StandartChoices(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4
        FIFTH = 5
        SIXTH = 6
        SEVENTH = 7
        EIGHT = 8
        NINTH = 9
        TENTH = 10

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(blank=False, null=False, max_length=200)
    last_name = models.CharField(blank=False, null=False, max_length=200)
    standard = models.IntegerField(choices=StandartChoices.choices, blank=False, null=False)

class Course(models.Model):
    course_name = models.CharField(unique=True, blank=False, null=False, max_length=200)
    standard = models.IntegerField(choices=StandartChoices.choices, default=StandartChoices.EIGHT)
    isCompulsory = models.BooleanField(default=False)

