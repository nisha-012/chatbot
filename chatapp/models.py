from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="questions")
    question_text = models.TextField()
    answer_text = models.TextField(blank=True, null=True)
    pdf_link = models.URLField(blank=True, null=True)  # Storing Google Drive PDF links
    show_in_faq = models.BooleanField(default=False)  # Checkbox to show in FAQ

    def __str__(self):
        return self.question_text

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class UserQuery(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField()
    question = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    response_sent = models.BooleanField(default=False)  # Track if email was sent

    def __str__(self):
        return f"{self.department.name} - {self.email}"

class Feedback(models.Model):
    email = models.EmailField()
    feedback_text = models.TextField()
    rating = models.IntegerField(default=0) #added rating field
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.email}"
