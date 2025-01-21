from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model."""
    username = None
    email = models.EmailField(
        verbose_name='Email',
        help_text='Enter your email',
        unique=True
    )
    first_name = models.CharField(
        verbose_name='First name',
        help_text='Enter your first name',
        max_length=50,
    )
    last_name = models.CharField(
        verbose_name='Last name',
        help_text='Enter your last name',
        max_length=50,
    )
    is_staff = models.BooleanField(
        verbose_name='Staff member?',
        default=True,
    )
    is_active = models.BooleanField(
        verbose_name='Active?',
        help_text='Activate user',
        default=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('id',)

    def __str__(self):
        return self.email
