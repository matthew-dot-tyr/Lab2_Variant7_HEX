"""Unit-тесты для проверки HEX-регулярного выражения."""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import Mock, patch
import requests
from file_parser import find_colors_in_file
from regex_checker import find_hex_colors, is_valid_hex_color
from web_parser import find_colors_on_page, get_page_text

class TestHexValidation(unittest.TestCase):
    def test_valid_short_colors(self):
        for value in ("#000", "#FFF", "#a1B"):
            with self.subTest(value=value):
                self.assertTrue(is_valid_hex_color(value))

    def test_valid_long_colors(self):
        for value in ("#000000", "#FFFFFF", "#a1B2c3"):
            with self.subTest(value=value):
                self.assertTrue(is_valid_hex_color(value))

    def test_invalid_colors(self):
        values = ("", "000", "#12", "#1234", "#12345", "#1234567",
                  "#GGG", "#12XZ89", "##FFF", " #FFF ")
        for value in values:
            with self.subTest(value=value):
                self.assertFalse(is_valid_hex_color(value))

    def test_search_in_text(self):
        self.assertEqual(
            find_hex_colors("Цвета #fff, #123456, #AbC; ошибки #12 и #GGG"),
            ["#fff", "#123456", "#AbC"]
        )

    def test_no_partial_match_in_long_sequence(self):
        self.assertEqual(find_hex_colors("#12345678 #1234567"), [])

class TestFileParser(unittest.TestCase):
    def test_file_search(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "sample.html"
            path.write_text("<p style='color:#123;background:#ABC'>", encoding="utf-8")
            self.assertEqual(find_colors_in_file(str(path)), ["#123", "#ABC"])

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            find_colors_in_file("missing_hex_lab_file.txt")

class TestWebParser(unittest.TestCase):
    def test_invalid_url_scheme(self):
        with self.assertRaises(ValueError):
            get_page_text("example.com")

    @patch("web_parser.requests.get")
    def test_get_page_text(self, mock_get):
        response = Mock()
        response.text = "<p style='color:#123456'>"
        mock_get.return_value = response
        self.assertEqual(get_page_text("https://example.com"), response.text)
        mock_get.assert_called_once()

    @patch("web_parser.get_page_text")
    def test_find_colors_on_page(self, mock_page):
        mock_page.return_value = "body { color: #fff; background: #010203; }"
        self.assertEqual(find_colors_on_page("https://example.com"),
                         ["#fff", "#010203"])

    @patch("web_parser.requests.get")
    def test_http_error(self, mock_get):
        response = Mock()
        response.raise_for_status.side_effect = requests.HTTPError("404")
        mock_get.return_value = response
        with self.assertRaises(requests.HTTPError):
            get_page_text("https://example.com")

if __name__ == "__main__":
    unittest.main(verbosity=2)
