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
    def __str__(self):
        return self.first_name + " ID:" + str(self.id)

class Course(models.Model):
    course_name = models.CharField(unique=True, blank=False, null=False, max_length=200)
    standard = models.IntegerField(choices=StandartChoices.choices, default=StandartChoices.EIGHT)
    isCompulsory = models.BooleanField(default=False)
    def __str__(self):
        return self.course_name + " ID:" + str(self.id)

class EnrolledCourse(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.student.first_name + " ID:" + str(self.id) + self.course.course_name + " ID:" + str(self.course.id)
