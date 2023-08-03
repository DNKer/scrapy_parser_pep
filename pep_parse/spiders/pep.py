import re
from typing import Any, Dict, List

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import (
    ALLOWED_DOMAINS,
    NAME_SPIDER,
    PEP_NAME_PATTERN,
    START_URLS
)


class PepSpider(scrapy.Spider):
    """Собирает данные о PEP."""

    name: str = NAME_SPIDER
    allowed_domains: List[str] = [ALLOWED_DOMAINS, ]
    start_urls: List[str] = START_URLS

    def parse(self, response) -> Dict[str, Any]:
        # Собирает ссылки на документы из таблицы Numerical Index.
        urls_list = response.css(
            'section#numerical-index').css('tbody').css('tr')
        for item in urls_list:
            href = item.css('a::attr(href)').get()
            if href is not None:
                yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response) -> Any:
        # Собирает страницы с документами и формирует Items.
        full_name = response.css('h1.page-title::text').get()
        pep_name_match = re.search(PEP_NAME_PATTERN, full_name)
        number, name = pep_name_match.groups()
        status = (
            response.css('dt:contains("Status:") + dd').css("abbr::text").get()
        )
        data: Dict[str, Any] = {'number': number,
                                'name': name,
                                'status': status}
        yield PepParseItem(data)
