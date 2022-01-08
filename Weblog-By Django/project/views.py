from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project 

class ProjectList(ListView):
	model = Project
	template_name = 'project/list.html'

class ProjectDetail(DetailView):
	model = Project
	template_name = 'project/detail.html'