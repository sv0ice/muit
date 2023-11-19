from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    # class GroupManager(models.Manager):
    #     """
    #     The manager for the auth's Group model.
    #     """
    #
    #     use_in_migrations = True
    #
    #     def get_by_natural_key(self, name):
    #         return self.get(name=name)

    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # settings.AUTH_USER_MODEL
    answer1 = models.TextField(default="Не выполнено!")
    answer2 = models.TextField(default="Не выполнено!")
    answer3 = models.TextField(default="Не выполнено!")
    answer4 = models.TextField(default="Не выполнено!")
    answer5 = models.TextField(default="Не выполнено!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#
# class Lesson(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#