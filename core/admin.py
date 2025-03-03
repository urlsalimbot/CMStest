from django.contrib import admin
from .models import Department, Course, Student, Professor, Enrollment

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'credits', 'department')
    list_filter = ('department', 'credits')
    search_fields = ('name', 'code')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'get_full_name', 'department', 'date_of_birth')
    list_filter = ('department', 'date_of_birth')
    search_fields = ('student_id', 'user__first_name', 'user__last_name')
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Full Name'

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'get_full_name', 'department')
    list_filter = ('department',)
    search_fields = ('employee_id', 'user__first_name', 'user__last_name')
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Full Name'

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date_enrolled', 'grade')
    list_filter = ('course', 'date_enrolled', 'grade')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'course__name')
