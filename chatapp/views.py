from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import AskQuestionForm
from .models import QuestionAnswer, UserQuery

def HomeView(request):
    return render(request, 'chatapp/home.html')

def ChatView(request):
    questions = QuestionAnswer.objects.all()
    question_id = request.GET.get('question_id')
    answer = None

    if question_id:
        question_obj = get_object_or_404(QuestionAnswer, id=question_id)
        answer = question_obj.answer

    return render(request, 'chatapp/chatbot.html', {'questions': questions, 'answer': answer})


def AskQuestionView(request):
    if request.method == "POST":
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            query = form.save()  # Saves the query in the database

            subject = f"New Query from {query.name}"
            message = f"Dear {query.name},\n\nYour query has been received.\n\n**Question:** {query.question}\n\nThe department will reply soon.\n\nBest,\nCUH Team"
            
            # Send email to user
            send_mail(subject, message, 'noreply@cuh.ac.in', [query.email])

            # Send email to department
            dept_message = f"New query received from {query.name} ({query.email}):\n\n{query.question}\n\nPlease reply to {query.email}."
            send_mail(f"New Query from {query.name}", dept_message, 'noreply@cuh.ac.in', [query.department])

            messages.success(request, "Your query has been submitted successfully!")
            return redirect("ask_question")
    else:
        form = AskQuestionForm()

    return render(request, "chatapp/ask_question.html", {"form": form})
