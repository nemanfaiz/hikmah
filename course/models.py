from django.db import models
from hikmah.user.models import Teacher
from hikmah.user.models import Student
# 
# Create your models here.
class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    semester = models.CharField(max_length=200)
class StudentGrade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    