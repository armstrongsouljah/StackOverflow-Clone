from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    """ form for adding and updating the question details """

    class Meta:
        model  = Question
        fields = ('title', 'question', )