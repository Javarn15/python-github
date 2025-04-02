while True:
    try:
        chosen_meal = int(input("Enter the number of your chosen meal: "))
        if chosen_meal in [1, 2, 3, 4, 5]:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
