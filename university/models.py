from django.db import models


class Semester(models.Model):
    name = models.CharField(max_length=50)  # z. B. "Sommersemester 2025"

    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StudentCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="card")
    card_number = models.CharField(max_length=20)

    def __str__(self):
        return self.card_number


class Course(models.Model):
    title = models.CharField(max_length=200)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="courses")
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name="courses")
    students = models.ManyToManyField(Student, related_name="courses")

    def __str__(self):
        return self.title


class CourseDescription(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="description")
    text = models.TextField()

    def __str__(self):
        return f"Beschreibung: {self.course.title}"
