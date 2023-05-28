from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('questions/<int:question_id>/', views.question_detail, name='question_detail'),
    path('questions/<int:question_id>/answer/', views.answer_question, name='answer_question'),
]

