from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from nexus_crm import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("users.urls", namespace="users")),
    path('crm/', include("orders.urls", namespace="orders")),
    path('crm/', include("clients.urls", namespace="clients")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)