from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance) -> None:
        ...

    @abstractmethod
    def refuel(self, fuel) -> None:
        ...


class Car(Vehicle):
    AC_FUEL_CONS = 0.9

    def drive(self, distance: float) -> None:
        fuel_needed = distance * (self.fuel_consumption + self.AC_FUEL_CONS)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= (self.fuel_consumption + 0.9) * distance

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_FUEL_CONS = 1.6

    def drive(self, distance: float) -> None:
        fuel_needed = distance * (self.fuel_consumption + self.AC_FUEL_CONS)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= (self.fuel_consumption + 1.6) * distance

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * 0.95
