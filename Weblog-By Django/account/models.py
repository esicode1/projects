from datetime import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.urls import reverse



class User(AbstractUser):
	email = models.EmailField(unique=True)
	is_author = models.BooleanField(default=False)
	special_user = models.DateTimeField(default=timezone.now)
	
	def is_special_user(self):
		if self.special_user > timezone.now():
			return True
		else:
			return False
		
	is_special_user.boolean = True
	
	def get_absolute_url(self):
		return reverse("login")