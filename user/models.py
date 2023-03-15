from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=200)
    gpa = models.FloatField()
    class_year = models.IntegerField()

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    title = models.CharField(max_length=200, default="Teacher")

class Administrator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
