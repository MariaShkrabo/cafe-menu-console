from dish import Dish


class Pizza(Dish):
    def __init__(self, name, grams, diameter, calorie, carbohydrates, proteins, fats, time, cost, quantity_ordered=0):
        super().__init__(name, grams, calorie, carbohydrates, proteins, fats, cost, quantity_ordered=0)
        self.__diameter = diameter
        self.__time = time

    def get_diameter(self):
        return self.__diameter

    def set_diameter(self, diameter):
        self.__diameter = diameter

    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time

    def __str__(self):
        return super().__str__() + "\n   Diameter: " + str(self.__diameter) + "cm. Time for preparing: " + self.__time + "min."
