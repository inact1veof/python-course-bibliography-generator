"""
Тестирование функций оформления списка источников по APA.
"""

from formatters.base import BaseCitationFormatter
from formatters.models import InternetResourceModel, DissertationModel
from formatters.styles.apa import APAInternetResource, APADissertation


class TestGOST:
    """
    Тестирование оформления списка источников согласно ГОСТ Р 7.0.5-2008.
    """

    def test_internet_resource(self, internet_resource_model_fixture: InternetResourceModel) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = APAInternetResource(internet_resource_model_fixture)

        assert (model.formatted == "Ведомости (01.01.2021) Наука как искусство https://www.vedomosti.ru")

    def test_dissertation(self, dissertation_model_fixture: DissertationModel) -> None:
        """
        Тестирование форматирования диссертации.
        :param DissertationModel dissertation_model_fixture: Фикстура модели диссертации
        :return:
        """

        model = APADissertation(dissertation_model_fixture)

        assert (model.formatted == "Иванов И.М. (2020) Наука как искусство, дис. [д-р. / канд. экон. 01.01.01] СПб., 999 p.")

    def test_citation_formatter(
            self,
            internet_resource_model_fixture: InternetResourceModel,
            dissertation_model_fixture: DissertationModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param DissertationModel dissertation_model_fixture: Фикстура модели диссертации
        :return:
        """

        models = [
            APAInternetResource(internet_resource_model_fixture),
            APADissertation(dissertation_model_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[0]
        assert result[1] == models[1]
