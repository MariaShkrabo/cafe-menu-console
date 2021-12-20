import random
from dish import Dish
from salad import Salad
from pizza import Pizza
from drink import Drink
from dessert import Dessert


class God:
    """ functional class for working with list of dishes"""
    __count = 0

    def __init__(self):
        God.__count += 1

    @staticmethod
    def get_count():
        return God.__count

    @staticmethod
    def create_dishes():
        grams = random.randint(1, 1000)
        carbohydrates = round(random.uniform(1, 20), 1)
        proteins = round(random.uniform(1, 100 - carbohydrates), 1)
        fats = round(100 - proteins - carbohydrates, 1)  # since the total amount of carbohydrates, fats and proteins is 100 percent
        cost = random.randint(1, 20)
        return grams, carbohydrates, proteins, fats, cost

    @staticmethod
    def convert_to_string(list_of_dishes, state, string_menu):
        string = string_menu
        count = 0
        if state == "menu":
            for dish in list_of_dishes:
                if issubclass(Salad or Pizza or Drink, Dish):
                    count += 1
                    string += str(count) + ") " + str(dish) + "\n"
        elif state == "bill":
            for dish in list_of_dishes:
                if issubclass(Salad or Pizza or Dessert or Drink, Dish) and dish.get_quantity_ordered() != 0:
                    count += 1
                    string += str(count) + ") " + str(dish) + "\n"
        return string

    def __del__(self):
        God.__count -= 1
        print("Object God was deleted")