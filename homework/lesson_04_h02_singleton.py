"""Домашнее задание. Тема 2: Singleton."""


class Capital:
    """Задание 05. Синглтон со сменой имени."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = "не установлен"
        return cls._instance

    def rename(self, new_name):
        self.name = new_name


class Fibonacci:
    """Задание 06. Синглтон-генератор чисел Фибоначчи."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_a"):
            self._a, self._b = 0, 1

    def next(self):
        res = self._a
        self._a, self._b = self._b, self._a + self._b
        return res


class God:
    """Задание 07. Синглтон со счётчиком обращений."""
    _instance = None
    _prayers = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pray(self):
        God._prayers += 1

    @classmethod
    def prayers(cls):
        return cls._prayers
