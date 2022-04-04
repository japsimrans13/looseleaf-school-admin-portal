from django.contrib import admin
from django.urls import path

from . import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Student URLS
    path('student', views.ListCreateStudent.as_view()),
    path('student/update/<int:pk>', views.UpdateStudent.as_view()),
    path('student/delete/<int:pk>', views.DeleteStudent.as_view()),
    path('student/view/<int:pk>', views.ListStudentCourses.as_view()),
    # Course URLS
    path('course', views.ListCreateCourse.as_view()),
    path('course/update/<int:pk>', views.UpdateCourse.as_view()),
    path('course/delete/<int:pk>', views.DeleteCourse.as_view()),
    path('course/enroll/<int:pk>',views.EnrollCourse.as_view()),
]
