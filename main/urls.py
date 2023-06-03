from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about_us, name='about_us'),
    path('exercise', views.exercise, name='exercise'),
    path('login', views.login, name='login'),
    path('questions/<int:question_id>', views.question_detail, name='question_detail'),
    path('questions/<int:question_id>/answer', views.answer_question, name='answer_question'),
]

