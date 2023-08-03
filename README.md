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
git clone git@github.com:DNKer/scrapy_parser_pep.git
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

## Пример работы парсинга
После запуска парсера,
```bash
scrapy crawl pep
```
в консоль будет непосредственно выводится лог процесса. Ниже кусок, для примера:
```bash
{'name': 'Python 2.0 Release Schedule', 'number': '200', 'status': 'Final'}
2023-08-03 09:20:15 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://peps.python.org/pep-0008/> from <GET https://peps.python.org/pep-0008>
2023-08-03 09:20:15 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://peps.python.org/pep-0007/> from <GET https://peps.python.org/pep-0007>
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0102/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0101/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0042/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0103/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.scraper] DEBUG: Scraped from <200 https://peps.python.org/pep-0160/>
{'name': 'Python 1.6 Release Schedule', 'number': '160', 'status': 'Final'}
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0020/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0100/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0013/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0012/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.scraper] DEBUG: Scraped from <200 https://peps.python.org/pep-0102/>
{'name': 'Doing Python Micro Releases', 'number': '102', 'status': 'Superseded'}
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0011/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.scraper] DEBUG: Scraped from <200 https://peps.python.org/pep-0101/>
{'name': 'Doing Python Releases 101', 'number': '101', 'status': 'Active'}
2023-08-03 09:20:15 [scrapy.core.scraper] DEBUG: Scraped from <200 https://peps.python.org/pep-0042/>
{'name': 'Feature Requests', 'number': '42', 'status': 'Withdrawn'}
2023-08-03 09:20:15 [scrapy.core.scraper] DEBUG: Scraped from <200 https://peps.python.org/pep-0103/>
{'name': 'Collecting information about git',
 'number': '103',
 'status': 'Withdrawn'}
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0010/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0009/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://peps.python.org/pep-0007/> (referer: https://peps.python.org/)
2023-08-03 09:20:15 [scrapy.core.scraper] DEBUG: Scraped from <200 https://peps.python.org/pep-0020/>
{'name': 'The Zen of Python', 'number': '20', 'status': 'Active'}
```
***
```bash
{'downloader/request_bytes': 319946,
 'downloader/request_count': 1238,
 'downloader/request_method_count/GET': 1238,
 'downloader/response_bytes': 7243496,
 'downloader/response_count': 1238,
 'downloader/response_status_count/200': 619,
 'downloader/response_status_count/301': 618,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 22.502642,
 'feedexport/success_count/FileFeedStorage': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2023, 8, 3, 4, 20, 15, 595386),
 'httpcompression/response_bytes': 28193206,
 'httpcompression/response_count': 620,
 'item_scraped_count': 618,
 'log_count/DEBUG': 1885,
 'log_count/INFO': 11,
 'request_depth_max': 1,
 'response_received_count': 620,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 0,
 'scheduler/dequeued': 1237,
 'scheduler/dequeued/memory': 1237,
 'scheduler/enqueued': 1237,
 'scheduler/enqueued/memory': 1237,
 'start_time': datetime.datetime(2023, 8, 3, 4, 19, 53, 92744)}
2023-08-03 09:20:15 [scrapy.core.engine] INFO: Spider closed (finished)
```


#### Лицензия
###### Free Software, as Is 
###### _License Free_
###### Author: [Dmitry](https://github.com/DNKer), [Yandex practikum](https://practicum.yandex.ru)
###### 2023