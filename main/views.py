from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
# from .models import Lesson, Question
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .forms import *
from .models import *
from .utils import *


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
    result = None
    if request.method == 'POST':
        # print(request.text)
        input_value = request.POST.get('input')
        # Run your Python script here using the input_value
        # ...
        # print(input_value)
        if input_value is None:
            result = 'Введите ответ!'

        elif input_value == '--version':
            # return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
            result = 'Правильный ответ!'
        else:
            # print(input_value)
            result = 'Неправильный ответ, прочтите лекцию еще раз!'
        # return HttpResponse('Script executed successfully')

    return render(request, 'main/exercise.html', {'result': result})


def run_script_ex2(request):
    result = None
    if request.method == 'POST':
        input_value = request.POST.get('input')
        # Run your Python script here using the input_value
        # ...
        if input_value is None:
            result = 'Введите ответ!'

        elif input_value == 'status':
            result = 'Правильный ответ!'
        else:
            result = 'Неправильный ответ, прочтите лекцию еще раз!'
        # return HttpResponse('Script executed successfully')

    return render(request, 'main/exercise_lib/exercise4.html', {'result': result})


def run_script_ex3(request):
    result = None
    if request.method == 'POST':
        input_value = request.POST.get('input')
        # Run your Python script here using the input_value
        # ...
        if input_value is None:
            result = 'Введите ответ!'

        if input_value == 'add':
            result = 'Правильный ответ!'
        else:
            result = 'Неправильный ответ, прочтите лекцию еще раз!'
        # return HttpResponse('Script executed successfully')

    return render(request, 'main/exercise_lib/exercise5.html', {'result': result})


def run_script_ex4(request):
    result = None
    if request.method == 'POST':
        input_value1 = request.POST.get('input1')
        input_value2 = request.POST.get('input2')
        # Run your Python script here using the input_value
        # ...
        if input_value1 is None:
            if input_value2 is None:
                result = 'Введите ответ!'
            result = 'Введите ответ!'

        if input_value1 == 'commit' and input_value2 == '-m':
            result = 'Правильный ответ!'
        else:
            result = 'Неправильный ответ, прочтите лекцию еще раз!'
        # return HttpResponse('Script executed successfully')

    return render(request, 'main/exercise_lib/exercise6.html', {'result': result})


def run_script_ex5(request):
    result = None
    if request.method == 'POST':
        input_value = request.POST.get('input')
        # Run your Python script here using the input_value
        # ...
        if input_value is None:
            result = 'Введите ответ!'

        if input_value == 'help':
            result = 'Правильный ответ!'
        else:
            result = 'Неправильный ответ, прочтите лекцию еще раз!'
        # return HttpResponse('Script executed successfully')

    return render(request, 'main/exercise_lib/exercise7.html', {'result': result})

def about_us(request):
    return render(request, 'main/about.html')

def register(request):
    return render(request, 'main/register.html')

# def login(request):
#     return render(request, 'main/register.html')

def cabinet(request):
    return render(request, 'main/cabinet.html')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


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

