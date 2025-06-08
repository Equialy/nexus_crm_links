from django.contrib import admin

from clients.models import Clients


# Register your models here.
@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', "name" , "phone" , "phone_2" , "telegram" , "email" , "manager")
    search_fields = ('name', "telegram")
    list_per_page = 20
    ordering = ('name',)
    fields = ('name', "phone" , "phone_2" , "telegram" , "email" , "manager") # Для добавления через admin
    save_on_top = True
    # Чтобы быстро добавлять новые услуги прямо через админку
    add_fieldsets = (
        (None, {
            'fields': ('name', "telegram")
        }),
    )
