from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views import generic as g
from django.contrib.auth import mixins as m
from .forms import ProfileChangeForm
from .models import Profile


User = getattr(settings, 'AUTH_USER_MODEL')

class ProfileUpdateView(m.LoginRequiredMixin, g.UpdateView):
    template_name = 'profile_change_form.html'
    form_class = ProfileChangeForm
    success_url = '/accounts/profile/'

    def get_object(self):
        username = self.request.user
        return get_object_or_404(Profile, user=username)


