from django.contrib import admin

from orders.models import Orders


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    # Поля, которые будут видны в списке заявок
    list_display = (
        'id',
        'service',
        'manager',
        'status',
        'cost_price',
        'total_price',
        'created_at',
    )
    # Фильтры сбоку
    list_filter = ('status', 'created_at', 'manager', 'service')
    # Поиск по текстовым полям и связанным объектам
    search_fields = (
        'description',
        'service__name',  # если модель Service имеет поле name
        'manager__email',
    )
    # Поля, доступные при редактировании одной записи
    fieldsets = (
        (None, {
            'fields': ( 'service', 'description', 'status')
        }),
        ('Адрес и цены', {
            'fields': ('address', 'cost_price', 'total_price'),
        }),
        ('Управление', {
            'fields': ('manager',),
        }),
    )
    # Делаем даты нередактируемыми
    readonly_fields = ('created_at', 'updated_at')
    # Автоматически сохранять поле manager при создании через админку (опционально)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.manager = request.user
        super().save_model(request, obj, form, change)

from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 20
    ordering = ('title',)
    fields = ('title',)
    save_on_top = True
    # Чтобы быстро добавлять новые услуги прямо через админку
    add_fieldsets = (
        (None, {
            'fields': ('title',)
        }),
    )
