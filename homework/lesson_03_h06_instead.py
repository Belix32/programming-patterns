"""Домашнее задание. Тема 6: композиция вместо наследования."""
from abc import ABC, abstractmethod


class TextTransformer:
    """Задание 18. Цепочка правил."""
    def __init__(self, rules):
        self.rules = rules

    def apply(self, text):
        result = text
        for rule in self.rules:
            result = rule(result)
        return result


class PaymentMethod(ABC):
    """Задание 19. Методы оплаты: стратегии."""
    @abstractmethod
    def pay(self, amount):
        pass


class CardMethod(PaymentMethod):
    def pay(self, amount):
        return f"оплачено картой {amount}"


class CashMethod(PaymentMethod):
    def pay(self, amount):
        return f"оплачено наличными {amount}"


class Checkout:
    def __init__(self, method):
        self.method = method

    def pay(self, amount):
        return self.method.pay(amount)


class Sword:
    """Задание 20. Персонаж со сменным оружием."""
    def attack(self):
        return "удар мечом"


class Bow:
    def attack(self):
        return "выстрел из лука"


class Character:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def set_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        return f"{self.name}: {self.weapon.attack()}"
