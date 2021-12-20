import random
from god import God
from drink import Drink


class DrinkGod(God):
    @staticmethod
    def create_dish(quantity):
        names = ["Tea", "Coffee", "Bear", "Mojito", "Daiquiri"]
        list_of_drinks = []

        if quantity > len(names):
            print("Error! We do not have so many salads")
            exit(0)
        for salad in range(quantity):
            grams, carbohydrates, proteins, fats, cost = God.create_dishes()
            name = random.choice(names)
            calorie = random.randint(20, 100)
            if name == "Tea" or name == "Coffee":
                alcoholicity = 0
            else:
                alcoholicity = random.randint(6, 20)
            i = 0
            while i < len(names):  # so that there are no repetitions in the names of dishes, the used name is deleted
                if names[i] == name:
                    names.remove(names[i])
                else:
                    i += 1
            dish = Drink(name, grams, calorie, carbohydrates, proteins, fats, alcoholicity, cost)
            list_of_drinks.append(dish)
        return list_of_drinks
