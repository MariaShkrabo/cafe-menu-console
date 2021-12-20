import random
from god import God
from pizza import Pizza


class PizzaGod(God):
    @staticmethod
    def create_dish(quantity):
        names = ["Margherita", "Peperoni", "Bolognese", "Mexicana", "Hawaii"]
        times = ["10-15", "15-20", "25-30"]
        diameters = [10, 20, 30]
        list_of_pizzas = []
        if quantity > len(names):
            print("Error! We do not have so many salads")
            exit(0)
        for salad in range(quantity):
            grams, carbohydrates, proteins, fats, cost = God.create_dishes()
            name = random.choice(names)
            time = random.choice(times)
            diameter = random.choice(diameters)
            calorie = random.randint(700, 2000)
            i = 0
            while i < len(names):  # so that there are no repetitions in the names of dishes, the used name is deleted
                if names[i] == name:
                    names.remove(names[i])
                else:
                    i += 1
            dish = Pizza(name, grams, diameter, calorie, carbohydrates, proteins, fats, time, cost)
            list_of_pizzas.append(dish)
        return list_of_pizzas
