from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise TypeError('Email must not be blank')

        if not password:
            raise TypeError('Password must not be blank')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    
    def create_staffuser(self, email, password):
        user =  self.create_user(email=email, password=password)
        user.staff = True
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.staff = True
        user.admin = True
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.email}"

    def get_username(self):
        return self.email
    
    def get_fullname(self):
        return self.email

    def get_shortname(self):
        return self.email.split('@')[0]

    

    
