from django.shortcuts import render, get_object_or_404
# from .models import Lesson, Question
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def exercise(request):
    return render(request, 'main/exercise.html')


def exercise2(request):
    return render(request, 'main/exercise_lib/exercise2.html')


def exercise3(request):
    return render(request, 'main/exercise_lib/exercise3.html')


def exercise4(request):
    return render(request, 'main/exercise_lib/exercise4.html')


def exercise5(request):
    return render(request, 'main/exercise_lib/exercise5.html')


def exercise6(request):
    return render(request, 'main/exercise_lib/exercise6.html')


def exercise7(request):
    return render(request, 'main/exercise_lib/exercise7.html')


def run_script_ex1(request):
    if request.method == 'POST':
        # print(request.text)
        input_value = request.POST.get('input')
        # Run your Python script here using the input_value
        # ...
        # print(input_value)
        if input_value is None:
            return HttpResponse('Input value is missing')

        if input_value == '--version':
            return HttpResponse('CORRECT!')
        else:
            # print(input_value)
            return HttpResponse('NOT CORRECT!')
        # return HttpResponse('Script executed successfully')
    else:
        return render(request, 'main/exercise.html')


def run_script_ex2(request):
    if request.method == 'POST':
        input_value = request.POST.get('input')
        # Run your Python script here using the input_value
        # ...
        if input_value is None:
            return HttpResponse('Input value is missing')

        if input_value == 'status':
            return HttpResponse('CORRECT!')
        else:
            return HttpResponse('NOT CORRECT!')
        # return HttpResponse('Script executed successfully')
    else:
        return render(request, 'main/exercise4.html')


def run_script_ex3(request):
    if request.method == 'POST':
        input_value = request.POST.get('input')
        # Run your Python script here using the input_value
        # ...
        if input_value is None:
            return HttpResponse('Input value is missing')

        if input_value == 'add':
            return HttpResponse('CORRECT!')
        else:
            return HttpResponse('NOT CORRECT!')
        # return HttpResponse('Script executed successfully')
    else:
        return render(request, 'main/exercise4.html')


def run_script_ex4(request):
    if request.method == 'POST':
        input_value1 = request.POST.get('input1')
        input_value2 = request.POST.get('input2')
        # Run your Python script here using the input_value
        # ...
        if input_value1 is None:
            if input_value2 is None:
                return HttpResponse('Input value is missing')
            return HttpResponse('Input value is missing')

        if input_value1 == 'commit' and input_value2 == '-m':
            return HttpResponse('CORRECT!')
        else:
            return HttpResponse('NOT CORRECT!')
        # return HttpResponse('Script executed successfully')
    else:
        return render(request, 'main/exercise4.html')


def run_script_ex5(request):
    if request.method == 'POST':
        input_value = request.POST.get('input')
        # Run your Python script here using the input_value
        # ...
        if input_value is None:
            return HttpResponse('Input value is missing')

        if input_value == 'help':
            return HttpResponse('CORRECT!')
        else:
            return HttpResponse('NOT CORRECT!')
        # return HttpResponse('Script executed successfully')
    else:
        return render(request, 'main/exercise4.html')

def about_us(request):
    return render(request, 'main/about.html')

def login(request):
    return render(request, 'main/login.html')


# def lesson_list(request):
#     lessons = Lesson.objects.all()
#     return render(request, 'main/lesson_list.html', {'lessons': lessons})
#
#
# def question_detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'main/question_detail.html', {'question': question})
#
#
# def answer_question(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == 'POST':
#         answer = request.POST['answer']
#         if answer.strip() == question.answer.strip():
#             messages.success(request, 'Correct!')
#         else:
#             messages.error(request, 'Incorrect!')
#         return redirect('question_detail', question_id=question.id)

