import random
from dish import Dish
from drink import Drink
from manager import Manager


class DrinkManager(Manager):
    __DISCOUNT = 50
    __MIN_HOUR = 22
    __MAX_HOUR = 3

    def profit_from_table(self, list_of_dishes):
        profit = 0
        for dish in list_of_dishes:
            if issubclass(Drink, Dish):
                profit += dish.get_cost() * dish.get_quantity_ordered()
        return "$" + str(profit)
