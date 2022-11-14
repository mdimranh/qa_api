from django.db import models

from users.models import User


class Question(models.Model):
    question = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    share = models.IntegerField(default=0)

    def preview(self):
        return self.question[0:25]+"..." if len(self.question) > 25 else self.question

    def total_answer(self):
        return Answer.objects.filter(id = self.id).count()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    answers = models.TextField()
