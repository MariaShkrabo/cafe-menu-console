import datetime
from dish import Dish
from table import Table
from dessert import Dessert


class DessertCostDiscount(Table):
    __DISCOUNT = 30
    __current_day_of_week = datetime.datetime.today().isoweekday()

    def get_count_with_discount(self, list_of_dishes):
        if 6 <= self.__current_day_of_week <= 7:
            for dish in list_of_dishes:
                if issubclass(Dessert, Dish):
                    dish.cost = dish.set_cost(round(dish.get_cost() - dish.get_cost() * 0.01 * self.__DISCOUNT, 1))

