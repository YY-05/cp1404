import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main function to run the guitar program."""
    # Load guitars from the file
    guitars = load_guitars()
    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)


if __name__ == '__main__':
    main()
