from django.shortcuts import render, get_object_or_404
from .models import QuestionAnswer

def chatbot_view(request):
    questions = QuestionAnswer.objects.all()
    question_id = request.GET.get('question_id')
    answer = None

    if question_id:
        question_obj = get_object_or_404(QuestionAnswer, id=question_id)
        answer = question_obj.answer

    return render(request, 'chatapp/chatbot.html', {'questions': questions, 'answer': answer})
