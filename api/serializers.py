from rest_framework import serializers
from . import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'