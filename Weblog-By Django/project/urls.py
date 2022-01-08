from django.urls import path
from .views import ProjectList, ProjectDetail

app_name = 'project'

urlpatterns = [
    path('projects', ProjectList.as_view(), name='projects'),
    path('project/<slug:slug>/', ProjectDetail.as_view(), name='detail')
]