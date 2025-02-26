from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


class ConsoleLogger:
    def log_to_console(self, msg: str):
        print(f"Console logging: {msg}")


class FileLogger:
    def write_to_file(self, text: str):
        print(f"File logging: {text}")


class CloudLogger:
    def send_log(self, data: str):
        print(f"Cloud logging: {data}")

# в логгерах должна быть своя логика поэтому методы сделаны не статичными

class ConsoleLoggerAdapter(Logger):
    def __init__(self, console_logger: ConsoleLogger):
        self.console_logger = console_logger

    def log(self, message: str):
        self.console_logger.log_to_console(message)


class FileLoggerAdapter(Logger):
    def __init__(self, file_logger: FileLogger):
        self.file_logger = file_logger

    def log(self, message: str):
        self.file_logger.write_to_file(message)


class CloudLoggerAdapter(Logger):
    def __init__(self, cloud_logger: CloudLogger):
        self.cloud_logger = cloud_logger

    def log(self, message: str):
        self.cloud_logger.send_log(message)


if __name__ == "__main__":
    console_logger = ConsoleLogger()
    file_logger = FileLogger()
    cloud_logger = CloudLogger()

    logger1 = ConsoleLoggerAdapter(console_logger)
    logger2 = FileLoggerAdapter(file_logger)
    logger3 = CloudLoggerAdapter(cloud_logger)

    # по итогу любой логгер мы можем добавлять в список

    for logger in [logger1, logger2, logger3]:
        logger.log("i love tech programmes.......................")
