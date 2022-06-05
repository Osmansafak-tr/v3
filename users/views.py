from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

from datetime import datetime

from .forms import CustomUserCreation
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreation
    template_name = 'sign_up.html'
    success_url = reverse_lazy('login')

@receiver(user_logged_out)
def sig_user_logged_out(sender, user, request, **kwargs):
    request.user.user_logout_time = datetime.now()
    request.user.save()

