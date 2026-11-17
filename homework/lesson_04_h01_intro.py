"""Домашнее задание. Тема 1: введение и мотивация."""


def hw_01(name):
    """Группа паттерна (малый словарь)."""
    patterns = {
        "Singleton": "порождающие",
        "Builder": "порождающие",
        "Prototype": "порождающие",
        "Observer": "поведенческие",
        "Strategy": "поведенческие",
        "Command": "поведенческие",
    }
    return patterns.get(name)


def hw_02():
    """Имена порождающих паттернов."""
    return sorted(["Singleton", "Builder", "Prototype"])


class Ticker:
    """Задание 03. Тикер: текущее и прошлое значение."""
    def __init__(self):
        self._current = None
        self._previous = None

    def tick(self, value):
        self._previous = self._current
        self._current = value

    def current(self):
        return self._current

    def previous(self):
        return self._previous


def hw_04(name):
    """Намерение паттерна по имени."""
    mapping = {
        "Singleton": "единственный экземпляр",
        "Builder": "пошаговая сборка сложного объекта",
        "Observer": "уведомление подписчиков",
    }
    return mapping.get(name)
