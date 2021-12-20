import random
from god import God
from dessert import Dessert


class DessertGod(God):
    @staticmethod
    def create_dish(quantity):
        names = ["Flapjack", "Bakewell tart", "Victoria sponge", "Zwetschgenkuchen", "Grand soletto"]
        temps = ["Hot", "Cold"]
        list_of_desserts = []
        if quantity > len(names):
            print("Error! We do not have so many salads")
            exit(0)
        for salad in range(quantity):
            grams, carbohydrates, proteins, fats, cost = God.create_dishes()
            name = random.choice(names)
            hot_or_cold = random.choice(temps)
            calorie = random.randint(500, 1000)
            i = 0
            while i < len(names):  # so that there are no repetitions in the names of dishes, the used name is deleted
                if names[i] == name:
                    names.remove(names[i])
                else:
                    i += 1
            dish = Dessert(name, hot_or_cold, grams, calorie, carbohydrates, proteins, fats, cost)
            list_of_desserts.append(dish)
        return list_of_desserts
