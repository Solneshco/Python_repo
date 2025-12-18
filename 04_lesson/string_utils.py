"""
Модуль с полезными утилитами для обработки и анализа строк
"""


class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    def capitalize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной
        и возвращает этот же текст
        Пример: `capitilize("skypro") -> "Skypro"`
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть
        Пример: `trim("   skypro") -> "skypro"`
        """
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ
        и `False` - если нет
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ
        Пример 1: `contains("SkyPro", "S") -> True`
        Пример 2: `contains("SkyPro", "U") -> False`
        """
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass

        return res

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ для удаления
        Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
        Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
        """
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string

    def starts_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка начинается с заданного символа
        и `False` - если нет
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ
        Пример 1: `starts_with("SkyPro", "S") -> True`
        Пример 2: `starts_with("SkyPro", "P") -> False`
        """
        if len(string) == 0 or len(symbol) == 0:
            return False
        return string[0] == symbol

    def end_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка заканчивается заданным символом
        и `False` - если нет
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ
        Пример 1: `end_with("SkyPro", "o") -> True`
        Пример 2: `end_with("SkyPro", "y") -> False`
        """
        if len(string) == 0 or len(symbol) == 0:
            return False
        return string[-1] == symbol

    def is_empty(self, string: str) -> bool:
        """
        Возвращает `True`, если строка пустая
        и `False` - если нет
        Пример 1: `is_empty("") -> True`
        Пример 2: `is_empty(" ") -> True`
        Пример 3: `is_empty("SkyPro") -> False`
        """
        trimmed = self.trim(string)
        return trimmed == ""

    def list_to_string(self, lst: list, joiner=", ") -> str:
        """
        Преобразует список элементов в строку
        с указанным разделителем
        Параметры:
            `lst` - список элементов
            `joiner` - разделитель элементов в строке
        Пример 1: `list_to_string([1,2,3,4]) -> "1, 2, 3, 4"`
        Пример 2: `list_to_string(["Sky", "Pro"]) -> "Sky, Pro"`
        Пример 3: `list_to_string(["Sky", "Pro"], "-") -> "Sky-Pro"`
        """
        string = ""
        length = len(lst)

        if length == 0:
            return string

        for i in range(length):
            string += str(lst[i])
            if i != length - 1:
                string += joiner

        return string