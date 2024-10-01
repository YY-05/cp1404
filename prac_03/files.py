name = input("Name: ")
out_file = open("name.txt", "w")
while name != "":
    out_file.write(name + "\n")
    name = input("Name: ")
out_file.close()

in_file = open("name.txt", "r")
print(in_file.read())
in_file.close()
print("Hi [name]!")

with open('numbers.txt', 'r') as file:
    sum_of_first_two = 0
    for _ in range(2):
        number = int(file.readline().strip())
        sum_of_first_two += number
    print(sum_of_first_two)

total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line.strip())
print(total)
