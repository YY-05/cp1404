import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main function to run the guitar program."""
    guitars = load_guitars()
    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    print("\nEnter new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)


def load_guitars():
    """Load guitars from the CSV file and return a list of Guitar objects."""
    guitars = []
    with open(FILENAME, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


if __name__ == '__main__':
    main()
