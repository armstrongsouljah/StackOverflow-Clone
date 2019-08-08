from django.shortcuts import render, get_object_or_404
from django.contrib.auth import views as v 
from django.contrib.auth import forms as f
from django.contrib.auth import mixins as m
from apps.profiles.models import Profile

from django.views import generic as g
from .forms import RegisterForm


class LoginView(v.LoginView):
    template_name = 'registration/login.html'
    form_class = f.AuthenticationForm


class RegistrationView(g.CreateView):
    form_class = RegisterForm
    template_name= 'signup.html'
    success_url = '/'


class ProfileView(m.LoginRequiredMixin, g.DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name='profile'

    def get_object(self, *args, **kwargs):
        profile_  = get_object_or_404(Profile, user=self.request.user)
        return profile_
