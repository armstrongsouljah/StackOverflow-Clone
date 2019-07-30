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
        user.save(using=self._db)
        return user

    
    def create_staffuser(self, email, password):
        user =  self.create_user(email, password=password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.staff = True
        user.admin = True
        user.save(using= self._db)
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

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return f"{self.email}"

    def get_username(self):
        return self.email
    
    def get_fullname(self):
        return self.email

    def get_shortname(self):
        return self.email.split('@')[0]
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def has_perm(self, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    

    
