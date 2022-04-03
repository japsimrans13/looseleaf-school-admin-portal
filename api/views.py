from rest_framework.response import Response
from rest_framework import status, generics

from . import models
from . import serializers

# Create your views here.

# Student API views (List, Create), (Update), (Delete)
class ListCreateStudent(generics.ListCreateAPIView):
# This API view will create a new Student om HTTP 'Post' request and return all the students registed on HTTP 'Get' request.
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request)
    def post(self, request, *args, **kwargs):
        return self.create(request)

    
class UpdateStudent(generics.UpdateAPIView):
# This API view is responsible for updating existing Student instance.
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()
    lookup_field = 'pk'

    def put(self, request,*args, **kwargs):
        return self.update(request, *args, **kwargs)

class DeleteStudent(generics.DestroyAPIView):
# This API view is responsible for deleting existing Student instance.
    serializer_class = serializers.StudentSerializer
    queryset = models.Student.objects.all()
    lookup_field = 'pk'

    def delete(self, request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Course API Views (List, Create), (Update), (Delete)

class ListCreateCourse(generics.ListCreateAPIView):
# This API view will create a new Student om HTTP 'Post' request and return all the students registed on HTTP 'Get' request.
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request)
    def post(self, request, *args, **kwargs):
        return self.create(request)

    
class UpdateCourse(generics.UpdateAPIView):
# This API view is responsible for updating existing Student instance.
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()
    lookup_field = 'pk'

    def put(self, request,*args, **kwargs):
        return self.update(request, *args, **kwargs)

class DeleteCourse(generics.DestroyAPIView):
# This API view is responsible for deleting existing Student instance.
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()
    lookup_field = 'pk'

    def delete(self, request,*args, **kwargs):
        return self.destroy(request, *args, **kwargs)