from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Department, Course, Student, Professor, Enrollment

# Create your views here.

@login_required
def dashboard(request):
    context = {
        'total_students': Student.objects.count(),
        'total_courses': Course.objects.count(),
        'total_professors': Professor.objects.count(),
        'total_departments': Department.objects.count(),
    }
    return render(request, 'core/dashboard.html', context)

@login_required
def student_list(request):
    students = Student.objects.select_related('user', 'department').all()
    return render(request, 'core/student_list.html', {'students': students})

@login_required
def course_list(request):
    courses = Course.objects.select_related('department').all()
    return render(request, 'core/course_list.html', {'courses': courses})

@login_required
def professor_list(request):
    professors = Professor.objects.select_related('user', 'department').all()
    return render(request, 'core/professor_list.html', {'professors': professors})

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'core/department_list.html', {'departments': departments})
