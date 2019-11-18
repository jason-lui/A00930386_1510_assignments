def myFunctionName():
    """

    :return:
    """
    calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
                 "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
                 "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}

    # Input loop
    new_item = input("Enter food item to add, or ’q’ to exit: ")
    while new_item != "q":
        new_item_calories = int(input(f"Enter calories for {new_item}: "))
        calories[new_item] = new_item_calories
        total_calories = 0
        food_item_names = []

        for item in calories:
            total_calories += calories[item]
            food_item_names.append(item)

        avg_calories = total_calories / len(calories)

        print("\nFood Items:", sorted(food_item_names))
        print(f"Total Calories: {total_calories} Average Calories: %0.1f\n" % avg_calories)

        new_item = input("Enter food item to add, or ’q’ to exit: ")
