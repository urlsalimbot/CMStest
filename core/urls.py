from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='course_list'),
    path('professors/', views.professor_list, name='professor_list'),
    path('departments/', views.department_list, name='department_list'),
]
