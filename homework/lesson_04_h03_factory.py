"""Домашнее задание. Тема 3: Factory Method."""


def create_connection(db_type):
    """Задание 08. Фабрика соединений."""
    connections = {
        "postgresql": {"host": "localhost", "port": 5432},
        "mysql": {"host": "localhost", "port": 3306},
        "sqlite": {"path": ":memory:"}
    }
    return connections.get(db_type)


class AnimalFactory:
    """Задание 09. Фабрика животных."""
    @classmethod
    def create_animal(cls, animal_type):
        animals = {
            "cat": Cat(name="Мурка"),
            "dog": Dog(name="Рекс"),
            "bird": Bird(name="Кеша")
        }
        return animals.get(animal_type)


class Cat:
    def __init__(self, name):
        self.name = name


class Dog:
    def __init__(self, name):
        self.name = name


class Bird:
    def __init__(self, name):
        self.name = name


def create_report(report_type):
    """Задание 10. Фабрика отчётов."""
    reports = {
        "html": {"format": "html", "extension": ".html"},
        "pdf": {"format": "pdf", "extension": ".pdf"},
        "json": {"format": "json", "extension": ".json"}
    }
    return reports.get(report_type)
