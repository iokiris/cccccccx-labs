from abc import ABC, abstractmethod


class GameObject:
    def __init__(self, uid: int, name: str, x: int, y: int):
        self._uid = uid
        self._name = name
        self._x = x
        self._y = y

    def get_id(self):
        return self._uid

    def get_name(self):
        return self._name

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


#
#

class Unit(GameObject, ABC):
    def __init__(self, uid: int, name: str, x: int, y: int, health: float):
        super().__init__(uid, name, x, y)
        self._health = health

    def is_alive(self) -> bool:
        return self._health > 0

    def receive_damage(self, damage: float) -> None:
        self._health = max(0.0, self._health - damage)

    def get_hp(self) -> float:
        return self._health


#
# Abstract classes
#

class Attacker(ABC):
    @abstractmethod
    def attack(self, target: Unit):
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass


#
#


class Building(GameObject):
    def __init__(self, uid: int, name: str, x: int, y: int, pre_built: bool):
        super().__init__(uid, name, x, y)
        self._is_built = pre_built

    def is_alive(self) -> bool:
        return self._is_built

    def build(self):
        self._is_built = True

    def destroy(self):
        self._is_built = False


class Fort(Building, Attacker):
    def __init__(self, uid: int, name: str, x: int, y: int, damage: float):
        self._damage = damage
        super().__init__(uid=uid, name=name, x=x, y=y, pre_built=True)

    def attack(self, target: Unit):
        if self.is_alive():
            target.receive_damage(self._damage)


class MobileHouse(Building, Moveable):
    def __init__(self, uid: int, name: str, x: int, y: int):
        super().__init__(uid=uid, name=name, x=x, y=y)

    def move(self, x: int, y: int):
        self._x = x * 3
        self._y = y


class Archer(Unit, Attacker, Moveable):

    def __init__(self, uid: int, name: str, x: int, y: int, damage: float):
        super().__init__(uid=uid, name=name, x=x, y=y, health=100.0)
        self._damage = damage

    def is_alive(self) -> bool:
        return self.get_hp() > 0

    def attack(self, target: Unit):
        if self.is_alive():
            target.receive_damage(self._damage)

    def move(self, x: int, y: int):
        self._x = x * 2
        self._y = y * 2
