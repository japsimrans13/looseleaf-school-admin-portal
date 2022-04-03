from django.contrib import admin
from django.urls import path

from . import views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student', views.ListCreateStudent.as_view()),
    path('student/update/<int:pk>', views.UpdateStudent.as_view()),
    path('student/delete/<int:pk>', views.DeleteStudent.as_view()),
]
