from django.db import models

class QuestionAnswer(models.Model):
    question = models.CharField(max_length=255, unique=True)
    answer = models.TextField()
    important = models.BooleanField(default=False, help_text="Mark as important to display in FAQs")  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class UserQuery(models.Model):
    DEPARTMENT_CHOICES = [
        ("cs@cuh.ac.in", "Computer Science"),
        ("math@cuh.ac.in", "Mathematics"),
        ("phy@cuh.ac.in", "Physics"),
        ("chem@cuh.ac.in", "Chemistry"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    question = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Stores submission time

    def __str__(self):
        return f"{self.name} - {self.department} ({self.timestamp})"
