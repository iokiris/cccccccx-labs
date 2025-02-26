from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def print(self, data: str):
        pass


class Monitor(Device):
    def print(self, data: str):
        print(f"Displaying on monitor: {data}")


class Printer(Device):
    def print(self, data: str):
        print(f"Printing to paper: {data}")


class Output(ABC):
    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def render(self, data: str):
        pass


class TextOutput(Output):
    def __init__(self, device: Device):
        super().__init__(device)

    def render(self, data: str):
        self.device.print(f"Text: {data}")


class ImageOutput(Output):
    def __init__(self, device: Device):
        super().__init__(device)

    def render(self, data: str):
        self.device.print(f"Image: [Binary data: {data}]")


if __name__ == "__main__":
    monitor = Monitor()
    printer = Printer()

    text_on_monitor = TextOutput(monitor)
    text_on_printer = TextOutput(printer)
    image_on_monitor = ImageOutput(monitor)

    text_on_monitor.render("Hello, world!")         # Вывод: Displaying on monitor: Text: Hello, world!
    text_on_printer.render("Hello, world!")         # Вывод: Printing to paper: Text: Hello, world!
    image_on_monitor.render("101010101")            # Вывод: Displaying on monitor: Image: [Binary data: 101010101]
