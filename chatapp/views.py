from django.shortcuts import render, redirect
from .models import Question, Feedback
from django.contrib import messages

def home(request):
    """Homepage with FAQ section."""
    faq_questions = Question.objects.filter(show_in_faq=True).order_by("topic", "question_text")
    return render(request, "chatapp/home.html", {"faq_questions": faq_questions})

def ask_query(request):
    """Renders the Ask Your Query page."""
    return render(request, "chatapp/ask_query.html")

def feedback(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback_text')
        rating = request.POST.get('rating')

        Feedback.objects.create(email=email, feedback_text=feedback_text, rating=rating)
        messages.success(request, 'Thank you for your feedback!')
        return redirect('feedback') # Redirect to the same page to clear form
    return render(request, 'chatapp/feedback.html')

def contact(request):
    """Renders the Contact page."""
    return render(request, "chatapp/contact.html")
