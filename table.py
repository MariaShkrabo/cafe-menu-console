MAX_TABLE_NUMBER = 20
MIN_TABLE_NUMBER = 1

MAX_NUMBER_OF_PEOPLE = 4
MIN_NUMBER_OF_PEOPLE = 1

MIN_NUMBER_OF_ORDERED_DISHES = 0

import random
from dish import Dish
from salad import Salad
from pizza import Pizza
from drink import Drink
from dessert import Dessert


class Table:
    """Class defines table information and generates the amount of each dish ordered"""
    __count = 0

    def __init__(self, number, hall, number_of_people):
        self.__number = number
        self.__hall = hall
        self.__number_of_people = number_of_people
        Table.__count += 1

    def get_number(self):
        return self.__number

    def set_number(self, number):
        if MIN_TABLE_NUMBER <= number <= MAX_TABLE_NUMBER:
            self.__number = number

    def get_hall(self):
        return self.__number

    def set_hall(self, hall):
        if hall == "VIP" or hall == "Common":
            self.__hall = hall

    def get_number_of_people(self):
        return self.__number_of_people

    def set_number_of_people(self, number_of_people):
        if MIN_NUMBER_OF_PEOPLE <= number_of_people <= MAX_NUMBER_OF_PEOPLE:
            self.__number_of_people = number_of_people

    @staticmethod
    def get_count():
        return Table.__count

    def __str__(self):
        return "BILL of table number " + str(self.__number) + ". " + self.__hall + " hall. " + str(
            self.__number_of_people) + " people."

    def get_info_about_ordered_dishes(self, list_of_dishes):
        for dish in list_of_dishes:
            if issubclass(Salad or Pizza or Dessert or Drink, Dish):
                dish.quantity_ordered = dish.set_quantity_ordered(random.randint(MIN_NUMBER_OF_ORDERED_DISHES,
                                                                                 self.__number_of_people))  # one dish is ordered at most once per person

    def get_count_with_discount(self, list_of_dishes):
        raise NotImplementedError

    def __del__(self):
        Table.__count -= 1
        print("Object Table was deleted")
