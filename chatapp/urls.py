from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Homepage with FAQ section
    path("ask-query/", views.ask_query, name="ask_query"),  # Ask Your Query Form
    path("feedback/", views.feedback, name="feedback"),  # Feedback Form
    path("contact/", views.contact, name="contact"),  # Contact Page
]
