# cafe-menu-console-python
A console application written in python. It is an electronic order management in a cafe.
Description of the subject area:
The subject area is the calculation of the total amount of an order from a specific table in a cafe, depending on the selected category of dishes.
As a result of the analysis of the subject area, the following classes were identified:

• dish (Dish) - an entity class that describes the characteristics of a dish;

• salads (Salad) - a class that inherits the properties and methods of the Dish class and represents the “Salads” category from the general list of dishes;

• pizzas (Pizza) - a class that inherits the properties and methods of the Dish class and represents the “Pizza” category from the general list of dishes;

• desserts (Dessert) - a class that inherits the properties and methods of the Dish class and represents the “Desserts” category from the general list of dishes;

• drinks (Drink) - a class that inherits the properties and methods of the Dish class and represents the “Drinks” category from the general list of dishes;

• table - a general class that describes both the characteristics of the table and some logic that sets the number of ordered dishes, which in turn depends on the corresponding state of the table: the number of people sitting at it, which sets the discount conditions;

• discount on salads (SaladCostDiscount) - a class in which the price of a salad (low-calorie in relation to all others) is reduced by 15% if the discount condition is met: the order is completed after 18:00

• discount on pizzas (PizzaCostDiscount) - a class in which the price of pizza is reduced by 40% if the discount condition is met: a table is occupied by a company of 4 people

• discount on desserts (DessertCostDiscount) - a class in which the price of a dessert is reduced by 30% if the discount condition is met: the order is completed on a weekend

• discount on drinks (DessertCostDiscount) - a class in which the price of a drink (non-alcoholic) is reduced by 50% if the discount condition is met: the order is completed after 22:00 and before the cafe closes

• manager (Manager) - functional class, which describes the main business logic of the application - calculating the total amount of the order;

• Most High (God) - a utility class for creating a list of dishes, as well as presenting this list in a string version for output to the console;

• Forming salads (SaladGod) - a utility class for creating a list of salads;

• Forming pizza (PizzaGod) - a utility class for creating a list of pizzas;

• Forming desserts (DessertGod) - a utility class for creating a list of desserts;

• Forming drinks (DrinkGod) - a utility class for creating a list of drinks;

• Interface - a system class that organizes interaction with the user in the console.
