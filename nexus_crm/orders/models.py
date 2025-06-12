from django.db import models
from django.urls import reverse
from django.db.models import When, Case, Value, IntegerField
from django.utils import timezone
from django.core.validators import MinValueValidator, FileExtensionValidator


from clients.models import Clients
from orders.manager import OrdersManager
from users.models import UserProfile


# Create your models here.
class Orders(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В работе'),
        ('completed', 'Завершена'),
        ('canceled', 'Отменена'),
    ]
    client = models.ForeignKey(Clients, on_delete=models.CASCADE,
                               verbose_name="Клиент", related_name="orders_requests" ,null=True)


    address = models.TextField(verbose_name="Адрес", blank=True)
    description = models.TextField(verbose_name="Описание заявки")
    cost_price = models.DecimalField(verbose_name="Себестоимость услуги",
                                     max_digits=10,
                                     decimal_places=2,
                                     blank=True,
                                     null=True,
                                     default=0
                                     )
    total_price = models.DecimalField(verbose_name="Общая стоимость",
                                      max_digits=10,
                                      decimal_places=2,
                                      blank=True,
                                      null=True,
                                      default=0)
    manager = models.ForeignKey(to=UserProfile,
                                on_delete=models.SET_NULL,
                                related_name="orders_requests",
                                null=True, blank=True)
    service = models.ForeignKey(to="Service",
                                on_delete=models.SET_NULL,
                                related_name="orders_requests",
                                null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='in_progress', max_length=15)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Дата и время изменения")

    objects = OrdersManager()



    def __str__(self):
        return f"Заявка №{self.pk} для клиента {self.client.name}."

    def get_absolute_url(self):
        return reverse("crm:service_request_detail", args=[self.pk])

    @property
    def profit(self):
        """Рассчитывает прибыль по заявке"""
        total = self.total_price or 0
        cost = self.cost_price or 0
        return total - cost

    class Meta:
        db_table = "orders"
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


class OrderCase(models.Model):
    """
    Одна составная часть кейса себестоимости
    """
    title = models.CharField(
        max_length=300,
        verbose_name="Название"
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Стоимость",
        default=0
    )
    cost_price_case = models.ForeignKey(
        to=Orders,
        related_name="parts",
        verbose_name="Часть себестоимости",
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = "order_cases"
        verbose_name = "Часть кейса себестоимости"
        verbose_name_plural = "Части кейсов себестоимости"


class OrderFile(models.Model):
    order = models.ForeignKey(
        Orders,
        related_name='files',
        on_delete=models.CASCADE
    )
    file = models.FileField(upload_to='order_files/', verbose_name="Документ")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return f"File for order {self.order.id}: {self.file.name}"

    class Meta:
        db_table = "order_files"
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

class Service(models.Model):
    """
    Услуга для заявки
    """
    title = models.CharField(max_length=350, verbose_name="Услуга")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "services"
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"