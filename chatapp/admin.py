from django.contrib import admin
from .models import QuestionAnswer

@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('question',)  # Display question in list
    search_fields = ('question',)  # Enable search by question
