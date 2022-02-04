from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class UserModel(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    mobile_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [mobile_no, name]
