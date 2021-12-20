import datetime
from dish import Dish
from table import Table
from salad import Salad


class SaladCostDiscount(Table):
    __DISCOUNT = 15
    __current_hour = datetime.datetime.now().hour
    __MIN_CALORIE = 100
    __MAX_CALORIE = 500

    def get_count_with_discount(self, list_of_dishes):
        if 18 <= self.__current_hour <= 23:
            for dish in list_of_dishes:
                if issubclass(Salad, Dish) and dish.get_calorie() <= ((self.__MAX_CALORIE - self.__MIN_CALORIE) // 2):
                    dish.cost = dish.set_cost(round(dish.get_cost() - dish.get_cost() * 0.01 * self.__DISCOUNT, 1))

