import csv
from datetime import datetime
from typing import Any

from pep_parse.exceptions import (
    ParserFileOutputError
)
from pep_parse.settings import (
    BASE_DIR,
    DIALECT,
    ENCODING,
    TIME_FORMAT,
    RESULT_DIR,
    FILE_FORMAT
)


class PepParsePipeline:
    """Обрабатывает полученные и переданные
    в Items данные со страницы."""

    def open_spider(self, spider) -> None:
        # Создание объекта статусов PEP.
        self.pep_statuses = {}
        self.total = 0

    def process_item(self, item, spider) -> Any:
        # Подсчет статусов PEP.
        if item['status'] not in self.pep_statuses:
            self.pep_statuses[item['status']] = 1
        else:
            self.pep_statuses[item['status']] += 1
        self.total += 1
        return item

    def close_spider(self, spider) -> None:
        # Запись результата подсчета в файл csv.
        now = datetime.now()
        now_formatted = now.strftime(TIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.{FILE_FORMAT}'
        file_path = BASE_DIR / RESULT_DIR / file_name
        try:
            with open(file_path, 'w', encoding=ENCODING) as file:
                writer = csv.writer(file, dialect=DIALECT)
                writer.writerow(('Статус', 'Количество'))
                writer.writerows(self.pep_statuses.items())
                writer.writerow(('Total', self.total))
        except Exception as error:
            raise ParserFileOutputError(
                f'В процессе работы с файлом возникла ошибка: {error}'
            )
