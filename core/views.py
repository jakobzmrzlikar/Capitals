import random

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from pinax.points.models import award_points, points_awarded

from .models import Country


def index(request):
    users = User.objects.all()
    user_list = []
    for user in users:
        tup = (user.username, points_awarded(user))
        user_list.append(tup)
    user_list.sort( key=lambda x: x[1], reverse=True)
    return render(request, 'core/index.html', {"user_list": user_list})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
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
    answer = request.POST.get('capital')
    correct_answer = request.POST.get('correct_answer')
    correct = bool(answer == correct_answer)
    if request.user.is_authenticated:
        user = request.user
    if correct:
        award_points(user, 1)
    else:
        award_points(user, -1)
    return render(request, 'core/results.html', {'correct': correct })


