from django.shortcuts import render
from django.utils import timezone

from .models import Question
from .models import QuestionField


def index(request):
    all_questions = Question.objects.order_by('-datetime')
    if request.method == 'POST':
        field = QuestionField(request.POST)
        if field.is_valid():
            question = Question(data=request.POST['data'],
                                datetime=timezone.now())
            question.save()

    else:
        field = QuestionField()

    return render(request, 'questions/index.html',
                  {'field': field, 'questions': all_questions})
