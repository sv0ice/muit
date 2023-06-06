from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about_us, name='about_us'),
    path('exercise', views.exercise, name='exercise'),
    path('exercise2', views.exercise2, name='exercise2'),
    path('exercise3', views.exercise3, name='exercise3'),
    path('exercise4', views.exercise4, name='exercise4'),
    path('exercise5', views.exercise5, name='exercise5'),
    path('exercise6', views.exercise6, name='exercise6'),
    path('exercise7', views.exercise7, name='exercise7'),
    path('output1', views.run_script_ex1, name='run_script_ex1'),
    path('output2', views.run_script_ex2, name='run_script_ex2'),
    path('output3', views.run_script_ex3, name='run_script_ex3'),
    path('output4', views.run_script_ex4, name='run_script_ex4'),
    path('output5', views.run_script_ex5, name='run_script_ex5'),
    path('login', views.login, name='login'),
    # path('questions/<int:question_id>', views.question_detail, name='question_detail'),
    # path('questions/<int:question_id>/answer', views.answer_question, name='answer_question'),
]

