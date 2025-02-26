from abc import ABC, abstractmethod


# Абстрактная бд
class Database(ABC):
    @abstractmethod
    def query(self, sql: str):
        pass


# Реальный объект
class RealDatabase(Database):
    def query(self, sql: str):
        print(f"Query: {sql}")


# Прокси для контроля доступа
class DatabaseProxy(Database):
    def __init__(self, has_access: bool):
        self._real_database = RealDatabase()
        self._has_access = has_access

    def query(self, sql: str):
        if self._has_access:
            self._real_database.query(sql)
        else:
            print("Access denied.")


if __name__ == "__main__":
    user_db = DatabaseProxy(False)
    admin_db = DatabaseProxy(True)

    user_db.query("SELECT * FROM users")
    admin_db.query("SELECT * FROM users")
