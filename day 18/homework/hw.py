# დავალება 1


# len()

# type()

# int()

# str()

# input()

# print()

# sum()

# max()

# min()

# count()


# დავალება 2


print(len("Hello"))
print(len([1, 2, 3, 4]))


print(type(5))              
print(type("Python"))       


print(int("5"))             
print(int(3.7))             


print(str(123))             
print(str(True))            


name = input("Enter Your Name: ")
print("welcome in", name)


print("Hello World")
print("Sum is", 2 + 2)


print(sum([1, 2, 3]))       
print(sum(range(5)))


print(max([3, 9, 1]))        
print(min([3, 9, 1]))  



# დავალება 3


def my_len(data):
    count = 0
    for _ in data:
        count += 1
    return count


def my_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def my_max(lst):
    max_value = lst[0]
    for x in lst:
        if x > max_value:
            max_value = x
    return max_value


# დავალება 4


numbers = [3, 7, 3, 2, 3]

choice = int(input("Choose a number from the list: "))

count = numbers.count(choice)

print(f"The number {choice} appears {count} time(s) in the list.")


# დავალება 5


items = ["apple", "banana", "cherry", "grape", "mango"]

answer = input("Do you want to clear the list? (yes/no): ")

if answer.lower() == "yes":
    items.clear()
    print("List cleared:", items)
else:
    print("List unchanged:", items)


# დავალება 6


fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

index = int(input("Enter the index of the fruit you want to remove (starts from 0): "))

if 0 <= index < len(fruits):
    fruits.pop(index)
    print("Updated list:", fruits)
else:
    print("Invalid index.")