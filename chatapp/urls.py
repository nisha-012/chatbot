from django.urls import path
from .views import HomeView, ChatView, AskQuestionView

urlpatterns = [
    path('', HomeView, name='home'),
    path("chatbot/", ChatView, name="chatbot"),  # Add this if 'chatbot' is required
    path("ask-query/", AskQuestionView, name="ask_query"),
]
