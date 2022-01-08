# from django.contrib.auth import views
from django.urls import path
from .views import (
    ProjectList,
    ProjectCreate,
    ProjectUpdate,
    ProjectDelete,
    Profile,
) 


app_name = 'account'


urlpatterns = [
    path('', ProjectList.as_view(), name='home'),
    path('article/create', ProjectCreate.as_view(), name='project-create'),
    path('article/update/<int:pk>', ProjectUpdate.as_view(), name='project-update'),
    path('article/delete/<int:pk>', ProjectDelete.as_view(), name='project-delete'),
    path('profile/', Profile.as_view(), name='profile'),

]