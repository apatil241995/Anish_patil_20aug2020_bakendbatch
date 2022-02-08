from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserModelManager(BaseUserManager):
    def create_user(self, email, date_of_birth, mobile_no, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            mobile_no=mobile_no,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, mobile_no, name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            date_of_birth=date_of_birth,
            mobile_no=mobile_no,
            name=name,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_staff(self, email, date_of_birth, mobile_no, name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            date_of_birth=date_of_birth,
            mobile_no=mobile_no,
            name=name,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    mobile_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [mobile_no, name, date_of_birth]

    object = UserModelManager()
