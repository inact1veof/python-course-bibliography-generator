"""
Стиль цитирования APA.
"""
from string import Template

from pydantic import BaseModel

from formatters.models import InternetResourceModel, DissertationModel
from formatters.styles.base import BaseCitationStyle
from logger import get_logger

logger = get_logger(__name__)


class APAInternetResource(BaseCitationStyle):
    """
    Форматирование для интернет-ресурсов.
    """

    data: InternetResourceModel

    @property
    def template(self) -> Template:
        return Template("$website ($access_date) $article $link")

    def substitute(self) -> str:
        logger.info('Форматирование интернет-ресурса "%s" ...', self.data.article)

        return self.template.substitute(
            article=self.data.article,
            website=self.data.website,
            link=self.data.link,
            access_date=self.data.access_date,
        )


class APADissertaion(BaseCitationStyle):
    """
    Форматирование для диссертации.
    """

    data: DissertationModel

    @property
    def template(self) -> Template:
        return Template(
            "$author ($year) $title, дис. [$degree $field $code] $city, $pages p."
        )

    def substitute(self) -> str:
        logger.info('Форматирование диссертации "%s" ...', self.data.title)

        return self.template.substitute(
            author=self.data.author,
            title=self.data.title,
            degree=self.data.degree,
            field=self.data.field,
            code=self.data.code,
            city=self.data.city,
            year=self.data.year,
            pages=self.data.pages,
        )


class APACitationFormatter:
    """
    Базовый класс для итогового форматирования списка источников.
    """

    formatters_map = {
        DissertationModel.__name__: APADissertaion,
        InternetResourceModel.__name__: APAInternetResource,
    }

    def __init__(self, models: list[BaseModel]) -> None:
        """
        Конструктор.
        :param models: Список объектов для форматирования
        """

        formatted_items = []
        for model in models:
            formatted_items.append(self.formatters_map.get(type(model).__name__)(model))

        self.formatted_items = formatted_items

    def format(self) -> list[BaseCitationStyle]:
        """
        Форматирование списка источников.
        :return:
        """

        return sorted(self.formatted_items, key=lambda item: item.formatted)
