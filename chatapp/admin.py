from django.contrib import admin
from .models import Topic, Question, UserQuery, Feedback

# Inline for managing questions within the Topic page
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Allows adding questions directly in the Topic page

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Show topic name in list view
    search_fields = ("name",)  # Allow searching topics
    inlines = [QuestionInline]  # Show related questions inline

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "topic", "show_in_faq", "pdf_link")  # Show FAQ status
    list_filter = ("topic", "show_in_faq")  # Filter by topic & FAQ inclusion
    search_fields = ("question_text", "answer_text")  # Search by question & answer
    ordering = ("topic", "question_text")  # Sort by topic & question text
    list_editable = ("show_in_faq",)  # Enable quick editing of FAQ status
    readonly_fields = ("pdf_link",)  # Prevent accidental changes to PDF link

    fieldsets = (
        ("Question Details", {"fields": ("topic", "question_text", "answer_text")}),
        ("Additional Info", {"fields": ("show_in_faq", "pdf_link")}),
    )

@admin.register(UserQuery)
class UserQueryAdmin(admin.ModelAdmin):
    list_display = ("email", "submitted_at", "response_sent")  # Key details
    list_filter = ("response_sent",)  # Filter by department & status
    search_fields = ("email", "question")  # Allow search by email or question
    ordering = ("-submitted_at",)  # Show latest queries first
    readonly_fields = ("submitted_at",)  # Prevent manual editing of timestamp
    
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("email", "submitted_at", "rating", "truncated_feedback")  # Added rating and truncated feedback
    search_fields = ("email", "feedback_text")
    ordering = ("-submitted_at",)
    readonly_fields = ("submitted_at", "rating") #Added rating to readonly field.
    list_filter = ("submitted_at", "rating") #Added rating filter.

    def truncated_feedback(self, obj):
        """Show a shortened version of the feedback in the list view."""
        return obj.feedback_text[:50] + "..." if len(obj.feedback_text) > 50 else obj.feedback_text

    truncated_feedback.short_description = "Feedback Preview"
