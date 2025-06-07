from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=15, verbose_name="telegram",
                                   blank=True, null=True,
                                   default=None, unique=True)
    phone_number = models.CharField(max_length=16, verbose_name="телефон", blank=True)
    email_notification = models.BooleanField(default=True, verbose_name="Оповещения на почту")
    telegram_notification = models.BooleanField(default=True, verbose_name="Оповещения в телеграм")
    day_off_notification = models.BooleanField(default=False, verbose_name="Оповещения по выходным")

    def __str__(self):
        return f"Профиль пользователя {self.user.username}"

    class Meta:
        db_table = "user_profile"
        verbose_name = "Профиль менеджера"
        verbose_name_plural = "Профили менеджеров"

