score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# elif score >= 90:
#     print("Excellent")
# elif score >= 50:
#     print("Passable")
# else:
#     print("Bad")


# Note boundary conditions (50 should be a pass, not > 50)
# Note efficiency and nesting; use the fewest number of if/elif as possible

def main():
    """Get a numeric score and display its status."""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
