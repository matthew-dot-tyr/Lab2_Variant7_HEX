"""Проверка и поиск HEX-цветов с помощью регулярных выражений."""
import re

HEX_VALIDATION_PATTERN = r"#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?"
HEX_SEARCH_PATTERN = (
    r"(?<![0-9A-Fa-f])"
    r"#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?"
    r"(?![0-9A-Fa-f])"
)
HEX_VALIDATOR = re.compile(HEX_VALIDATION_PATTERN)
HEX_FINDER = re.compile(HEX_SEARCH_PATTERN)

def is_valid_hex_color(value: str) -> bool:
    """Проверяет, что вся строка — HEX-цвет #RGB или #RRGGBB."""
    return HEX_VALIDATOR.fullmatch(value) is not None

def find_hex_colors(text: str) -> list[str]:
    """Находит HEX-цвета в тексте."""
    return HEX_FINDER.findall(text)
