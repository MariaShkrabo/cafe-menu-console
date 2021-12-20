from dish import Dish


class Drink(Dish):
    def __init__(self, name, grams, calorie, carbohydrates, proteins, fats, alcoholicity, cost, quantity_ordered=0):
        super().__init__(name, grams, calorie, carbohydrates, proteins, fats, cost, quantity_ordered=0)
        self.__alcoholicity = alcoholicity

    def get_alcoholicity(self):
        return self.__alcoholicity

    def set_alcoholicity(self, alcoholicity):
        self.__alcoholicity = alcoholicity

    def __str__(self):
        return super().__str__() + "\n   Alcoholicity: " + str(self.__alcoholicity) + "%."
