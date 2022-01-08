from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'resume/home.html')

def contact(request):
	return render(request, 'resume/contact.html')

def about(request):
	return render(request, 'resume/about.html')