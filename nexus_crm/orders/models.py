from django.db import models
from django.urls import reverse
from django.db.models import When, Case, Value, IntegerField

from users.models import UserProfile


# Create your models here.
class Orders(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В работе'),
        ('completed', 'Завершена'),
        ('canceled', 'Отменена'),
    ]
    # TODO сделать отношение к таблице клиента

    address = models.TextField(verbose_name="Адрес", blank=True)
    description = models.TextField(verbose_name="Описание заявки")
    cost_price = models.IntegerField(verbose_name="Себестоимость услуги",
                                     blank=True,
                                     null=True,
                                     default=0
                                     )
    total_price = models.PositiveIntegerField(verbose_name="Общая стоимость",
                                              blank=True,
                                              null=True,
                                              default=0)
    manager = models.ForeignKey(to=UserProfile,
                                on_delete=models.SET_NULL,
                                related_name="service_requests",
                                null=True, blank=True)
    # service = models.ForeignKey(to="Service",
    #                             on_delete=models.SET_NULL,
    #                             related_name="service_requests",
    #                             null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='in_progress', max_length=15)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Дата и время изменения")
    #
    # def __str__(self):
    #     return f"Заявка №{self.pk} для клиента {self.client.name}."

    def get_absolute_url(self):
        return reverse("crm:service_request_detail", args=[self.pk])

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = [
            Case(
                When(status='in_progress', then=Value(0)),
                When(status='completed', then=Value(1)),
                When(status='canceled', then=Value(2)),
                default=Value(3),
                output_field=IntegerField()
            ),
            "-updated_at"
        ]
