# names = ["Ada", "Alan", "Bill", "John"]
# name_to_remove = input("Who do you want to remove: ")
#
# while name_to_remove != "":
#     if name_to_remove in names:
#         names.remove(name_to_remove)
#     else:
#         print(f"{name_to_remove} is not in the list")
#
#     print(", ".join(names))
#     name_to_remove = input("Who do you want to remove: ")
#
# names = ["Ada", "Alan", "Bill", "John"]
# while len(names) != 0:
#     try:
#         name_to_remove = input("Who do you want to remove: ")
#     expect ValueError
#         print("Invalid input, Try again!")
#     print(names)
#     name_to_remove = input("Who do you want to remove: ")

# numbers = [10, 3, 6, -20, 87, 3, -1]
# print(numbers)
# print([number + 2 for number in numbers])
#
# print([number for number in numbers if number > 50])
#
# for number in numbers:
#     print(number * 2)
#
# print([number * 2 for number in numbers if number > 50])
# print([number for number in numbers if number < 0])
#
# def main():
#     numbers = get_numbers()
#     squared_numbers = square_numbers(numbers)
#     display_numbers(squared_numbers)
#
#
# def get_numbers():
#     """Get numbers from the user as a list of floats."""
#     numbers_str = input("Enter numbers separated by commas: ")
#     numbers = [float(num) for num in numbers_str.split(',')]
#     return numbers
#
#
# def square_numbers(numbers):
#     """Return a list of squared numbers."""
#     return [num ** 2 for num in numbers]
#
#
# def display_numbers(numbers):
#     """Display the numbers separated by commas."""
#     print(", ".join([f"{num:.1f}" for num in numbers]))
#
#
# main()


# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
#
#
# def display_data(data):
#     # Find the maximum length of the names to align the output
#     max_name_length = max(len(name) for name, score in data)
#
#     for name, score in data:
#         # Print each name, aligned to the maximum length, followed by the score
#         print(f"{name:<{max_name_length}} = {score}")
#
#
# display_data(data)
#
#
# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
#
#

"""
CP1404 Assignment 1 - Travel Tracker
Name: Yuye Guo
Date started: 15/10/2024
GitHub URL: https://github.com/cp1404-students/a1-YY-05
"""

import csv
import random

FILENAME = 'places.csv'


def main():
    """Main function for Travel Tracker."""
    print("Travel Tracker 1.0 - by Yuye Guo")
    places = load_places(FILENAME)
    print(f"{len(places)} places loaded from {FILENAME}")

    while True:
        display_menu()
        choice = input(">>> ").lower().strip()

        if choice == 'd':
            display_places(places)
        elif choice == 'r':
            recommend_place(places)
        elif choice == 'a':
            add_place(places)
        elif choice == 'm':
            mark_place_as_visited(places)
        elif choice == 'q':
            save_places(FILENAME, places)
            print(f"{len(places)} places saved to {FILENAME}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def display_menu():
    """Display the menu options to the user."""
    print("Menu:")
    print("D - Display all places")
    print("R - Recommend a random place")
    print("A - Add a new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def load_places(filename):
    """Load places from a CSV file and return them as a list of dictionaries."""
    places = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                name, country, priority, visited = row
                places.append({'name': name, 'country': country, 'priority': int(priority), 'visited': visited == 'v'})
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty list of places.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return places


def display_places(places):
    sorted_places = sorted(places, key=lambda place: (place['visited'], place['priority']))

    count_unvisited = sum(1 for place in places if not place['visited'])

    max_name_length = max(len(place['name']) for place in sorted_places)
    max_country_length = max(len(place['country']) for place in sorted_places)

    for index, place in enumerate(sorted_places, start=1):
        visit_status = "*" if not place['visited'] else " "
        print(f"{visit_status}{index:>2}. {place['name']:<{max_name_length}} in {place['country']:<{max_country_length}} {place['priority']:>2}")

    print(f"{len(places)} places tracked. You still want to visit {count_unvisited} places.")


def recommend_place(places):
    """Recommend a random place from the list of unvisited places."""
    unvisited_places = [place for place in places if place['visited'] == False]
    if unvisited_places:
        place = random.choice(unvisited_places)
        print(f"Not sure where to visit next?")
        print(f"How about... {place['name']} in {place['country']}?")
    else:
        print("No places left to visit!")


def add_place(places):
    """Add a new place to the list."""
    while True:
        name = input("Name: ").strip()
        if name:
            break
        print("Input can not be blank")

    while True:
        country = input("Country: ").strip()
        if country:
            break
        print("Input can not be blank")

    while True:
        try:
            priority = int(input("Priority: "))
            if priority > 0:
                break
            else:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")

    new_place = {'name': name, 'country': country, 'priority': priority, 'visited': False}
    places.append(new_place)
    print(f"{new_place['name']} in {new_place['country']} (priority {new_place['priority']}) added to Travel Tracker.")


def mark_place_as_visited(places):
    """Mark a place as visited from the list."""
    sorted_places = sorted(places, key=lambda place: (place['visited'], place['priority']))

    unvisited_places = [place for place in places if place['visited'] == False]

    if not unvisited_places:
        print("No unvisited places")
        return

    display_places(places)
    print("Enter the number of a place to mark as visited")

    while True:
        try:
            place_number_input = input(">>> ").strip()
            place_number = int(place_number_input)

            if place_number < 1:
                print("Number must be > 0")
            elif place_number > len(sorted_places):
                print("Invalid place number")
            elif sorted_places[place_number - 1]['visited']:
                print(f"You have already visited {sorted_places[place_number - 1]['name']}")
                break
            else:
                original_place = sorted_places[place_number - 1]
                original_place['visited'] = True
                print(f"{original_place['name']} in {original_place['country']} visited!")
                break
        except ValueError:
            print("Invalid input; enter a valid number")


def save_places(filename, places):
    """Save the current list of places to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for place in places:
            writer.writerow([place['name'], place['country'], place['priority'], 'v' if place['visited'] else 'n'])


main()














