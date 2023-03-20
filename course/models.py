from django.db import models
from hikmah.user.models import Teacher
from hikmah.user.models import Student


# testing 1234
#
# Create your models here.
class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    semester = models.CharField(max_length=200)


class StudentGrade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=200)


class StudentCourse(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    gradeID = models.ForeignKey(StudentGrade, on_delete=models.CASCADE)


class Assignment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)


class StudentAssignment(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField()
