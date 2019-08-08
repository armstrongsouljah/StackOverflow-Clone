from django import forms
from .models import Profile


class ProfileChangeForm(forms.ModelForm):
    """ class for changing a user's profile details """

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio']
