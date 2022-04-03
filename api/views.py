from rest_framework.response import Response
from rest_framework import status, generics

from . import models
from . import serializers

# Create your views here.

class ListCreateStudent(generics.ListCreateAPIView):
    # This API view will create a new Student om HTTP 'Post' request and return all the students registed on HTTP 'Get' request.
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request)
    def post(self, request, *args, **kwargs):
        return self.create(request)

    

