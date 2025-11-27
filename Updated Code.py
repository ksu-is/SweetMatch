import random 
#Import random so when there's more than one dessert option for a given mood and flavor, the program can randomly choose one instead of giving the same result every time. 

#creating a function for the dessert recommendation. 
dessert_by_mood = {
    'happy':{
        "chocolate": ["Chocolate Lava Cake", "Brownie Sundae", "S'mores"],
        "fruity": ["Strawberry Shortcake", "Lemon Blueberry Muffins", "Raspberry Sorbet"],
        "creamy": ["New York Cheesecake", "Banana Pudding", "Creme Puffs"],
    },
    'sad/stressed': {
        "chocolate": ["Warm Chocolate Chip Skillet Cookie", "Flourless Chocolate Cake", "Double Fudge Brownies"],
        "fruity": ["Blackberry Cobbler", "Banana Bread", "Apple Turnover with Vanilla Bean Ice Cream"],
        "creamy": ["Rice Pudding", "Jumbo Cinnamon Rolls", "Spanish Flan"],
    },
    'cozy/romantic': {
        "chocolate": ["Black Forest Cake", "Hot Cocoa Bombs", "Red Velvet Cake "],
        "fruity": ["Berry Pavlova", "Vanilla Bourbon Poached Pears", "Chocolate-Covered Strawberries"],
        "creamy": ["Creme Brulee", "Tiramisu", "White Chocolate Mousse"],
    },
    'adventurous': {
        "chocolate": ["Chili Chocolate Pudding with Grilled Peaches", "White Chocolate Matcha Cookies", "Lavender Chocolate Truffles"],
        "fruity": ["Blood Orange Sorbet", "Guava Cheesecake", "Watermelon Mint Granita"],
        "creamy": ["Masala Chai Panna Cotta", "Ube Mochi Ice Cream", "Lychee Mille-Feuille"],
    }
}

def prompt_menu(prompt,options):
    while True:
        print(prompt)
        for letter, label in options.items():
            print(f"{letter}.{label}")
        choice = input("Choose an option: ").strip().lower()
        if choice == 'q':
            return 'q'
        if choice in options:
            return options [choice]
        print("\nInvalid choice - please try again.\n")


print("Hello! How are you feeling today?\n")

while True:
    mood_options = {
        "a": "happy",
        "b": "sad/stressed",
        "c": "cozy/romantic",
        "d": "adventurous"
    }

    mood = prompt_menu ("Select your mood (or press q to quit): ", mood_options)
    if mood == 'q':
        print("\nNo worries - treat yourself soon!")
        break


    flavor_options = {
        "a": "chocolate",
        "b": "fruity",
        "c": "creamy"
}

    flavor = prompt_menu ("What flavor are you craving?: ", flavor_options)
    if flavor == 'q':
        print ("\nNo worries - treat yourself soon!")
        break


# get dessert list
    desserts = dessert_by_mood[mood][flavor]

    print(f"\nSince you're feeling {mood}, and craving something {flavor} , here are some desserts!\n")

    accepted = False
    for index, dessert in enumerate(desserts):
        print(f"How about: {dessert}? ")
        answer = input("Do you like this suggestion?(y/n)").strip().lower()
        if answer == "q":
            print("\nNo worries - treat yourself soon!")
            accepted = True 
            break
        if answer == "y":
            print("\nEnjoy your treat!")
            accepted = True
            break
        if index < len(desserts) - 1:
            print("Okay, let's try another...\n")
    if accepted:
        break
    while True:
        retry = input("\nYou didn't like any of those recommendations, would you like to try a new mood or flavor? (y/n): ").strip().lower()
        if retry == 'y':
            print("\nRestarting...\n")
            break
        elif retry == 'n' or retry == 'q':
            print("\nNo worries - treat yourself soon!")
            exit()
        else: 
            print("Please enter 'y' or 'n'. ")





