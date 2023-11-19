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

# === my filter ===
# from .filters import QuestionFilter



def index(request):
    return render(request, 'main/index.html')


def exercise(request):
    return render(request, 'main/exercise.html')


def exercise2(request):
    return render(request, 'main/exercise_lib/exercise2.html')


def exercise3(request):
    return render(request, 'main/exercise_lib/exercise3.html')


def exercise4(request):
    request.session['mid'] = request.user.id
    uid = request.session['mid']
    userobj = User.objects.get(id=uid)
    answer1 = Question.objects.filter(user=userobj).values('answer1').last()

    return render(request, 'main/exercise_lib/exercise4.html', {'answer1': answer1['answer1']})


def exercise5(request):
    request.session['mid'] = request.user.id
    uid = request.session['mid']
    userobj = User.objects.get(id=uid)
    answer2 = Question.objects.filter(user=userobj).values('answer2').last()

    return render(request, 'main/exercise_lib/exercise5.html', {'answer2': answer2['answer2']})


def exercise6(request):
    request.session['mid'] = request.user.id
    uid = request.session['mid']
    userobj = User.objects.get(id=uid)
    answer3 = Question.objects.filter(user=userobj).values('answer3').last()

    return render(request, 'main/exercise_lib/exercise6.html', {'answer3': answer3['answer3']})


def exercise7(request):
    request.session['mid'] = request.user.id
    uid = request.session['mid']
    userobj = User.objects.get(id=uid)
    answer4 = Question.objects.filter(user=userobj).values('answer4').last()

    return render(request, 'main/exercise_lib/exercise7.html', {'answer4': answer4['answer4']})



def run_script_ex1(request):
    if request.user.is_authenticated:
        result = None
        # answer1 = None
        request.session['mid'] = request.user.id
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)

        if request.method == 'POST':
            input_value = request.POST.get('input')
            if input_value is None:
                result = 'Введите ответ!'

            elif input_value == '--version':
                # return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
                result = 'Правильный ответ!'
                q = Question(user=userobj, answer1="Выполнено!")
                # if q.answer is True:
                # answer1 = Question.objects.filter(user=userobj, answer1="Правильный ответ!")
                # answer1 = q.answer1
                # Save the object into the database. You have to call save() explicitly.
                q.save()

            else:
                result = 'Неправильный ответ, прочтите лекцию еще раз!'
                q = Question(user=userobj, answer1="Не выполнено!")
                # answer1 = q.objects.filter(user=userobj, answer1="Неправильный ответ, прочтите лекцию еще раз!")
                # answer1 = q.answer1
                # Save the object into the database. You have to call save() explicitly.
                q.save()
        data = {
            'result': result,
            # 'answer1': answer1
        }
        return render(request, 'main/exercise.html', context=data)
    else:
        pass



def run_script_ex2(request):
    if request.user.is_authenticated:
        result = None
        # answer1 = None  # Проверка на выполнение первой задачи
        request.session['mid'] = request.user.id
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)

        if request.method == 'POST':
            input_value = request.POST.get('input')
            if input_value is None:
                result = 'Введите ответ!'

            elif input_value == 'status':
                # return redirect(request.META.get('HTTP_REFERER','redirect_if_referer_not_found'))
                result = 'Правильный ответ!'
                q = Question(user=userobj,  answer1="Выполнено!", answer2="Выполнено!")
                # answer1 = Question.objects.filter(user=userobj).values('answer1').last()
                # Save the object into the database. You have to call save() explicitly.
                q.save()  # Сразу загружает в БАЗУ ДАННЫХ, т.е сохраняет каждый объект после выполнения скрипта

            else:
                result = 'Неправильный ответ, прочтите лекцию еще раз!'
                q = Question(user=userobj, answer1="Выполнено!", answer2="Не выполнено!")
                # answer1 = Question.objects.filter(user=userobj).values('answer1').last()
                # Save the object into the database. You have to call save() explicitly.
                q.save()
        data = {
            'result': result,
            # 'answer1': answer1['answer1']
        }
        return render(request, 'main/exercise_lib/exercise4.html', context=data)
    else:
        pass


def run_script_ex3(request):
    if request.user.is_authenticated:
        result = None
        # answer2 = None  # Проверка на выполнение задачи
        request.session['mid'] = request.user.id
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)

        if request.method == 'POST':
            input_value = request.POST.get('input')
            if input_value is None:
                result = 'Введите ответ!'

            elif input_value == 'add':
                result = 'Правильный ответ!'
                q = Question(user=userobj,  answer1="Выполнено!", answer2="Выполнено!", answer3="Выполнено!")
                # answer2 = Question.objects.filter(user=userobj).values('answer2').last()
                # Save the object into the database. You have to call save() explicitly.
                q.save()

            else:
                result = 'Неправильный ответ, прочтите лекцию еще раз!'
                q = Question(user=userobj, answer1="Выполнено!", answer2="Выполнено!", answer3="Не выполнено!")
                # answer2 = Question.objects.filter(user=userobj).values('answer2').last()
                # Save the object into the database. You have to call save() explicitly.
                q.save()

        data = {
            'result': result,
            # 'answer3': answer2['answer2']
        }

        return render(request, 'main/exercise_lib/exercise5.html', context=data)
    else:
        pass

# def run_script_ex3(request):
#     result = None
#     if request.method == 'POST':
#         input_value = request.POST.get('input')
#         # Run your Python script here using the input_value
#         # ...
#         if input_value is None:
#             result = 'Введите ответ!'
#
#         if input_value == 'add':
#             result = 'Правильный ответ!'
#         else:
#             result = 'Неправильный ответ, прочтите лекцию еще раз!'
#         # return HttpResponse('Script executed successfully')
#
#     return render(request, 'main/exercise_lib/exercise5.html', {'result': result})


def run_script_ex4(request):
    if request.user.is_authenticated:
        result = None
        # answer3 = None  # Проверка на выполнение задачи
        request.session['mid'] = request.user.id
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)

        if request.method == 'POST':
            input_value1 = request.POST.get('input1')
            input_value2 = request.POST.get('input2')

            if input_value1 is None or input_value2 is None:
                result = 'Введите ответ!'

            elif input_value1 == 'commit' and input_value2 == '-m':
                result = 'Правильный ответ!'
                q = Question(user=userobj,  answer1="Выполнено!", answer2="Выполнено!", answer3="Выполнено!", answer4="Выполнено!")
                # answer3 = Question.objects.filter(user=userobj).values('answer3').last()
                # Save the object into the database. You have to call save() explicitly.
                q.save()

            else:
                result = 'Неправильный ответ, прочтите лекцию еще раз!'
                q = Question(user=userobj, answer1="Выполнено!", answer2="Выполнено!", answer3="Выполнено!", answer4="Не выполнено!")
                # answer3 = Question.objects.filter(user=userobj).values('answer3').last()
                # Save the object into the database. You have to call save() explicitly.
                q.save()

        data = {
            'result': result,
            # 'answer3': answer3['answer3']
        }
        return render(request, 'main/exercise_lib/exercise6.html', context=data)
    else:
        pass


# def run_script_ex4(request):
#     result = None
#     if request.method == 'POST':
#         input_value1 = request.POST.get('input1')
#         input_value2 = request.POST.get('input2')
#         # Run your Python script here using the input_value
#         # ...
#         if input_value1 is None:
#             if input_value2 is None:
#                 result = 'Введите ответ!'
#             result = 'Введите ответ!'
#
#         if input_value1 == 'commit' and input_value2 == '-m':
#             result = 'Правильный ответ!'
#         else:
#             result = 'Неправильный ответ, прочтите лекцию еще раз!'
#         # return HttpResponse('Script executed successfully')
#
#     return render(request, 'main/exercise_lib/exercise6.html', {'result': result})


def run_script_ex5(request):
    if request.user.is_authenticated:
        result = None
        # answer4 = None # Проверка на выполнение задачи
        request.session['mid'] = request.user.id
        uid = request.session['mid']
        userobj = User.objects.get(id=uid)

        if request.method == 'POST':
            input_value = request.POST.get('input')
            if input_value is None:
                result = 'Введите ответ!'

            elif input_value == 'help':
                result = 'Правильный ответ!'
                q = Question(user=userobj, answer1="Выполнено!", answer2="Выполнено!", answer3="Выполнено!", answer4="Выполнено!", answer5="Выполнено!")
                # answer4 = Question.objects.filter(user=userobj).values('answer4').last()
                # Save the object into the database. You have to call save() explicitly.
                q.save()

            else:
                result = 'Неправильный ответ, прочтите лекцию еще раз!'
                q = Question(user=userobj, answer1="Выполнено!", answer2="Выполнено!", answer3="Выполнено!", answer4="Выполнено!", answer5="Не выполнено!")
                # answer4 = Question.objects.filter(user=userobj).values('answer4').last()
                # Save the object into the database. You have to call save() explicitly.
                q.save()

        data = {
            'result': result,
            # 'answer4': answer4['answer4']
        }

        return render(request, 'main/exercise_lib/exercise7.html', context=data)
    else:
        pass

def about_us(request):
    return render(request, 'main/about.html')

def register(request):
    return render(request, 'main/register.html')

# def login(request):
#     return render(request, 'main/register.html')

def cabinet(request):
    answer1 = None
    answer2 = None
    answer3 = None
    answer4 = None
    answer5 = None

    request.session['mid'] = request.user.id
    uid = request.session['mid']
    userobj = User.objects.get(id=uid)

    answers1_list = Question.objects.filter(user=userobj).values('answer1')
    answers2_list = Question.objects.filter(user=userobj).values('answer2')
    answers3_list = Question.objects.filter(user=userobj).values('answer3')
    answers4_list = Question.objects.filter(user=userobj).values('answer4')
    answers5_list = Question.objects.filter(user=userobj).values('answer5')
    # myfilter = QuestionFilter()

    if Question.objects.filter(user=userobj):
        # Returns QuerySet - I should restore the set
        # upd: I solved a problem
        answer1 = answers1_list.last()
        answer2 = answers2_list.last()
        answer3 = answers3_list.last()
        answer4 = answers4_list.last()
        answer5 = answers5_list.last()

        # === OLD CODE ===
        # answer3 = Question.objects.filter(user=userobj, answer3="Правильный ответ!")
        # answer4 = Question.objects.filter(user=userobj, answer4="Правильный ответ!")
        # answer5 = Question.objects.filter(user=userobj, answer5="Правильный ответ!")
        # answers = Question.objects.all()

    data = {
        'answer1': answer1['answer1'],
        'answer2': answer2['answer2'],
        'answer3': answer3['answer3'],
        'answer4': answer4['answer4'],
        'answer5': answer5['answer5'],
    }

    return render(request, 'main/cabinet.html', context=data)  # , {'user_question': answer}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    # user = form_class.save()
    # Question.objects.create(user=user)

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

