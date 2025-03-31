# enter your name and age 
name = input("enter your name:")
age = input("enter your age")

#choose your activity that you want
activity_list = ['Music Jam Session (2 hours, easy, $5 fee)','Science Experiments Lab (3 hours, moderate, $10 fee)','Sports Leadership Training (4 hours, challenging, $12 fee)']
 
print('Choose an activity: ')
print(f'1. {activity_list[0]}')
print(f'2. {activity_list[1]}')
print(f'3. {activity_list[2]}')

activity_list = input("enter the number of your chosen activity:")
#choose what meal opition you want 
meal_opitions = ['standered','vegetarian','dairy-free','no meal']

print('choose a meal option: ')
print(f'1. {meal_opitions[0]}')
print(f'2. {meal_opitions[1]}')
print(f'3. {meal_opitions[2]}')


# Activity input with validation
while True:
    try:
        chosen_activity = int(input("Enter the number of your chosen activity: "))
        if chosen_activity in [1, 2, 3]:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


        # Chosen activity fee calculation
if chosen_activity == 1:
    activity_fee = 5
elif chosen_activity == 2:
    activity_fee = 10
elif chosen_activity == 3:
    activity_fee = 12

#meal input with validation

while True:
    try:
        chosen_meal = int(input("Enter the number of your chosen meal: "))
        if chosen_meal in [1, 2, 3, 4, 5]:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")




if chosen_meal == 1 or chosen_meal == 2 or chosen_meal == 3 or chosen_meal == 4: 
    meal_fee = 7
else:
    meal_fee = 0

    total_fee = activity_fee + meal_fee


print(f'{name}, aged {age}, has chosen "{activity_list[chosen_activity - 1]}", meal option: "{meal_opitions[chosen_meal - 1]}". The total fee is ${total_fee}.')
