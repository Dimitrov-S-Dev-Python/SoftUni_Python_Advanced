from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name, dough, topping_capacity):
        self.name = name
        self.dough = dough
        self.topping_capacity = topping_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def topping_capacity(self):
        return self.__topping_capacity

    @topping_capacity.setter
    def topping_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or "
                             "equal to zero")
        self.__topping_capacity = value

    def add_topping(self, topping: Topping):
        if self.__topping_capacity == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        if topping.topping_type is not self.toppings:
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        total_dough = self.dough.weight
        total_topping = sum(t[1] for t in self.toppings.items())

        return total_dough + total_topping
