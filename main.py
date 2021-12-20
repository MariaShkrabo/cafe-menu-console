# The program counts the ordered dishes and gives a total bill for a table in a cafe
# Laboratory work №30
# Name: Object Oriented Programming. Virtualization and polymorphic behavior in Python
# Version 1.0
# Shkrabo Maria M.
# Group №10701119
# Date: 04.05.2020

from interface_manager import Interface
from table import Table


def main():
    number_of_section = Interface.correct_input()
    Section, Table_section, string_menu = Interface.display_desired_section(number_of_section)
    list_of_dishes = Section.create_dish(5)
    print(Section.convert_to_string(list_of_dishes, "menu", string_menu))
    table = Table_section(3, "Common", 4)  # create the object table number 3, in the common room, for which 2 people sat
    print(str(table))
    Interface.get_bill(table, list_of_dishes, Section)
    print(Interface.number_of_objects() + "\n")
    del table


if __name__ == "__main__":
    main()
