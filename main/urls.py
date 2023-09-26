from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,  name='index'),
    path('main/about/', views.about, name='about'),
    path('main/', views.start_page, name='start_walk'),
    path('main/<int:plant_id>/', views.plant_detail, name='plant_detail'),
    path('main/previous/<int:plant_id>/', views.previous_plant, name='previous_plant'),
    path('main/next/<int:plant_id>/', views.next_plant, name='next_plant'),


]