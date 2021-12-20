MAX_NUMBER_OF_ORDERED_DISHES = 4
MIN_NUMBER_OF_ORDERED_DISHES = 0


class Dish:
    """Class defines dish information"""
    __count = 0

    def __init__(self, name, grams, calorie, carbohydrates, proteins, fats, cost, quantity_ordered=MIN_NUMBER_OF_ORDERED_DISHES):
        self.__name = name
        self.__grams = grams
        self.__calorie = calorie
        self.__carbohydrates = carbohydrates
        self.__proteins = proteins
        self.__fats = fats
        self.__cost = cost
        self.__quantity_ordered = quantity_ordered  # quantity of ordered items (immediately 0)
        Dish.__count += 1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_grams(self):
        return self.__grams

    def set_grams(self, grams):
        self.__grams = grams

    def get_calorie(self):
        return self.__calorie

    def set_calorie(self, calorie):
        self.__calorie = calorie

    def get_carbohydrates(self):
        return self.__carbohydrates

    def set_carbohydrates(self, carbohydrates):
        self.__carbohydrates = carbohydrates

    def get_proteins(self):
        return self.__carbohydrates

    def set_proteins(self, proteins):
        self.__proteins = proteins

    def get_fats(self):
        return self.__fats

    def set_fats(self, fats):
        self.__fats = fats

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost

    def get_quantity_ordered(self):
        return self.__quantity_ordered

    def set_quantity_ordered(self, quantity_ordered):
        if MIN_NUMBER_OF_ORDERED_DISHES <= quantity_ordered <= MAX_NUMBER_OF_ORDERED_DISHES:
            self.__quantity_ordered = quantity_ordered

    @staticmethod
    def get_count():
        return Dish.__count

    def __str__(self):
        current_dish = "Dish name: " + self.__name + ". Dish volume: " + str(self.__grams) + "g. Calories: " + str(
            self.__calorie) + "kcal. Carbohydrates: " + str(self.__carbohydrates) + "%. Proteins: " + str(self.__proteins) + \
            "%. Fats: " + str(self.__fats) + "%. Cost: $" + str(self.__cost) + ". "
        if self.__quantity_ordered != MIN_NUMBER_OF_ORDERED_DISHES:
            current_dish += "Quantity ordered: " + str(self.__quantity_ordered) + " items. "
        return current_dish

    def __del__(self):
        Dish.__count -= 1
        print("Object Dish was deleted")


