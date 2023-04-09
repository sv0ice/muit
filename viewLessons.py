# training_app/views.py

from django.shortcuts import render, get_object_or_404
from .models import Lesson, Question
from django.shortcuts import redirect
from django.contrib import messages

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lesson_list.html', {'lessons': lessons})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'question_detail.html', {'question': question})

# training_app/views.py

def answer_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        answer = request.POST['answer']
        if answer.strip() == question.answer.strip():
            messages.success(request, 'Correct!')
        else:
            messages.error(request, 'Incorrect!')
        return redirect('question_detail', question_id=question.id)

