from django.shortcuts import render
from django.contrib.auth import views as v 
from django.contrib.auth import forms as f
from django.views.generic import (
    CreateView,
)
from .forms import RegisterForm


class LoginView(v.LoginView):
    template_name = 'registration/login.html'
    form_class = f.AuthenticationForm


class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name= 'signup.html'
    success_url = '/'
