cooking_dictionary = {"pizza": "oven", "bread": "toaster", "Roast Chicken": "oven", "Muffins": "toaster"}
def sub1 ():
        print(cooking_dictionary)
        print('To cook pizza we use', cooking_dictionary["pizza"])
        task_time = (f"To cook bread we use {cooking_dictionary['bread']}")
        print(task_time)
        print(f"To cook roast chicke we use {cooking_dictionary['Roast Chicken']}")
        print(f"To cook muffins we use {cooking_dictionary['Muffins']}")
sub1()