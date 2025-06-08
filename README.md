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