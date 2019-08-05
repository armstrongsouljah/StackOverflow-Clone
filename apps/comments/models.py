from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from apps.authentication.models import User


class Comment(models.Model):
    """ A class to allow users to comment on questions and
        eventually answers 
    """
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.author}"

    class Meta:
        ordering = ['-commented_at']
