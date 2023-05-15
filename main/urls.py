from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lesson_list'),
    path('index2', views.index2, name='lesson_list'),
    path('questions/<int:question_id>/', views.question_detail, name='question_detail'),
    path('questions/<int:question_id>/answer/', views.answer_question, name='answer_question'),
]

