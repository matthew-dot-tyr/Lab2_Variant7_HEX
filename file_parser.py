"""Поиск HEX-цветов в локальных текстовых и HTML-файлах."""
from pathlib import Path
from regex_checker import find_hex_colors

def read_text_file(path: str) -> str:
    """Читает файл в UTF-8, при необходимости пробует Windows-1251."""
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")
    try:
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return file_path.read_text(encoding="cp1251")

def find_colors_in_file(path: str) -> list[str]:
    """Возвращает HEX-цвета, найденные в файле."""
    return find_hex_colors(read_text_file(path))
