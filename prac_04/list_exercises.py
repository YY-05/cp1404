NUMBER_OF_NUMBERS = 5
num_numbers = 1
total = 0
the_numbers = []
while num_numbers <= 5:
    number = int(input("Number: "))
    the_numbers.append(number)
    num_numbers += 1
    total += number
print(f"The first number is {the_numbers[0]}")
print(f"The last number is {the_numbers[-1]}")
print(f"The smallest number is {min(the_numbers)}")
print(f"The largest of the number is {max(the_numbers)}")
print(f"The average of the numbers is {total / NUMBER_OF_NUMBERS}")

