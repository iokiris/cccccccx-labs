from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None


class HandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("HandlerA hanlded")
            return True
        return super().handle(request)


class HandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("HandlerB handled")
            return True
        return super().handle(request)


if __name__ == "__main__":
    handler_a = HandlerA()
    handler_b = HandlerB()

    handler_a.set_next(handler_b)

    requests = ["A", "B", "C"]

    for req in requests:
        if not handler_a.handle(req):
            print(f"'{req}' is not handled")
