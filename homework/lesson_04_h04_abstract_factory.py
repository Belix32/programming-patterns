"""Домашнее задание. Тема 4: Abstract Factory."""


class LightTheme:
    """Задание 11. Светлая тема страницы."""
    def background(self):
        return "white"

    def text(self):
        return "black"


class DarkTheme:
    """Задание 11. Тёмная тема страницы."""
    def background(self):
        return "black"

    def text(self):
        return "white"


def render_page(theme):
    """Задание 12. Клиентский код без знания семейства."""
    return {"background": theme.background(), "text": theme.text()}


def get_ui_factory(platform):
    """Задание 13. Фабрика фабрик."""
    factories = {
        "mobile": MobileFactory,
        "desktop": DesktopFactory
    }
    factory_class = factories.get(platform)
    return factory_class() if factory_class else None


class MobileFactory:
    def create_button(self):
        return "MobileButton"

    def create_textbox(self):
        return "MobileTextbox"


class DesktopFactory:
    def create_button(self):
        return "DesktopButton"

    def create_textbox(self):
        return "DesktopTextbox"


def same_family(factory1, factory2):
    """Задание 14. Проверка согласованности семейства."""
    return type(factory1) == type(factory2)
