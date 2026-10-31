"""Главное меню лабораторной работы №2, вариант 7."""
import requests
from file_parser import find_colors_in_file
from regex_checker import find_hex_colors, is_valid_hex_color
from web_parser import find_colors_on_page

def print_colors(colors: list[str]) -> None:
    """Выводит найденные цвета без повторений."""
    unique = list(dict.fromkeys(colors))
    if not unique:
        print("HEX-цвета не найдены.")
        return
    print(f"Совпадений: {len(colors)}; уникальных цветов: {len(unique)}")
    for color in unique:
        print(f"  {color}")

def main() -> None:
    """Запускает интерактивное меню."""
    while True:
        print("\n=== HEX COLOR REGEX — вариант 7 ===")
        print("1. Проверить цвет")
        print("2. Найти цвета в тексте")
        print("3. Найти цвета в файле")
        print("4. Найти цвета на веб-странице")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()
        try:
            if choice == "1":
                value = input("Введите цвет (#RGB или #RRGGBB): ").strip()
                print("Корректный HEX-цвет." if is_valid_hex_color(value)
                      else "Некорректный HEX-цвет.")
            elif choice == "2":
                print_colors(find_hex_colors(input("Введите текст: ")))
            elif choice == "3":
                print_colors(find_colors_in_file(input("Путь к TXT/HTML-файлу: ").strip()))
            elif choice == "4":
                print_colors(find_colors_on_page(input("URL: ").strip()))
            elif choice == "0":
                print("Завершение программы.")
                break
            else:
                print("Нет такого пункта меню.")
        except (OSError, UnicodeError, ValueError, requests.RequestException) as error:
            print(f"Ошибка: {error}")

if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nРабота программы прервана.")
