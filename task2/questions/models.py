from django.db import models
from django.forms import ModelForm


class Question(models.Model):
    data = models.CharField(max_length=1024)
    datetime = models.DateTimeField('published')

    def __str__(self):
        return self.data


class QuestionField(ModelForm):
    class Meta:
        model = Question
        fields = ['data']
