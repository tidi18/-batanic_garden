from django.urls import path
from . import views
urlpatterns = [
    path('', views.register,  name='register'),
    path('token_check.html', views.check_token, name='check_token')


]