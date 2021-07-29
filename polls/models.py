from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    name = models.CharField(max_length=32, verbose_name="Poll name")
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)


TYPE = [('O', 'open'), ('S', "single"), ('M', 'multiple')]


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.TextField()
    type = models.CharField(max_length=1, choices=TYPE)
    active = models.BooleanField(default=True)

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return str(self.text)



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)

    def __repr__(self):
        return str(self.answer)

    def __str__(self):
        return str(self.answer)
