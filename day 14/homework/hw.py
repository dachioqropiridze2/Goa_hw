# 1) ცვლადში შეინახეთ თქვენი სახელი. შემდეგ ინდექსინგის მეშვეობით ეკრანზე გამოიტანეთ სტრინგიდან ყველა ის ასო, რომელიც არის ხმოვანი.

my_name = "YourNameHere"  # მოაყოლეთ თქვენი სახელი
vowels = "AEIOUaeiou"
for letter in my_name:
    if letter in vowels:
        print(letter)


# 2) Strings are mutable, Lists are immutable.
# პასუხი: False.
# სტრინგები (strings) არიან immutable, ანუ მათი მნიშვნელობა არ შეიძლება შეიცვალოს, ხოლო სიები (lists) არიან mutable, 
# რაც ნიშნავს, რომ სიების ელემენტები შეიძლება შეიცვალოს.


# 3) პასუხი: სტრინგები (strings) პითონში immutable-ია, ხოლო სიები (lists) mutable-ია.


# 4) ცვლადში შეინახეთ ცარიელი სია. input-ის მეშვეობით მომხმარებელს შემოატანინეთ ინფორმაცია საკუთარი თავის შესახებ.

user_info = []
user_info.append(input("შეიყვანეთ თქვენი სახელი: "))
user_info.append(input("შეიყვანეთ თქვენი გვარი: "))
user_info.append(input("შეიყვანეთ თქვენი ასაკი: "))
user_info.append(input("შეიყვანეთ თქვენი დაბადების თარიღი: "))
user_info.append(input("შეიყვანეთ თქვენი სიმაღლე: "))
user_info.append(input("შეიყვანეთ თქვენი ადგილმდებარეობა: "))
user_info.append(input("შეიყვანეთ თქვენი პროფესია: "))
user_info.append(input("შეიყვანეთ თქვენი ჰობი: "))

print(user_info)


# 5) დაასრულეთ საკლასო დავალებები. (ეცადეთ თქვენით გააკეთოთ სანამ ჩანაწერს გადახედავთ ):

# • მომხმარებელს შემოატანინეთ 10 მნიშვნელობა სიაში (For loop-ის მეშვეობით. ) შემდეგ გამოიყენეთ კიდევ ერთი for loop, გადაუარეთ თითოეულ სიის ელემენტს და შამოწმეთ ეს რიცხვები ლუწია თუ კენტი.

numbers = []
for i in range(10):
    number = int(input(f"შეიყვანეთ რიცხვი {i+1}: "))
    numbers.append(number)

for num in numbers:
    if num % 2 == 0:
        print(f"{num} არის ლუწი.")
    else:
        print(f"{num} არის კენტი.")


# • მომხმარებელს შემოატანინეთ 5 სახეთი, შემდეგ კი კიდევ ერთი for loop გამოიყენეთ რათა გაიგოთ ამ სახელებში სიმბოლოების რაოდენობა აღემატება თუ არა 5-ს.

names = []
for i in range(5):
    name = input(f"შეიყვანეთ სახელი {i+1}: ")
    names.append(name)

for name in names:
    if len(name) > 5:
        print(f"{name} consists of more than five letters.")


# • შექმენით სია, რომელშიც დაამატებთ ჯანსაღ საკვებ პროდუქტებს. (იყოს მინიმუმ 5 პროდუქტი). 
# ამოშალეთ სიის პირველი და ბოლო ელემენტები და ტერმინალში დაბეჭდეთ სიის განახლებული ვერსია.

healthy_foods = ["apple", "banana", "carrot", "spinach", "almonds"]
del healthy_foods[0]  # წაშლით პირველ ელემენტს
del healthy_foods[-1]  # წაშლით ბოლო ელემენტს
print(healthy_foods)


# • შექმენით რიცხვების სია, რომელშიც მინიმუმ გექნებათ 5 ელემენტი. ამ 5 ელემენტიდან 1 განსხვავებული ელემენტი იქნება. 
# ეს ელემენტი უნდა იყოს მოთავსებული დაახლოების სიის შუაში. (არ უნდა იყოს სიის დასაწყისში ან დასასრულში). 
# თქვენი დავალებაა დაწეროთ პროგრამა და იპოვოთ ეს განსხვავებული ელემენტი მოცემულ სიაში. (მინიშნება: სიის დალაგება)

numbers_list = [1, 2, 3, 5, 4]
numbers_list.sort()  # დაალაგებთ სიას
different_element = None

for i in range(1, len(numbers_list)-1):
    if numbers_list[i] != numbers_list[i-1] and numbers_list[i] != numbers_list[i+1]:
        different_element = numbers_list[i]
        break

print(f"განifferებული ელემენტი არის: {different_element}")
