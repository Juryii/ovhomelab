# ovhomelab
django site for ov calculator

планируемая структура проекта
ovhomelab/
├── ovhomelab/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── project/
│   ├── models.py          # Модели для создания и управления проектом
│   ├── views.py
│   ├── urls.py
│   └── ...
├── building/
│   ├── models.py          # Модели для создания зданий
│   ├── views.py
│   ├── urls.py
│   └── ...
├── heating_library/      # Приложение библиотека для элементов раздела отопление от производителей
│   ├── models.py          # Модели элементов библиотеки
│   ├── views.py
│   ├── urls.py
│   └── ...
├── heating/               # Приложение  раздел отопление
│   ├── models.py          # Модели отопления
│   ├── views.py
│   ├── urls.py
│   └── ...
├── ventilation_library/   # Приложение библиотека для элементов раздела вентиляции от производителей
│   ├── models.py          # Модели элементов библиотеки
│   ├── views.py
│   ├── urls.py
│   └── ...
├── ventilation/           # Приложение  раздел вентиляция
│   ├── models.py          # Модели вентиляции
│   ├── views.py
│   ├── urls.py
│   └── ...
├── heat_networks_library/      # Приложение библиотека для элементов раздела тепловые сети от производителей
│   ├── models.py               # Модели элементов библиотеки
│   ├── views.py
│   ├── urls.py
│   └── ...
├── heat_networks/           # Приложение  раздел тепловые сети
│   ├── models.py            # Модели тепловых сетей
│   ├── views.py
│   ├── urls.py
│   └── ...
└── insulation/             # Приложение для управления изоляцией трубопроводов
    ├── models.py
    ├── views.py
    ├── urls.py
    └── ...

проект ТС1 ТС2 ТС3
