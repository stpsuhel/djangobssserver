from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

USERNAME_REGEX = '^[A-Za-z0-9.+-]*$'


class UserManager(BaseUserManager):
    def create_user(self, username, email, name, password=None):
        if not username:
            raise ValueError('User must have a username')
        if not email:
            raise ValueError('User must have a email')

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.name = name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, name, password):
        user = self.create_user(
            username, email, name=name, password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    username = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(regex=USERNAME_REGEX,
                           message='User Name must be alphanumeric or contains numbers',
                           code='invalid_username')
        ], unique=True
    )

    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
    name = models.CharField(max_length=255)

    password = models.CharField(
        max_length=255,
        default='1234'
    )

    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True


class Amount(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    money = models.BigIntegerField()
    paymentMonth = models.CharField(max_length=50)
    paymentDay = models.CharField(max_length=50)
    paymentTime = models.CharField(max_length=50)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)

    def __str__(self):
        return self.user.username + ' has pay for ' + self.paymentMonth


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
