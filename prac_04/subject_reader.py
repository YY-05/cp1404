"""
CP1404/CP5632 Practical
Data file -> lists program
"""

# FILENAME = "subject_data.txt"
#
#
# def main():
#     data = load_data()
#     print(data)
#
#
# def load_data():
#     """Read data from file formatted like: subject,lecturer,number of students."""
#     input_file = open(FILENAME)
#     for line in input_file:
#         print(line)  # See what a line looks like
#         print(repr(line))  # See what a line really looks like
#         line = line.strip()  # Remove the \n
#         parts = line.split(',')  # Separate the data into its parts
#         print(parts)  # See what the parts look like (notice the integer is a string)
#         parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
#         print(parts)  # See if that worked
#         print("----------")
#     input_file.close()
#
#
# main()


FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        subjects.append(list(parts))
        print("----------")
    input_file.close()
    return subjects


def display_subject_details(subjects):
    """Display subject details."""
    for i in range(len(subjects)):
        print(f"{subjects[i][0]} is taught by {subjects[i][1]} and has {subjects[i][2]} students")


main()
