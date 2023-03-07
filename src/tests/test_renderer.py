"""
Тестирование функций генерации выходного файла.
"""
from pathlib import Path

import pytest

from renderer import Renderer, APARenderer


class TestRenderer:
    """
    Тестирование функций генерации выходного файла.
    """

    @pytest.fixture
    def formatted_models(self) -> tuple[str, ...]:
        """
         Получение объекта тестовой рабочей книги.
        :return:
        """

        return (
            "Строка №1",
            "Строка №2",
            "Строка №3",
        )

    def test_render(self, tmp_path: Path, formatted_models: tuple[str, ...]) -> None:
        """
        Тестирование функции генерации выходного файла.

        :param Path tmp_path: Фикстура пути для временного хранения файла во время тестирования
        :param tuple[str, ...] formatted_models: Список строк для сохранения в файле
        """

        path = tmp_path / "output.docx"
        Renderer(formatted_models).render(path)

        # проверка наличия файла
        assert len(list(tmp_path.iterdir())) == 1
        # проверка размера файла в байтах на диске
        assert path.stat().st_size == 36773

class TestAPARenderer:
    """
    Тестирование функций генерации выходного файла.
    """

    @pytest.fixture
    def formatted_models(self) -> tuple[str, ...]:
        """
         Получение объекта тестовой рабочей книги.
        :return:
        """

        return (
            "Строка №1",
            "Строка №2",
            "Строка №3",
        )

    def test_render(self, tmp_path: Path, formatted_models: tuple[str, ...]) -> None:
        """
        Тестирование функции генерации выходного файла.
        :param Path tmp_path: Фикстура пути для временного хранения файла во время тестирования
        :param tuple[str, ...] formatted_models: Список строк для сохранения в файле
        """

        path = tmp_path / "output.docx"
        APARenderer(formatted_models).render(path)

        # проверка наличия файла
        assert len(list(tmp_path.iterdir())) == 1
        # проверка размера файла в байтах на диске
        assert path.stat().st_size == 36765
