from django import forms
from .models import Question, Tag
from apps.comments.models import Comment

class QuestionForm(forms.ModelForm):
    """ form for adding and updating the question details """

    class Meta:
        model  = Question
        fields = ('title', 'question', 'tags', )


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name',]

    def clean_name(self):
        tag_name = self.cleaned_data.get('name')
        tag_qs = Tag.objects.filter(name__iexact=tag_name)
        
        if tag_qs.exists():
            raise forms.ValidationError("This tag has already been added, add a different tag")
        return tag_name
