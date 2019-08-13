from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = getattr(settings, 'AUTH_USER_MODEL')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, null=True, max_length=123)
    last_name = models.CharField(blank=True, null=True, max_length=123)
    bio = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        ordering = ['-created_at']



def profile_pre_save_receiver(instance, created,  *args, **kwargs):
    if created:
        Profile.objects.get_or_create(
            user=instance
        )

post_save.connect(profile_pre_save_receiver, sender=User)


