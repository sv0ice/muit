# git_training/urls.py

from django.urls import path
from training_app.views import lesson_list, question_detail, answer_question

urlpatterns = [
    path('', lesson_list, name='lesson_list'),
    path('questions/<int:question_id>/', question_detail, name='question_detail'),
    path('questions/<int:question_id>/answer/', answer_question, name='answer_question'),
]

