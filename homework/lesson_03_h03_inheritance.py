"""Домашнее задание. Тема 3: наследование и super()."""


class PersonA:
    """Задание 08. super() в переопределённом методе."""
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Меня зовут {self.name}"


class StudentA(PersonA):
    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

    def introduce(self):
        return f"{super().introduce()}, учусь в {self.university}"


class BaseAccount:
    """Задание 09. Сберегательный счёт."""
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount


class SavingsAccount(BaseAccount):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = self._balance * (self.rate / 100)
        self._balance += interest
        return round(self._balance, 2)


class QueueList(list):
    """Задание 10. Очередь на базе встроенного list."""
    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        return self.pop(0)

    def front(self):
        if not self:
            raise IndexError("Очередь пуста")
        return self[0]

    def size(self):
        return len(self)
