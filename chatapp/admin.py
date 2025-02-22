from django.contrib import admin
from .models import QuestionAnswer, UserQuery

@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "important", "created_at", "updated_at")  # Show important status & timestamps
    search_fields = ("question",)  # Enable search by question
    list_filter = ("important", "created_at")  # Filter by importance & creation date
    list_editable = ("important",)  # Allow quick edits for important field
    readonly_fields = ("created_at", "updated_at")  # Prevent manual editing of timestamps
    fieldsets = (
        ("Question Details", {
            "fields": ("question", "answer", "important"),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),  # Collapsible section for cleaner UI
        }),
    )

@admin.register(UserQuery)
class UserQueryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "department", "timestamp")  # Show essential details
    search_fields = ("name", "email", "question")  # Enable search
    list_filter = ("department", "timestamp")  # Filter by department & time
    date_hierarchy = "timestamp"  # Adds a date-based navigation filter
    readonly_fields = ("timestamp",)  # Prevent manual timestamp edits
    fieldsets = (
        ("User Information", {
            "fields": ("name", "email", "department"),
        }),
        ("Query Details", {
            "fields": ("question",),
        }),
        ("Timestamp", {
            "fields": ("timestamp",),
            "classes": ("collapse",),  # Collapsible section for better UI
        }),
    )
