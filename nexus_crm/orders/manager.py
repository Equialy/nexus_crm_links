from django.db import models

class OrdersManager(models.Manager):
    def get_queryset(self):
        """Фильтр по дефолтному полю"""
        return super().get_queryset()

    def active(self):
        """Все заявки в работе."""
        return self.get_queryset().filter(status='in_progress')

    def by_manager(self, manager: str):
        """Заявки, назначенные конкретному менеджеру."""
        return self.get_queryset().filter(manager=manager)

    def active_for_manager(self, manager: str):
        """
        Все активные заявки для конкретного менеджера.
        """
        return self.get_queryset().filter(
            status='in_progress',
            manager=manager
        )

    def create_order(self, *, manager, address='', description, cost_price=0, total_price=0):
        """
        Метод для создания заявки.
        Пригодится в DashboardAddOrderView.post()
        """
        order = self.model(
            manager=manager,
            address=address,
            description=description,
            cost_price=cost_price,
            total_price=total_price
        )
        order.save(using=self._db)
        return order