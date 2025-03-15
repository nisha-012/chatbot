from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Topic, Question, Feedback, UserQuery
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def create_admin_user(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin123")
        return HttpResponse("Superuser created! Username: admin, Password: admin123")
    else:
        return HttpResponse("Superuser already exists.")

def home(request):
    """Homepage with FAQ section."""
    faq_questions = Question.objects.filter(show_in_faq=True).order_by("topic", "question_text")
    return render(request, "chatapp/home.html", {"faq_questions": faq_questions})

def chat_with_us(request):
    topics = Topic.objects.all()
    return render(request, 'chatapp/chat_with_us.html', {'topics': topics})

def get_questions(request, topic_id):
    """Fetch all questions for a selected topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    questions = Question.objects.filter(topic=topic).values("id", "question_text", "answer_text", "pdf_link")

    return JsonResponse({"questions": list(questions)})


def ask_query(request):
    """Renders the Ask Your Query page and handles form submission."""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        question = request.POST.get("question")

        # Validation
        if not name:
            messages.error(request, "Name is required.")
            return render(request, "chatapp/ask_query.html", {"name": name, "email": email, "question": question})

        if not email:
            messages.error(request, "Email is required.")
            return render(request, "chatapp/ask_query.html", {"name": name, "email": email, "question": question})

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address.")
            return render(request, "chatapp/ask_query.html", {"name": name, "email": email, "question": question})

        if not question:
            messages.error(request, "Question is required.")
            return render(request, "chatapp/ask_query.html", {"name": name, "email": email, "question": question})

        # Store data in the database
        try:
            UserQuery.objects.create(email=email, question=question)
            messages.success(request, "Your query has been submitted successfully!")
            return redirect("ask_query")  # Redirect to clear the form
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return render(request, "chatapp/ask_query.html", {"name": name, "email": email, "question": question})

    return render(request, "chatapp/ask_query.html")

def feedback(request):
    """Handles feedback form submission and validation."""
    if request.method == 'POST':
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback_text')
        rating = request.POST.get('rating')

        # Validation
        if not email:
            messages.error(request, "Email is required.")
        else:
            try:
                validate_email(email)
            except ValidationError:
                messages.error(request, "Invalid email address.")

        if not feedback_text:
            messages.error(request, "Feedback text is required.")

        if not rating or rating not in ["1", "2", "3", "4", "5"]:  # Ensure rating is valid
            messages.error(request, "Please select a valid rating (1-5).")

        # If there are errors, re-render the form with the previous inputs
        if messages.get_messages(request):
            return render(request, 'chatapp/feedback.html', {
                "email": email,
                "feedback_text": feedback_text,
                "rating": rating
            })

        # Store data in the database
        try:
            Feedback.objects.create(email=email, feedback_text=feedback_text, rating=rating)
            messages.success(request, "Thank you for your feedback!")
            return redirect('feedback')  # Redirect to clear the form
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    # Ensure that an HttpResponse is always returned
    return render(request, 'chatapp/feedback.html')

def contact(request):
    """Renders the Contact page."""
    return render(request, "chatapp/contact.html")
