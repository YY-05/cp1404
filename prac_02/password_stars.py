# MINIMUM_LENGTH = 8
#
# password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
# while len(password) < MINIMUM_LENGTH:
#     password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
#
# print('*' * len(password))

MINIMUM_LENGTH = 8


def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password, ensuring it meets the minimum length requirement."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def print_asterisks(password):
    """Print as many asterisks as there are characters in the password."""
    print('*' * len(password))


main()
