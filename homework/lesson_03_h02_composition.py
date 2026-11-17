"""Домашнее задание. Тема 2: композиция и делегирование."""


class BoatEngine:
    """Задание 05, часть 1. Лодочный двигатель."""
    def __init__(self, hp):
        self.hp = hp

    def start(self):
        return "двигатель заведён"


class Boat:
    """Задание 05, часть 2. Лодка делегирует запуск двигателю."""
    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

    def sail(self):
        return f"{self.name}: {self.engine.start()}"


class Page:
    """Задание 06, часть 1. Страница: заголовок и число слов."""
    def __init__(self, title, words):
        self.title = title
        self.words = words


class Notebook:
    """Задание 06, часть 2. Блокнот из страниц."""
    def __init__(self):
        self._pages = []

    def add_page(self, page):
        self._pages.append(page)

    def total_words(self):
        return sum(page.words for page in self._pages)

    def longest_page(self):
        longest = None
        for page in self._pages:
            if longest is None or page.words > longest.words:
                longest = page
        return longest.title if longest else None


class Greeter:
    """Задание 07. Приветствия с внедрённым логгером."""
    def __init__(self, logger):
        self.logger = logger

    def greet(self, name):
        self.logger.log(f"приветствие: {name}")
        return f"Привет, {name}!"
