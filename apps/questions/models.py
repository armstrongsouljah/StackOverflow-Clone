from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _
from utils.helper_funcs import create_unique_slug
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from apps.comments.models import Comment

User = getattr(settings, 'AUTH_USER_MODEL')

class Tag(models.Model):
    name = models.CharField(max_length=120, unique=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _('Question Tag')
        verbose_name_plural = _('Question Tags')


class Question(models.Model):
    """ Holds information regarding questions """
    title = models.CharField(max_length=203)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(verbose_name='Detail')
    question_slug = models.CharField(blank=True, max_length=250)
    date_asked = models.DateTimeField(verbose_name='Asked On', auto_now_add=True)
    comments = GenericRelation(Comment)
    tags = models.ManyToManyField(Tag, related_name='question_tags', blank=True)


    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-date_asked']

    def get_absolute_url(self):
        return reverse('questions:detail', kwargs={'question_slug': self.question_slug})

    
def pre_save_question_receiver(instance, *args, **kwargs):
    if not instance.question_slug:
        instance.question_slug = create_unique_slug(instance.title)

pre_save.connect(pre_save_question_receiver, sender=Question)
