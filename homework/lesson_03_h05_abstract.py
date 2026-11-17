"""Домашнее задание. Тема 5: абстрактные классы."""
from abc import ABC, abstractmethod


class SoundSource(ABC):
    """Задание 15. Шаблонный метод на абстрактной базе."""
    @abstractmethod
    def make_sound(self):
        pass

    def speak(self, times=1):
        return ' '.join([self.make_sound() for _ in range(times)])


class DogSound(SoundSource):
    def make_sound(self):
        return "гав"


class Storage(ABC):
    """Задание 16. Интерфейс хранилища."""
    @abstractmethod
    def save(self, key, value):
        pass

    @abstractmethod
    def load(self, key):
        pass


class MemoryStorage(Storage):
    def __init__(self):
        self.data = {}

    def save(self, key, value):
        self.data[key] = value

    def load(self, key):
        return self.data.get(key)


class Sealed:
    """Задание 17. Запрет наследования."""
    def __init_subclass__(cls, **kwargs):
        raise TypeError("Наследование от Sealed запрещено")
