import random
from dish import Dish
from salad import Salad
from pizza import Pizza
from drink import Drink


class Manager:
    """functional class for business logic"""
    __count = 0

    def __init__(self):
        Manager.__count += 1

    @staticmethod
    def profit_from_table(list_of_dishes):
        profit = 0
        for dish in list_of_dishes:
            if issubclass(Salad or Pizza or Drink, Dish):
                profit += dish.get_cost() * dish.get_quantity_ordered()
        return "$"+str(round(profit,1))

    @staticmethod
    def get_count():
        return Manager.__count

    def __del__(self):
        Manager.__count -= 1
        print("Object Manager was deleted")
