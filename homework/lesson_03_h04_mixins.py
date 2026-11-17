"""Домашнее задание. Тема 4: миксины и MRO."""


class DescribeMixin:
    """Задание 11. Строковое описание объекта."""
    def describe(self):
        attrs = []
        for name, value in self.__dict__.items():
            attrs.append(f"{name}={value}")
        return f"{type(self).__name__}: {', '.join(attrs)}"


class EqMixin:
    """Задание 12. Сравнение по полям."""
    def fields(self):
        raise NotImplementedError("Носитель миксина должен реализовать fields()")

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        my_fields = self.fields()
        other_fields = other.fields()
        if len(my_fields) != len(other_fields):
            return False
        for i in range(len(my_fields)):
            if getattr(self, my_fields[i]) != getattr(other, other_fields[i]):
                return False
        return True


class Book(EqMixin):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def fields(self):
        return ("title", "author")


class P:
    """Задание 13. Ромб MRO: S→Q→R→P."""
    def who(self):
        return "P"


class Q(P):
    def who(self):
        return f"Q->{super().who()}"


class R(P):
    def who(self):
        return f"R->{super().who()}"


class S(Q, R):
    def who(self):
        return f"S->{super().who()}"


class StatsMixin:
    """Задание 14. Ленивое состояние в миксине."""
    def remember(self, value):
        if not hasattr(self, '_log'):
            self._log = []
        self._log.append(value)

    def average(self):
        if not hasattr(self, '_log') or not self._log:
            return 0.0
        return sum(self._log) / len(self._log)
