import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Country


def index(request):
    return render(request, 'core/index.html')


def question(request):
    count = Country.objects.all().count()
    randint_lst = random.sample(range(1, count + 1), 4)
    countries = [get_object_or_404(Country, pk=key) for key in randint_lst]
    possible_answers = [country.capital for country in countries]
    random.shuffle(possible_answers)
    context = {
        'name': countries[0].name,
        'correct_answer': countries[0].capital,
        'possible_answers': possible_answers
    }
    return render(request, 'core/question.html', context)
    

def results(request):
    answer = request.POST.get('capital', '123')
    correct_answer = request.POST.get('correct_answer')
    correct = bool(answer == correct_answer)
    return render(request, 'core/results.html', {'correct': correct })


