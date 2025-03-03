from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    credits = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    courses = models.ManyToManyField(Course, through='Enrollment')
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.student_id})"

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"Prof. {self.user.get_full_name()}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, blank=True, null=True)
    
    class Meta:
        unique_together = ['student', 'course']
    
    def __str__(self):
        return f"{self.student} - {self.course}"
