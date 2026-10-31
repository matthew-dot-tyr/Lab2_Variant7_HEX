"""Загрузка веб-страниц и поиск HEX-цветов в HTML."""
import requests
from regex_checker import find_hex_colors

DEFAULT_TIMEOUT = 10

def get_page_text(url: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Загружает страницу по HTTP/HTTPS и возвращает её HTML."""
    normalized_url = url.strip()
    if not normalized_url.startswith(("http://", "https://")):
        raise ValueError("URL должен начинаться с http:// или https://")
    response = requests.get(
        normalized_url, timeout=timeout,
        headers={"User-Agent": "Lab2-HEX-Regex/1.0"}
    )
    response.raise_for_status()
    return response.text

def find_colors_on_page(url: str) -> list[str]:
    """Загружает страницу и ищет в её HTML HEX-цвета."""
    return find_hex_colors(get_page_text(url))
