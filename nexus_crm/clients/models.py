from django.db import models
from django.core.validators import RegexValidator

from users.models import UserProfile


# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="ФИО Клиента")
    phone_regex = RegexValidator(regex=r'^((\+7)|8)\d{10}$',
                                 message="Phone number must be entered in the format: '+79999999999' or '89999999999'.")
    phone = models.CharField(validators=[phone_regex], max_length=16,
                             verbose_name="Телефон", )

    phone_2 = models.CharField(validators=[phone_regex], max_length=16,
                               verbose_name="Второй телефон",
                               blank=True)
    telegram = models.CharField(max_length=55,
                                verbose_name="telegram",
                                blank=True)
    email = models.EmailField(verbose_name="email", blank=True)
    manager = models.ForeignKey(to=UserProfile,
                                on_delete=models.SET_NULL,
                                related_name="clients",
                                null=True, blank=True)

    def __str__(self):
        return f"Клиент: {self.name}"

    class Meta:
        db_table = "clients"
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["-id"]
