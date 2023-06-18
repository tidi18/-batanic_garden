from django.utils.crypto import get_random_string
from .forms import RegisterForm
from .models import Visitor, Time, Event
from django.shortcuts import render, redirect
from .forms import TokenCheckForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['last_name']
            time_str = form.cleaned_data['time']
            time = Time.objects.get(time=time_str)
            event = Event.objects.get(time=time)

            total_limit = event.total

            total_visitors = Visitor.objects.count()
            if total_visitors >= total_limit:
                limit_errors = 'Извините все билеты распроданы!'
                return render(request, 'register/limit_errors.html', {'limit_errors': limit_errors})

            if time.number_in_the_group < Visitor.objects.filter(time=time).count():
                limit_errors = 'Извините группа переполнена запишитесь в другое время ! '
                return render(request, 'register/limit_errors.html', {'limit_errors': limit_errors})

            token = get_random_string(10)

            visitor = Visitor(time=time, name=name, last_name=surname, token=token)
            visitor.save()

            return render(request, 'register/success.html', {'token': token})
    else:
        form = RegisterForm()

    return render(request, 'register/register.html', {'form': form})


def check_token(request):
    if request.method == 'POST':
        form = TokenCheckForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            token = form.cleaned_data['token']

            try:
                visitor = Visitor.objects.get(name=name, last_name=last_name, token=token)
                # Проверка на совпадение имени, фамилии и токена

                # Редирект на другую страницу
                return redirect('start_walk')
            except Visitor.DoesNotExist:
                # Ошибка, если запись не найдена
                error_message = 'Ошибка: данные не совпадают!'
                return render(request, 'register/error_token_check.html', {'error_message': error_message})
    else:
        form = TokenCheckForm()

    return render(request, 'register/token_check.html', {'form': form})


