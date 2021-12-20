from dish import Dish


class Salad(Dish):
    def __init__(self, name, classification, grams, calorie, carbohydrates, proteins, fats, cost, quantity_ordered=0):
        super().__init__(name, grams, calorie, carbohydrates, proteins, fats, cost, quantity_ordered=0)
        self.__classification = classification

    def get_classification(self):
        return self.__classification

    def set_classification(self, classification):
        self.__classification = classification

    def __str__(self):
        return super().__str__() + "\n   Classification: " + self.__classification
