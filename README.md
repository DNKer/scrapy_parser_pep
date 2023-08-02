# Асинхронный парсер PEP
## Описание
Приложение производит парсинг страницы https://peps.python.org/ на базе фреймворка Scrapy. Сохраняет список документов PEP.
Собирает данные о количестве и статусе документов PEP. Результаты работы сохраняются в CSV-файлы.
## Технологии .
[![Python](https://img.shields.io/badge/-Python-464646?style=plastic&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/) [![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=plastic&logo=GitHub%20actions&logoColor=56C0C0&color=008080)](https://github.com/features/actions)
![Python](https://img.shields.io/badge/python-scrapy-blue)

![workflow](https://github.com/DNKer/scrapy_parser_pep/actions/workflows/scrapy_parser_pep_workflow.yml/badge.svg?branch=master&event=push)

## Установка

> приводятся команды для `Windows`.

Клонировать репозитарий:

```bash
git clone git@github.com:DNKer/bs4_parser_pep.git
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/scripts/activate
```

Обновить систему управления пакетами:

```bash
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Запустить парсер:

```bash
scrapy crawl pep
```

В результате парсинга в директории ```scrapy_parser_pep/results/``` создадутся два файла ```pep_ДатаВремя.csv``` и ```status_summary_ДатаВремя.csv```, например ```pep_2029-01-31T23-55-00.csv``` и ```status_summary_2029-01-31_23-55-00.csv```

<img src="tests\img\IMG_001.PNG" alt="drawing" width="800"/>

В первом файле выведен список всех PEP: номер, название и статус.
Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке этого файла выведено общее количество всех документов - их сумма.

#### Лицензия
###### Free Software, as Is 
###### _License Free_
###### Author: [Dmitry](https://github.com/DNKer), [Yandex practikum](https://practicum.yandex.ru)
###### 2023
