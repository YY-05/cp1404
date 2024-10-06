# 1.
name = input("What is your name? ")
with open("name.txt", "w") as out_file:
    out_file.write(name)

# 2.
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", "w") as file:
    file.write("17\n42\n400\n")

with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
