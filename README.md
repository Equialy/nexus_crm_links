# Nexus CRM

CRM-система для управления заявками, клиентами и задачами, построенная на Django 4.2 и Bootstrap 5.

---

##  Основные возможности

- **Панель заявок**  
  Просмотр списка активных заявок с фильтрацией по менеджеру, статусу и дате.

- **Создание и редактирование заявки**  
  – Форма добавления новой заявки (клиент, услуга, описание, адрес)  
  – Редактирование любых полей заявки на отдельной странице или через модальные окна с AJAX

- **Изменение адреса через AJAX-модалку**  
  Быстрое редактирование поля «Адрес» без перезагрузки страницы.

- **Загрузка и управление файлами заявки**  
  – Загрузка любых документов в папку `media/order_files/`  
  – Список прикреплённых файлов с возможностью скачивания и удаления

- **Управление задачами**  
  Просмотр, создание и статус-менеджмент задач, привязанных к заявкам.

- **Сервисы и клиенты**  
  Справочники услуг и клиентов с возможностью добавления через AJAX-модалки

- **Аутентификация и авторизация**  
  Регистрация, вход/выход и разграничение доступа по менеджерам.

- **Адаптивный дизайн**  
  Bootstrap 5, градиентный фон, карточки с эффектом размытия и полупрозрачные модалки.

---

## 📦 Установка

1. **Клонировать репозиторий**
   ```bash
   git clone https://repo....
   cd nexus-crm

## Установка и настройка проекта

### Крок 1: Создать и активировать виртуальное окружение

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Крок 2: Установить зависимости

```bash
pip install -r requirements.txt
```

### Крок 3: Настроить переменные окружения

Создайте файл `.env` рядом с `manage.py` и укажите:

```ini
DEBUG=True
SECRET_KEY=ваш_секретный_ключ
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

### Крок 4: Выполнить миграции и собрать статику

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### Крок 5: Создать супер-пользователя (для доступа к админке)

```bash
python manage.py createsuperuser
```

### Крок 6: Запустить сервер разработки

```bash
python manage.py runserver
```

Перейдите на [http://127.0.0.1:8000/](http://127.0.0.1:8000/), чтобы увидеть приложение.

---

## ⚙️ Конфигурация

### Статические файлы

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
```

### Медиа-файлы

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
```

### URL-раздача медиа (в режиме DEBUG)

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ваши маршруты
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


```commandline
my_crm/
├── .venv/                # Виртуальное окружение (uv)
├── nexus_crm/                  # Исходный код
│   ├── crm/              # Приложение CRM
│   │   ├── models.py
│   │   ├── views.py
│   │   └── ...
│   ├── nexus_crm/             # Настройки Django
│   │   ├── settings.py
│   │   ├── celery.py
│   │   └── ...
│   │ 
│   ├── orders/                # Настройки Django
│   │   ├── forms.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── manager.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── ...
│   ├── users/                 # Приложение users
│   │   ├── forms.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── manager.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── ...
│   ├── static/                 
│   │   └── crm
│   │         ├── css
│   │         └── js
│   ├── media/                 
│   │   └── order_files
│   │         └── ....
│   ├── users/                 
│   │   ├── forms.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── ...
│   ├── templates/                 # Настройки Django
│   │   ├── base.py
│   │   │      ├── base.html
│   │   │      └── dashboard.html
│   │   ├── includes.py
│   │   │      ├── client_add_form.html.html
│   │   │      ├── navbar.html
│   │   │      ├── service_add_form.html
│   │   │      └── edit_order_address.html
│   │   ├── orders.py
│   │   │      ├── order_blank.html
│   │   │      └── ...
│   │   ├── users.py
│   │   │      ├── login.html
│   │   │      └── ...
│   │   └── ...
│   └── manage.py
│
└── pyproject.toml        # Конфигурация и зависимости
```