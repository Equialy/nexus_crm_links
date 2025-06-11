from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils import timezone

from users.manager import MyUserManager


# Create your models here.

class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=50, verbose_name="username", null=True, blank=False, unique=True)
    telegram_id = models.CharField(max_length=15, verbose_name="telegram",
                                   blank=True, null=True,
                                   default=None, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    phone_regex = RegexValidator(regex=r'^((\+7)|8)\d{10}$',
                                 message="Phone number must be entered in the format: '+79999999999' or '89999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16, verbose_name="телефон", null=True,
                                    blank=True)

    email_notification = models.BooleanField(default=True, verbose_name="Оповещения на почту")
    telegram_notification = models.BooleanField(default=True, verbose_name="Оповещения в телеграм")
    day_off_notification = models.BooleanField(default=False, verbose_name="Оповещения по выходным")

    def __str__(self):
        return f"Профиль пользователя {self.username}"

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user_profile"
        verbose_name = "Профиль менеджера"
        verbose_name_plural = "Профили менеджеров"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
