import datetime
from dish import Dish
from table import Table
from drink import Drink


class DrinkCostDiscount(Table):
    __DISCOUNT = 50
    __current_hour = datetime.datetime.now().hour

    def get_count_with_discount(self, list_of_dishes):
        if 22 <= self.__current_hour <= 23 or 0 <= self.__current_hour <= 3:
            for dish in list_of_dishes:
                if issubclass(Drink, Dish) and dish.get_alcoholicity() == 0:
                    dish.cost = dish.set_cost(round(dish.get_cost() - dish.get_cost() * 0.01 * self.__DISCOUNT, 1))

