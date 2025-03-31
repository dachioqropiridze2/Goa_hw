
sum_numbers = 0

for i in range(10):
    number = int(input(f"Please enter number {i+1}: "))
    sum_numbers += number


average = sum_numbers / 10


print(f"Sum of the numbers: {sum_numbers}")
print(f"Average: {average}")

