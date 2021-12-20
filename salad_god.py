import random
from god import God
from salad import Salad


class SaladGod(God):
    @staticmethod
    def create_dish(quantity):
        names = ["Cobb", "Israeli", "Mexican black bean", "Gado-gado", "Nicoise"]
        classifications = ["Salad-appetite", "Main salad", "Dessert salad", "Complementary salad"]
        list_of_salads = []
        if quantity > len(names):
            print("Error! We do not have so many salads")
            exit(0)
        for salad in range(quantity):
            grams, carbohydrates, proteins, fats, cost = God.create_dishes()
            name = random.choice(names)
            classification = random.choice(classifications)
            calorie = random.randint(100, 500)
            i = 0
            while i < len(names):  # so that there are no repetitions in the names of dishes, the used name is deleted
                if names[i] == name:
                    names.remove(names[i])
                else:
                    i += 1
            dish = Salad(name, classification, grams, calorie, carbohydrates, proteins, fats, cost)
            list_of_salads.append(dish)
        return list_of_salads
