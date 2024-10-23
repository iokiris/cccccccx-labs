from abc import ABC, abstractmethod


class Singleton:
    _instance = None

    def __new__(cls, name=None):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.name = name
        return cls._instance

    def show(self):
        return f"[Singleton]: Имя: {self.name}, id: {id(self)}"


singleton1 = Singleton("Первый экземпляр")
singleton2 = Singleton("Второй экземпляр")

print("Вызов 1 - ", singleton1.show())
print("Вызов 2 - ", singleton2.show())

#
#
# ВЫВОД
# Вызов 1 -  [Singleton]: Имя: Первый экземпляр, id: 134768347986336
# Вызов 2 -  [Singleton]: Имя: Первый экземпляр, id: 134768347986336
#
#


class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


class FileLogger(Logger):
    def log(self, message: str):
        print(f"Logging to file: {message}")


class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"Logging to console: {message}")


class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

    def log_message(self, message: str):
        logger = self.create_logger()
        logger.log(message)


class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()


class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()


if input("1. file\n2. console\nEnter logger type: ") == "1":
    factory = FileLoggerFactory()
else:
    factory = ConsoleLoggerFactory()

factory.log_message("message")

#
#
# 1. file
# 2.console
# Enter logger type: 1
# Logging to file: message
#
#


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsButton(Button):
    def paint(self):
        print("Created windows button")


class MacButton(Button):
    def paint(self):
        print("Created mac   button")


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Created windows-checkbox")


class MacCheckbox(Checkbox):
    def paint(self):
        print("Ceated mac-checkbox")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()


if input("1. Windows\n2. Mac\nEnter logger type: ") == "1":
    app = Application(WindowsFactory())
else:
    app = Application(MacFactory())

app.paint()

#
#
# 1. Windows
# 2. Mac
# Enter logger type: 1
# Created windows button
# Created windows-checkbox
#
#


class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def set_dough(self, dough: str):
        self.dough = dough

    def set_sauce(self, sauce: str):
        self.sauce = sauce

    def set_topping(self, topping: str):
        self.topping = topping

    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, {self.topping} topping"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("cross")
        return self

    def build_sauce(self):
        self.pizza.set_sauce("barbeque")
        return self

    def build_topping(self):
        self.pizza.set_topping("pineapple")
        return self

    def get_result(self):
        return self.pizza


class Director:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_pizza(self):
        (self.builder
         .build_dough()
         .build_sauce()
         .build_topping())


builder = PizzaBuilder()
director = Director(builder)
director.construct_pizza()

pizza = builder.get_result()

print(pizza)

#git check