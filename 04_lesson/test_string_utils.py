"""
Тесты для класса StringUtils
Для запуска тестов установите pytest: pip install pytest
Запуск: pytest test_string_utils.py
"""

import pytest
from string_utils import StringUtils


class TestStringUtils:
    """Тесты для класса StringUtils"""

    @pytest.fixture
    def util(self):
        """Фикстура для создания экземпляра StringUtils"""
        return StringUtils()

    # Тесты для метода capitalize
    def test_capitalize_positive(self, util):
        """Позитивные тесты для capitalize"""
        assert util.capitalize("skypro") == "Skypro"
        assert util.capitalize("hello world") == "Hello world"
        assert util.capitalize("python") == "Python"
        assert util.capitalize("a") == "A"

    def test_capitalize_empty_string(self, util):
        """Тест capitalize с пустой строкой"""
        assert util.capitalize("") == ""

    def test_capitalize_already_capitalized(self, util):
        """Тест capitalize с уже заглавной первой буквой"""
        assert util.capitalize("Skypro") == "Skypro"
        assert util.capitalize("TEST") == "Test"

    @pytest.mark.parametrize("input_str, expected", [
        ("123abc", "123abc"),
        (" abc", " abc"),
        ("1test", "1test"),
    ])
    def test_capitalize_edge_cases(self, util, input_str, expected):
        """Параметризованные тесты для пограничных случаев"""
        assert util.capitalize(input_str) == expected

    # Тесты для метода trim
    def test_trim_positive(self, util):
        """Позитивные тесты для trim"""
        assert util.trim("   skypro") == "skypro"
        assert util.trim("  hello  ") == "hello  "
        assert util.trim(" test") == "test"
        assert util.trim("    multiple    spaces") == "multiple    spaces"

    def test_trim_no_spaces(self, util):
        """Тест trim без начальных пробелов"""
        assert util.trim("skypro") == "skypro"
        assert util.trim("test  ") == "test  "

    def test_trim_empty_string(self, util):
        """Тест trim с пустой строкой"""
        assert util.trim("") == ""
        assert util.trim("   ") == ""

    @pytest.mark.parametrize("input_str, expected", [
        ("\ttext", "\ttext"),  # табуляция не удаляется
        ("\ntext", "\ntext"),  # перевод строки не удаляется
        ("  \n  text", "\n  text"),  # пробелы удаляются, перенос строки остается
    ])
    def test_trim_only_spaces(self, util, input_str, expected):
        """Тест trim только с пробелами (не другими whitespace символами)"""
        assert util.trim(input_str) == expected

    # Тесты для метода contains
    def test_contains_positive(self, util):
        """Позитивные тесты для contains"""
        assert util.contains("SkyPro", "S") is True
        assert util.contains("SkyPro", "k") is True
        assert util.contains("SkyPro", "Pro") is True
        assert util.contains("Hello World", " ") is True

    def test_contains_negative(self, util):
        """Негативные тесты для contains"""
        assert util.contains("SkyPro", "U") is False
        assert util.contains("", "a") is False
        assert util.contains("test", "TEST") is False

    def test_contains_empty_string(self, util):
        """Тест contains с пустой строкой или символом"""
        # ВАЖНО: метод contains возвращает True для ("", "")
        # потому что string.index("") возвращает 0
        assert util.contains("", "") is True  # ИЗМЕНИЛОСЬ!
        assert util.contains("test", "") is True  # ИЗМЕНИЛОСЬ!

    @pytest.mark.parametrize("string, symbol, expected", [
        ("hello", "h", True),
        ("hello", "H", False),  # регистр имеет значение
        ("12345", "3", True),
        ("", "x", False),
        ("test", "", True),  # ИЗМЕНИЛОСЬ!
        ("", "", True),  # ИЗМЕНИЛОСЬ!
    ])
    def test_contains_parametrized(self, util, string, symbol, expected):
        """Параметризованные тесты для contains"""
        assert util.contains(string, symbol) == expected

    # Тесты для метода delete_symbol
    def test_delete_symbol_positive(self, util):
        """Позитивные тесты для delete_symbol"""
        assert util.delete_symbol("SkyPro", "k") == "SyPro"
        assert util.delete_symbol("SkyPro", "Pro") == "Sky"
        assert util.delete_symbol("hello world", " ") == "helloworld"
        assert util.delete_symbol("banana", "na") == "ba"

    def test_delete_symbol_no_match(self, util):
        """Тест delete_symbol без совпадений"""
        assert util.delete_symbol("SkyPro", "X") == "SkyPro"
        assert util.delete_symbol("test", "123") == "test"

    def test_delete_symbol_all_occurrences(self, util):
        """Тест delete_symbol удаляет все вхождения"""
        assert util.delete_symbol("aaaa", "a") == ""
        assert util.delete_symbol("ababab", "ab") == ""
        assert util.delete_symbol("testtest", "t") == "eses"

    def test_delete_symbol_empty_input(self, util):
        """Тест delete_symbol с пустыми входными данными"""
        assert util.delete_symbol("", "a") == ""
        assert util.delete_symbol("test", "") == "test"
        assert util.delete_symbol("", "") == ""

    @pytest.mark.parametrize("string, symbol, expected", [
        ("hello", "l", "heo"),
        ("mississippi", "iss", "mippi"),
        ("123.456.789", ".", "123456789"),
        ("same", "same", ""),
    ])
    def test_delete_symbol_parametrized(self, util, string, symbol, expected):
        """Параметризованные тесты для delete_symbol"""
        assert util.delete_symbol(string, symbol) == expected

    # Тесты для метода starts_with
    def test_starts_with_positive(self, util):
        """Позитивные тесты для starts_with"""
        assert util.starts_with("SkyPro", "S") is True
        assert util.starts_with("hello", "h") is True
        assert util.starts_with("123abc", "1") is True
        assert util.starts_with(" test", " ") is True

    def test_starts_with_negative(self, util):
        """Негативные тесты для starts_with"""
        assert util.starts_with("SkyPro", "P") is False
        assert util.starts_with("hello", "H") is False  # регистр имеет значение
        assert util.starts_with("", "a") is False
        assert util.starts_with("test", "est") is False  # только первый символ
        assert util.starts_with("test", "") is False  # пустой символ
        assert util.starts_with("", "") is False  # обе строки пустые

    @pytest.mark.parametrize("string, symbol, expected", [
        ("apple", "a", True),
        ("Apple", "a", False),
        ("", "x", False),
        ("multi char", "m", True),
        ("123", "1", True),
        ("  space", " ", True),
        ("test", "", False),  # пустой символ
        ("", "", False),  # обе строки пустые
    ])
    def test_starts_with_parametrized(self, util, string, symbol, expected):
        """Параметризованные тесты для starts_with"""
        assert util.starts_with(string, symbol) == expected

    # Тесты для метода end_with
    def test_end_with_positive(self, util):
        """Позитивные тесты для end_with"""
        assert util.end_with("SkyPro", "o") is True
        assert util.end_with("hello", "o") is True
        assert util.end_with("test123", "3") is True
        assert util.end_with("end ", " ") is True

    def test_end_with_negative(self, util):
        """Негативные тесты для end_with"""
        assert util.end_with("SkyPro", "y") is False
        assert util.end_with("hello", "O") is False  # регистр имеет значение
        assert util.end_with("", "a") is False
        assert util.end_with("test", "tes") is False  # только последний символ
        assert util.end_with("test", "") is False  # пустой символ
        assert util.end_with("", "") is False  # обе строки пустые

    @pytest.mark.parametrize("string, symbol, expected", [
        ("apple", "e", True),
        ("Apple", "E", False),
        ("", "x", False),
        ("multi char", "r", True),
        ("123", "3", True),
        ("space ", " ", True),
        ("test", "", False),  # пустой символ
        ("", "", False),  # обе строки пустые
    ])
    def test_end_with_parametrized(self, util, string, symbol, expected):
        """Параметризованные тесты для end_with"""
        assert util.end_with(string, symbol) == expected

    # Тесты для метода is_empty
    def test_is_empty_positive(self, util):
        """Позитивные тесты для is_empty"""
        assert util.is_empty("") is True
        assert util.is_empty(" ") is True
        assert util.is_empty("   ") is True
        assert util.is_empty("  \t\n  ") is False  # только пробелы удаляются, табуляция и перевод строки остаются

    def test_is_empty_negative(self, util):
        """Негативные тесты для is_empty"""
        assert util.is_empty("SkyPro") is False
        assert util.is_empty("  a") is False
        assert util.is_empty("test  ") is False  # пробелы в конце не удаляются

    @pytest.mark.parametrize("string, expected", [
        ("", True),
        (" ", True),
        ("  ", True),
        ("a", False),
        (" a", False),
        ("  test", False),
        ("\t", False),  # табуляция не считается пробелом для trim
        ("\n", False),  # перевод строки не считается пробелом
        ("\t\n", False),  # комбинация
    ])
    def test_is_empty_parametrized(self, util, string, expected):
        """Параметризованные тесты для is_empty"""
        assert util.is_empty(string) == expected

    # Тесты для метода list_to_string
    def test_list_to_string_positive(self, util):
        """Позитивные тесты для list_to_string"""
        assert util.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
        assert util.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
        assert util.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
        assert util.list_to_string(["a", "b", "c"], "") == "abc"

    def test_list_to_string_empty_list(self, util):
        """Тест list_to_string с пустым списком"""
        assert util.list_to_string([]) == ""
        assert util.list_to_string([], "-") == ""

    def test_list_to_string_single_element(self, util):
        """Тест list_to_string с одним элементом"""
        assert util.list_to_string(["single"]) == "single"
        assert util.list_to_string([42]) == "42"
        assert util.list_to_string(["test"], "---") == "test"  # разделитель не используется

    def test_list_to_string_mixed_types(self, util):
        """Тест list_to_string с разными типами данных"""
        assert util.list_to_string([1, "two", 3.0, True]) == "1, two, 3.0, True"

    @pytest.mark.parametrize("lst, joiner, expected", [
        ([1, 2, 3], ", ", "1, 2, 3"),
        (["a", "b"], "-", "a-b"),
        (["hello"], " ", "hello"),
        ([], ", ", ""),
        ([True, False], " and ", "True and False"),
    ])
    def test_list_to_string_parametrized(self, util, lst, joiner, expected):
        """Параметризованные тесты для list_to_string"""
        assert util.list_to_string(lst, joiner) == expected

    # Интеграционные тесты (проверка взаимодействия методов)
    def test_integration_trim_and_capitalize(self, util):
        """Интеграционный тест: trim + capitalize"""
        result = util.capitalize(util.trim("   hello world"))
        assert result == "Hello world"

    def test_integration_contains_and_delete(self, util):
        """Интеграционный тест: contains + delete_symbol"""
        text = "Hello World"
        if util.contains(text, "World"):
            result = util.delete_symbol(text, "World")
            assert result == "Hello "

    # Тесты на обработку исключений
    def test_methods_with_none(self, util):
        """Тест методов с None вместо строки"""
        # Проверяем, что методы падают с AttributeError при передаче None
        with pytest.raises(AttributeError):
            util.capitalize(None)
        
        with pytest.raises(AttributeError):
            util.trim(None)
        
        with pytest.raises(AttributeError):
            util.contains(None, "a")

    # Дополнительные тесты на граничные случаи
    def test_unicode_characters(self, util):
        """Тест с Unicode символами"""
        assert util.capitalize("привет") == "Привет"
        assert util.contains("café", "é") is True
        assert util.delete_symbol("👋🌍", "🌍") == "👋"
        assert util.list_to_string(["🍎", "🍌", "🍒"], " → ") == "🍎 → 🍌 → 🍒"


if __name__ == "__main__":
    # Можно запускать тесты без pytest: python test_string_utils.py
    pytest.main(["-v", "test_string_utils.py"])



