from pathlib import Path
from typing import Dict


BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
# Obey robots.txt rules
ROBOTSTXT_OBEY: bool = True
# Configure item pipelines
ITEM_PIPELINES: Dict[str, int] = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
BASE_DIR = Path(__file__).parent.parent
NAME_SPIDER: str = 'pep'
RESULT_DIR: str = 'results'
FILE_FORMAT: str = 'csv'
ALLOWED_DOMAINS: str = 'peps.python.org'
# PEP_NAME_PATTERN - шаблон для поиска версии и статуса.
# \d - соответствует цифре (эквивалентно [0-9])
# + 1 или больше повторений предшествующего символа
# . соответствует любому символу (за исключением символа конца строки)
# * 0 или больше повторений предшествующего символа
# pep_number - номер версии
# pep_name - название PEP
PEP_NAME_PATTERN: str = r'PEP (?P<pep_number>\d+) – (?P<pep_name>.*)'
DIALECT: str = 'unix'
ENCODING: str = 'utf-8'
TIME_FORMAT: str = '%Y-%m-%dT%H-%M-%S'
FEEDS = {
    f'results/pep_%(time)s.{FILE_FORMAT}': {
        'format': FILE_FORMAT,
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}
