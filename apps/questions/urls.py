from django.urls import path
from .views import (
    QuestionAddView,
    QuestionDetailView,
    QuestionUpdateView,
    QuestionDeleteView,
    TagAddView,
)
app_name = 'questions'
urlpatterns = [
  path('new/', QuestionAddView.as_view(), name='add'),
  path('<question_slug>/view/', QuestionDetailView.as_view(), name='detail'),
  path('<question_slug>/update/', QuestionUpdateView.as_view(), name='update'),
  path('<question_slug>/delete/', QuestionDeleteView.as_view(), name='delete'),
  path('tag', TagAddView.as_view(), name='add-tag')
]