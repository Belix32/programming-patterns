"""Домашнее задание. Тема 6: анти-паттерны."""


def statistics():
    """Задание 18. Статистика без классов."""
    data = [1, 2, 3, 4, 5]
    return {
        "mean": sum(data) / len(data),
        "max": max(data),
        "min": min(data)
    }


def ops(operation):
    """Задание 19. Словарь операций."""
    operations = {
        "add": lambda x, y: x + y,
        "sub": lambda x, y: x - y,
        "mul": lambda x, y: x * y,
        "div": lambda x, y: x / y
    }
    op_func = operations.get(operation)
    return op_func(10, 20) if op_func else None


def needs_abstract(cls):
    """Задание 20. Нужен ли абстрактный класс?"""
    from abc import ABC, abstractmethod
    return any(hasattr(method, '__isabstractmethod__') and method.__isabstractmethod__
               for method in cls.__dict__.values())
