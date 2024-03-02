# 1. Nested Decisions: The Adventure Game 🏰
# Objective:

# To practice the use of nested if statements in creating a simple text-based adventure game.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to guide a user through an adventure game,
# but it has some errors. Identify and fix them.

# Buggy Code:

import random


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Just wandering through the forest")
elif place == "cave":
    cave_action = input("Would you like to 'light a torch' or 'proceed in the dark'.")
    if cave_action == "light a torch":
        print("The walls of the cave are lit by the torch.")
    elif cave_action == "proceed in the dark":
        print("The darkness of the cave surrounds you.")
    else:
        pass
    print("You find a hidden treasure!")
else:
    print("Just keep on wandering")


# Task 2: Setting the Scene

# Based on the corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

# Task 3: Default Path

# If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.

# 2. Quick Decisions: The Event Planner 🎉
# Objective:

# To practice the use of shorthand if statements in determining event-related decisions.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

# Buggy Code:

attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) > 100 else "conference room"
print(venue)
amenities = "Purchase audio system and projector." if venue == "large hall" else "Rent speakers and a tv."
dining_choice = input("Would you like vegetarian?(yes or no): ")    
caterer = "Veggie Delight Caterers" if dining_choice == "yes" else "Gourmet Meals Caterers"
# Task 2: Venue Selection

# Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees.

# Task 3: Catering Choices

# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

# 3. Silent Failures: The Error Handler 🐞
# Objective:

# To practice the use of the pass statement in handling potential errors silently.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to handle errors silently, but it has some mistakes. Identify and fix them.

# Buggy Code:

try:
    x = 1 / 0
except ZeroDivisionError:
    pass

try:
    x/"twenty"
except ValueError:
    pass

user_file_search = input("Please enter a file to search for: ")
try:
    with open(user_file_search, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    pass


# Task 2: Division Calculator

# Based on the corrected code from Task 1, enhance the program to handle other potential errors, such as ValueError when trying to divide a number by a string.

# Task 3: File Reader

# Ask the user for a filename to read. Try to open and read the file. If the file doesn't exist, use the pass statement to handle the error silently.

# 4. Nested Quick Decisions: The Shopping Assistant 🛍️
# Objective:

# To practice the use of nested shorthand if statements in assisting a shopping decision.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to assist in shopping, but it has errors. Identify and fix them.

# Buggy Code:

weather = input("Enter the weather: sunny, rainy, foggy or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
print(clothing)


# Task 2: Clothing Recommendation

# Based on the corrected code from Task 1, further enhance the program to recommend additional items like "hat" or "boots" based on the weather.

more_clothing = "rain boots" if weather == "rainy" else "hat" if weather == "sunny" else "coat"
print(more_clothing)

# Task 3: Accessory Recommendation

# Based on the clothing recommendation, suggest an accessory. For instance, if "sunglasses" were recommended, suggest "sunscreen" as an accessory.

accessories = "watch" if clothing == "sunglasses" else "poncho" if clothing == "umbrella" else "beanie"
print(accessories)

# 5. The Silent Logger: System Monitor 🖥️
# Objective:

# To practice the use of the pass statement in a system monitoring context.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to monitor system parameters, but it has some mistakes. Identify and fix them.

# Buggy Code:

# import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass

ram_usage = random.randint(0, 100)
if ram_usage > 90:
    print("High memory usage!")
elif ram_usage > 80 and ram_usage <= 90:
    pass
else:
    pass

disk_space = random.randint(0, 100)
if disk_space > 90:
    print("Disk space almost full!")
elif disk_space > 80 and disk_space <= 90:
    pass
else:
    pass

#Task 2: System Check

# Based on the corrected code from Task 1, enhance the program to also monitor memory usage and disk space, and provide alerts accordingly.

# Task 3: Alert System

# If any of the system parameters exceed a certain threshold, print an alert message. However, if the system parameter is within a "gray zone", use the pass statement to silently log this without alerting the user.
