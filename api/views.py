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

class EnrollCourse(generics.GenericAPIView):
# This API view is responsible for assigning new course to a student and returns all courses of a student
    def get(self, request, pk,  *args, **kwargs):
        # Returns courses which can be enrolled to a student
        # Logic = Non Compulsory Courses - Enrolled Courses
        try:
            student = models.Student.objects.get(id=pk)
        except Exception as e:
            # As there is no student with the given ID, so returning 400 Bad request
            return Response({"Error":"Student with such ID does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        print(student.standard)
        non_compulsory_courses = models.Course.objects.filter(standard=student.standard, isCompulsory=False)
        already_enrolled_courses = models.EnrolledCourse.objects.filter(student=student)
        non_compulsory_course_list =[]
        already_enrolled_course_list =[]
        # Coverting to list for removal operations
        for elem in non_compulsory_courses:
            non_compulsory_course_list.append(elem)
        for elem in already_enrolled_courses:
            already_enrolled_course_list.append(elem.course)
        for element in already_enrolled_course_list:
            non_compulsory_course_list.remove(element)

        serializer = serializers.CourseSerializer(instance=non_compulsory_course_list, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, pk, *args, **kwargs):
        try:
            student = models.Student.objects.get(pk=pk)
        except Exception as e:
            # As there is no student with the given ID, so returning 400 Bad request
            return Response({"Error":"Student with such ID does not exists"}, status=status.HTTP_400_BAD_REQUEST)

        data = self.request.data.dict()
        # Checking if the new course to be enrolled, is not enrolled and, is not a compulsory course
        already_enrolled_courses = models.EnrolledCourse.objects.filter(student=student)
        compulsory_courses = models.Course.objects.filter(standard=student.standard, isCompulsory=True)
        for course in already_enrolled_courses:
            if course.course.id == int(data['courseID']):
                # As the Course is already assigned, returning 400 response
                return Response({"Error":"Course Already Assigned"},status=status.HTTP_400_BAD_REQUEST)
        for course in compulsory_courses:
            if course.id == int(data['courseID']):
                # As the Course is compulsory, returning 400 response
                return Response({"Error":"Course is a Compulsory Course and is assigned by default"},status=status.HTTP_400_BAD_REQUEST)
        try:
            course = models.Course.objects.get(id=data['courseID'])
        except Exception as e:
            # As there is no Course with the given ID, so returning 400 Bad request
            return Response({"Error":"Course with such ID does not exists"},status=status.HTTP_400_BAD_REQUEST)
        enroll_course = models.EnrolledCourse(student=student, course=course)
        enroll_course.save()
        return Response(status=status.HTTP_201_CREATED)


class ListStudentCourses(generics.GenericAPIView):
# This API view returns (compulsory-according to standard, non-compulsory-assigned by admin) Courses
    def get(self, request, pk,  *args, **kwargs):
        # Returns courses which can be enrolled to a student
        # Logic = Non Compulsory Courses - Enrolled Courses
        try:
            student = models.Student.objects.get(id=pk)
        except Exception as e:
            # As there is no student with the given ID, so returning 400 Bad request
            return Response(status=status.HTTP_400_BAD_REQUEST)
        already_enrolled_courses_queryset = models.EnrolledCourse.objects.filter(student=student)
        compulsory_courses_queryset = models.Course.objects.filter(standard=student.standard, isCompulsory=True)
        data = []
        for elem in already_enrolled_courses_queryset:
            data.append(elem.course)
        for elem in compulsory_courses_queryset:
            data.append(elem)

        serializer = serializers.CourseSerializer(instance=data, many=True)
        
        return Response(data =serializer.data,status=status.HTTP_200_OK)
        