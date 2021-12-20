from salad_god import SaladGod
from pizza_god import PizzaGod
from dessert_god import DessertGod
from drink_god import DrinkGod
from table import Table
from manager import Manager
from dish import Dish
from god import God
from drink_table import DrinkCostDiscount
from pizza_table import PizzaCostDiscount
from salad_table import SaladCostDiscount
from dessert_table import DessertCostDiscount


class Interface:
    @staticmethod
    def number_of_objects():
        return "\nIn total, " + str(
            Dish.get_count() + Table.get_count() + Manager.get_count() + God.get_count()) + " objects were created in the project. "

    @staticmethod
    def correct_input():
        needed_numbers = ["1", "2", "3", "4"]
        number_of_section = ""
        while number_of_section not in needed_numbers:
            number_of_section = str(
                input("You are offered a menu of four sections. Select the section from which you want to place an order:\n"
                      "\t1. Salads\n\t2. Pizzas\n\t3. Desserts\n\t4. Drinks\nYour choice: "))
            if number_of_section not in needed_numbers:
                print("Incorrect data! Expected number from 1 to 4. Try again.")
        return int(number_of_section)

    @staticmethod
    def display_desired_section(number_of_section):
        if number_of_section == 1:
            return SaladGod, SaladCostDiscount, "Starting today, in our cafe there is a 15% discount on low-calorie salads after 18:00. Take care of your health !!!\nSALADS MENU:\n"
        elif number_of_section == 2:
            return PizzaGod, PizzaCostDiscount, "Only today for a company of 4 people a 40% discount on every pizza !!!\nPIZZAS MENU:\n"
        elif number_of_section == 3:
            return DessertGod, DessertCostDiscount, "Saturday-Sunday in our cafe there is a 30% discount on all desserts. Come with the kids and have fun !!!\nDESSERTS MENU:\n"
        else:
            return DrinkGod, DrinkCostDiscount, "Every day in our cafe there is a discount on soft drinks after 22.00 before closing (3 a.m.)!!!\nDRINKS MENU:\n"

    @staticmethod
    def get_bill(table, list_of_dishes, Section):
        table.get_info_about_ordered_dishes(list_of_dishes)
        table.get_count_with_discount(list_of_dishes)
        print(Section.convert_to_string(list_of_dishes, "bill", ""))
        total = Manager.profit_from_table(list_of_dishes)
        print("TOTAL: %s" % total)
