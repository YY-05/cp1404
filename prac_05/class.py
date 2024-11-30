# def main():
#     strings = ['Bill', 'Jane', 'Sven']
#     result = string_lengths(strings)
#     print(result)
#
#
# def string_lengths(strings):
#     """Return a dictionary"""
#     lengths = {}
#     for string in strings:
#         lengths[string] = len(string)
#     return lengths
#
#
# main()


import csv
import random

FILENAME = 'places.csv'


def load_places(filename):
    places = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                name, country, priority, visited = row
                places.append({
                    'name': name,
                    'country': country,
                    'priority': int(priority),
                    'visited': visited == 'v'
                })
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty list of places.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return places


def save_places(filename, places):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for place in places:
            writer.writerow([
                place['name'],
                place['country'],
                place['priority'],
                'v' if place['visited'] else 'n'
            ])


def display_places(places):
    sorted_places = sorted(places, key=lambda place: (place['visited'], place['priority']))

    count_unvisited = sum(1 for place in places if not place['visited'])

    max_name_length = max(len(place['name']) for place in sorted_places)
    max_country_length = max(len(place['country']) for place in sorted_places)

    for index, place in enumerate(sorted_places, start=1):
        visit_status = "*" if not place['visited'] else " "
        print(f"{visit_status}{index:>2}. {place['name']:<{max_name_length}} in {place['country']:<{max_country_length}} {place['priority']:>2}")

    print(f"{len(places)} places tracked. You still want to visit {count_unvisited} places.")


def add_place(places):
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

    new_place = {
        'name': name,
        'country': country,
        'priority': priority,
        'visited': False
    }
    places.append(new_place)
    print(f"{new_place['name']} in {new_place['country']} (priority {new_place['priority']}) added to Travel Tracker.")


def recommend_place(places):
    unvisited_places = [place for place in places if not place['visited']]
    if unvisited_places:
        place = random.choice(unvisited_places)
        print(f"Not sure where to visit next?")
        print(f"How about... {place['name']} in {place['country']}?")
    else:
        print("No places left to visit!")


def mark_place_as_visited(places):
    sorted_places = sorted(places, key=lambda place: (place['visited'], place['priority']))

    unvisited_places = [place for place in places if not place['visited']]

    if not unvisited_places:
        print("No unvisited places")
        return

    display_places(places)

    while True:
        try:
            place_number = int(input("Enter the number of a place to mark as visited: "))
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


def main():
    print("Travel Tracker 1.0 - by Guo Yuye")
    places = load_places(FILENAME)
    print(f"{len(places)} places loaded from {FILENAME}")

    while True:
        print(
            "Menu:\nD - Display all places\nR - Recommend a random place\nA - Add a new place\nM - Mark a place as visited\nQ - Quit")
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


main()
