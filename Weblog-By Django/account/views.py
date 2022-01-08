from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	ListView,
	CreateView, 
	UpdateView,
	DeleteView,
	)
from project.models import Project
from .mixins import (
	FieldsdMixin,
	FormValidMixin,
	AuthorAccessMixin,
	SuperUserAccessMixin,
	AuthorsAccessMixin,
	)
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView  
from .forms import ProfileForm
from .models import User

class ProjectList(AuthorsAccessMixin ,ListView):
	template_name = 'registration/home.html'
	
	def get_queryset(self):
		if self.request.user.is_superuser:
			return Project.objects.all()
		else:
			return Project.objects.filter(author=self.request.user)        
		
class ProjectCreate(AuthorsAccessMixin, FormValidMixin, FieldsdMixin, CreateView):
	model = Project
	template_name = "registration/article-create-update.html"
		
class ProjectUpdate(AuthorAccessMixin, FormValidMixin, FieldsdMixin, UpdateView):
	model = Project
	template_name = "registration/article-create-update.html"

class ProjectDelete(SuperUserAccessMixin, DeleteView):
	model = Project
	success_url = reverse_lazy('account:home')
	template_name = 'registration/article_confirm_delete.html'
	
	
class Profile(LoginRequiredMixin ,UpdateView):
	model = User
	template_name = "registration/profile.html"
	form_class = ProfileForm
	success_url = reverse_lazy("account:profile")
		
	def get_object(self ):
		return User.objects.get(pk=self.request.user.pk)
	
	def get_form_kwargs(self):
		kwargs = super(Profile, self).get_form_kwargs()
		kwargs.update({
			'user': self.request.user
		})
		return kwargs    
	
class Login(LoginView):
	def get_success_url(self):
		user = self.request.user
		
		if user.is_superuser or user.is_author:
			return reverse_lazy('resume:home')
		else:
			return reverse_lazy('account:home')


from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


class Register(CreateView):
	form_class = SignupForm
	template_name = 'registration/register.html'
 
	def form_valid(self, form):
		user = form.save(commit=False)
		user.is_active = False
		user.save()
		current_site = get_current_site(self.request)
		mail_subject = 'Activate your account.'
		message = render_to_string('registration/activate_account.html', {
			'user': user,
			'domain': current_site.domain,
			'uid':urlsafe_base64_encode(force_bytes(user.pk)),
			'token':account_activation_token.make_token(user),
		})
		to_email = form.cleaned_data.get('email')
		email = EmailMessage(
					mail_subject, message, to=[to_email]
		)
		email.send()
		return render(self.request, 'registration/send_registration_link.html')


def activate(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		return render(request, 'registration/confiramtion_done.html')
	else:
		return render(request, 'registration/confiramtion_failed.html')
