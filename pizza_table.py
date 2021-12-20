from dish import Dish
from table import Table
from pizza import Pizza


class PizzaCostDiscount(Table):
    __DISCOUNT = 40
    __NUMBER_OF_PEOPLE_FOR_DISCOUNT = 4

    def get_count_with_discount(self, list_of_dishes):
        for dish in list_of_dishes:
            if issubclass(Pizza, Dish) and super().get_number_of_people() == self.__NUMBER_OF_PEOPLE_FOR_DISCOUNT:
                dish.cost = dish.set_cost(round(dish.get_cost() - dish.get_cost() * 0.01 * self.__DISCOUNT, 1))

