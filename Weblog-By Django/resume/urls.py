from django.urls import path
from .views import home

app_name = 'resume'

urlpatterns = [
    path('', home, name='home'),
]