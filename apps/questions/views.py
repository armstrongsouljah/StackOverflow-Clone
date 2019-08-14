from django.shortcuts import render, get_object_or_404
from django.views import generic as g
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy, reverse
from .forms import QuestionForm, TagForm
from .models import Question, Tag
from apps.comments.forms import CommentForm
from apps.comments.models import Comment



class QuestionAddView(LoginRequiredMixin, g.CreateView):
    form_class = QuestionForm
    template_name = 'question_add_form.html'
    success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super(QuestionAddView, self).form_valid(form)


class QuestionListView(g.ListView):
    template_name = 'questions.html'
    context_object_name = 'questions'

    def get_queryset(self, *args, **kwargs):
        qs = Question.objects.all()
        return qs


class QuestionDetailView(g.DetailView, g.CreateView):
    template_name = 'question_view.html'
    context_object_name = 'question'
    form_class = CommentForm

    def get_object(self):
        slug = self.kwargs.get('question_slug')
        return get_object_or_404(Question, question_slug=slug)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.object_id = self.get_object().pk
        instance.content_type = ContentType.objects.get(app_label='questions', model='question')
        instance.author = self.request.user
        self.success_url = self.get_object().get_absolute_url()
        return super(QuestionDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related = Question.objects.filter(tags__in=self.get_object().tags.all())
        context['related_questions'] = [q for q in related if q.title != self.get_object().title]
        return context


class QuestionUpdateView(LoginRequiredMixin, g.UpdateView):
    template_name = 'question_update.html'
    context_object_name = 'question'
    form_class = QuestionForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        if instance.author != self.request.user:
            return super(QuestionUpdateView, self).form_invalid(form)
        return super(QuestionUpdateView, self).form_valid(form)

    def get_object(self):
        slug = self.kwargs.get('question_slug')
        return get_object_or_404(Question, question_slug=slug)


class QuestionDeleteView(LoginRequiredMixin, g.DeleteView):
    template_name = 'question_confirm_delete.html'
    context_object_name = 'question'
    success_url = reverse_lazy('home')

    def get_object(self):
        slug = self.kwargs.get('question_slug')
        return get_object_or_404(Question, question_slug=slug)


class TagAddView(g.CreateView):
    form_class = TagForm
    template_name = 'tag_add.html'
    success_url = '/accounts/profile'
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        return super(TagAddView, self).form_valid(form)
