from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from utils.helper_funcs import create_unique_slug
from django.urls import reverse

User = getattr(settings, 'AUTH_USER_MODEL')


class Question(models.Model):
    """ Holds information regarding questions """
    title = models.CharField(max_length=203)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(verbose_name='Detail')
    question_slug = models.CharField(blank=True, max_length=250)
    date_asked = models.DateTimeField(verbose_name='Asked On', auto_now_add=True)

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
