import doctest


def calorie_counter():
    """
    Assemble and print a list of food items, total calorie count, and the average calorie count.

    :postcondition: the food list will be assembled and printed
    """
    food_items = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
                 "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
                 "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}

    # Input loop
    new_item = input("Enter food item to add, or 'q' to exit: ")
    while new_item != "q":
        # Update dictionary with the new food item and its caloric value
        new_item_calories = int(input(f"Enter calories for {new_item}: "))
        food_items[new_item] = new_item_calories

        # Print food list, total calories, and average calories
        print_food_calories(food_items)

        # Ask for the next item or quit
        new_item = input("Enter food item to add, or 'q' to exit: ")


def print_food_calories(food_dict: dict):
    """
    Print the a sorted list of foods, its total calorie count, and its average calorie per item.

    :param food_dict: a dictionary
    :precondition: food_dict must be a dictionary of food items as strings and their caloric values as ints
    :postcondition: a sorted list of foods, a total calorie count, and an average calorie count will be printed

    >>> print_food_calories({"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66})
    <BLANKLINE>
    Food Items: ['apple', 'bread', 'carrot', 'lettuce']
    Total Calories: 195 Average Calories: 48.8
    <BLANKLINE>
    """
    total_calories = sum([value for value in food_dict.values()])
    avg_calories = total_calories / len(food_dict)

    print("\nFood Items:", sorted(food_dict.keys()))
    print("Total Calories:", total_calories, "Average Calories: %0.1f\n" % avg_calories)


if __name__ == '__main__':
    doctest.testmod()
