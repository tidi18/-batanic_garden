from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from register.models import Event
from .models import Plants


def index(request):
    list_event = Event.objects.all()
    return render(request, 'main/index.html', {'list_event': list_event})


def about(request):
    return render(request, 'main/about.html')

def start_page(request):
    if request.method == 'POST':
        plant = Plants.objects.first()  # Получаем первое растение из базы данных
        return render(request, 'main/plant_detail.html', {'plant': plant})  # Рендерим шаблон с информацией о растении
    return render(request, 'main/start_page.html')


def plant_detail(request, plant_id):
    plant = get_object_or_404(Plants, id=plant_id)
    return render(request, 'main/plant_detail.html', {'plant': plant})


def previous_plant(request, plant_id):
    current_plant = get_object_or_404(Plants, id=plant_id)
    previous_plant = Plants.objects.filter(id__lt=current_plant.id).order_by('-id').first()
    if previous_plant:
        return HttpResponseRedirect(reverse('plant_detail', args=[previous_plant.id]))
    else:
        errors = 'Дальше нечего нет!'
        return render(request, 'main/errors.html', {'errors': errors})


def next_plant(request, plant_id):
    current_plant = get_object_or_404(Plants, id=plant_id)
    next_plant = Plants.objects.filter(id__gt=current_plant.id).order_by('id').first()
    if next_plant:
        return HttpResponseRedirect(reverse('plant_detail', args=[next_plant.id]))
    else:
        errors = 'Дальше нечего нет!'
        return render(request, 'main/errors.html', {'errors': errors})