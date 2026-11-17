"""Домашнее задание. Тема 5: порождающие вместе."""


class Settings:
    """Задание 15. Синглтон с настройками по умолчанию."""
    _instance = None

    def __new__(cls, **settings):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, **settings):
        if not hasattr(self, '_settings'):
            self._settings = settings

    @property
    def settings(self):
        return self._settings.copy()


def create_counting(func):
    """Задание 16. Фабрика считающих обёрток."""
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        return f"{result}: {count}"

    return wrapper


class Cache:
    """Задание 17. Синглтон-кэш."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._cache = {}
        return cls._instance

    def get(self, key):
        return self._cache.get(key)

    def set(self, key, value):
        self._cache[key] = value
