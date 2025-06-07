```commandline
my_crm/
├── .venv/                # Виртуальное окружение (uv)
├── src/                  # Исходный код
│   ├── crm/              # Приложение CRM
│   │   ├── models.py
│   │   ├── views.py
│   │   └── ...
├── core/                 # Настройки Django
│   ├── settings.py
│   ├── celery.py
│   └── ...
├── pyproject.toml        # Конфигурация и зависимости
└── requirements.txt      # Автогенерируемый
```