# # დავალება 1


# numbers = []

# # მომხმარებლისგან 10 რიცხვის მიღება
# for i in range(10):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# # რიცხვების შემოწმება და ლუწი/კენტი ტიპის დაბეჭდვა
# for num in numbers:
#     if num % 2 == 0:
#         print(f"{num} is even.")
#     else:
#         print(f"{num} is odd.")


# # დავალება 2


# names = []

# # მომხმარებლისგან 5 სახელის მიღება
# for i in range(5):
#     name = input(f"Enter name {i+1}: ")
#     names.append(name)

# # სახელების სიმბოლოების რაოდენობის შემოწმება
# for name in names:
#     if len(name) > 5:
#         print(f"The name '{name}' consists of more than five letters.")


# # დავალება 3


# ჯანსაღი საკვები პროდუქტების სია
healthy_foods = ["apple", "banana", "carrot", "spinach", "almonds"]

# პირველი და ბოლო ელემენტის ამოშლა
healthy_foods.pop(0)  # ამოშლის პირველ ელემენტს
healthy_foods.pop()   # ამოშლის ბოლო ელემენტს

# განახლებული სიის დაბეჭდვა
print("Updated list:", healthy_foods)


# დავალება 4


def find_unique_element(numbers):
    
    sorted_numbers = sorted(numbers)
    
    if sorted_numbers[0] != sorted_numbers[1]:
        return sorted_numbers[0]
    
    elif sorted_numbers[-1] != sorted_numbers[-2]:
        return sorted_numbers[-1]
    
    else:
        for i in range(1, len(sorted_numbers) - 1):
            if sorted_numbers[i] != sorted_numbers[i-1] and sorted_numbers[i] != sorted_numbers[i+1]:
                return sorted_numbers[i]


numbers = [1, 1, 1, 2, 1]

unique_element = find_unique_element(numbers)
print(f"გამორჩეული ელემენტი: {unique_element}")