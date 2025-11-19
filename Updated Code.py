import random 
#Import random so when there's more than one dessert option for a given mood and flavor, the program can randomly choose one instead of giving the same result every time. 

#creating a function for the dessert recommendation. 
dessert_by_mood = {
    'happy':{
        "chocolate": ["Chocolate Lava Cake", "Brownie Sundae", "S'mores"],
        "fruity": ["Strawberry Shortcake", "Lemon Blueberry Muffins", "Raspberry Sorbet"],
        "creamy": ["New York Cheesecake", "Banana Pudding", "Creme Puffs"]
    },
    'sad/stressed': {
        "chocolate": ["Warm Chocolate Chip Skillet Cookie", "Flourless Chocolate Cake", "Double Fudge Brownies"],
        "fruity": ["Blackberry Cobbler", "Banana Bread", "Apple Turnover with Vanilla Bean Ice Cream"],
        "creamy": ["Rice Pudding", "Jumbo Cinnamon Rolls", "Spanish Flan"]
    },
    'cozy/romantic': {
        "chocolate": ["Black Forest Cake", "Hot Cocoa Bombs", "Red Velvet Cake "],
        "fruity": ["Berry Pavlova", "Vanilla Bourbon Poached Pears", "Chocolate-Covered Strawberries"],
        "creamy": ["Creme Brulee", "Tiramisu", "White Chocolate Mousse"]
    },
    'adventurous': {
        "chocolate": ["Chili Chocolate Pudding with Grilled Peaches", "White Chocolate Matcha Cookies", "Lavender Chocolate Truffles"],
        "fruity": ["Blood Orange Sorbet", "Guava Cheesecake", "Watermelon Mint Granita"],
        "creamy": ["Masala Chai Panna Cotta", "Ube Mochi Ice Cream", "Lychee Mille-Feuille"]
    }
}

def prompt_menu(prompt, options): 
    print(prompt) 
    for letter, label in options.items():
        print(f"{letter}.{label}")
    choice = input ("Choose an option: ").lower()
    return options.get(choice)
    
print("Hello! How are you feeling today?\n")

mood_options = {
    "a": "happy",
    "b": "sad/stressed",
    "c": "cozy/romantic",
    "d": "adventurous"
}

mood = prompt_menu ("Select your mood: ", mood_options)

if not mood:
    print("Sorry, I couldn't find recommendations for that mood.")
    quit()


flavor_options = {
    "a": "chocolate",
    "b": "fruity",
    "c": "creamy"
}

flavor = prompt_menu ("What flavor are you craving?", flavor_options)

if not flavor:
    print("Sorry, I couldn't find recommendations for that flavor.")
    quit()

# get dessert list
desserts = dessert_by_mood[mood][flavor]

print(f"\nSince you're feeling {mood}, here are some {flavor} desserts!\n")

for dessert in desserts:
    print(f"How about: {dessert}?")
    answer = input("So you like this suggestion? (y/n): ").lower()

    if answer == "y":
        print("Enjoy your dessert!")
        quit()
    else:
        print("Okay, let's try another...\n")
print("Those were all the dessert options! \n Restart the program to try again.")

