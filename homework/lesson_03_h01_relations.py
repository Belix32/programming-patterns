"""Домашнее задание. Тема 1: инкапсуляция и отношения."""


class Safe:
    """Задание 01. Сейф: приватность и счётчик попыток."""
    def __init__(self, code):
        self.__code = code
        self._attempts = 0

    def open(self, code):
        if code == self.__code:
            return "открыто"
        self._attempts += 1
        raise ValueError("неверный код")

    @property
    def attempts(self):
        return self._attempts


class Config:
    """Задание 02. Настройки только для чтения."""
    def __init__(self, **settings):
        self._settings = dict(settings)

    @property
    def settings(self):
        return dict(self._settings)

    def update(self, key, value):
        self._settings[key] = value

    def get(self, key, default=None):
        return self._settings.get(key, default)


class Player:
    """Задание 03, часть 1. Игрок."""
    def __init__(self, name):
        self.name = name


class Team:
    """Задание 03, часть 2. Агрегация: команда из игроков."""
    def __init__(self, name):
        self.name = name
        self._players = []

    def add(self, player):
        self._players.append(player)

    def roster(self):
        return [player.name for player in self._players]


class Course:
    """Задание 04. Ассоциация: курс и студенты."""
    def __init__(self, title):
        self.title = title
        self._students = []

    def enroll(self, student):
        self._students.append(student)

    def students(self):
        return [student.name for student in self._students]


class Student:
    """Студент (для задания 04)."""
    def __init__(self, name):
        self.name = name
