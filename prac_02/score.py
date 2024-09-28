# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# elif score >= 90:
#     print("Excellent")
# elif score >= 50:
#     print("Passable")
# else:
#     print("Bad")

import random


def main():
    """Get user score, validate it, and print the result."""
    score = float(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid score")
    else:
        result = determine_status(score)
        print(result)

    random_score = random.randint(0, 100)
    random_result = determine_status(random_score)
    print(f"The random score is {random_score} and the result of random score is {random_result}")


def determine_status(score):
    """Determine the status of a given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
