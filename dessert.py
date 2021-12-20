from dish import Dish


class Dessert(Dish):
    def __init__(self, name, hot_or_cold, grams, calorie, carbohydrates, proteins, fats, cost, quantity_ordered=0):
        super().__init__(name, grams, calorie, carbohydrates, proteins, fats, cost, quantity_ordered=0)
        self.__hot_or_cold = hot_or_cold

    def get_hot_or_cold(self):
        return self.__hot_or_cold

    def set_hot_or_cold(self, hot_or_cold):
        self.__hot_or_cold = hot_or_cold

    def __str__(self):
        return super().__str__() + "\n   " + self.__hot_or_cold + " dish."
