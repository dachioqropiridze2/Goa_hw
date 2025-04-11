# დავალება 1

age = 20
if age >= 18:
    print("You are an adult.")


for i in range(1, 6):
    print(i)


i = 0
while i < 5:
    print(i)
    i += 1

# დავალება 2


for i in range(1, 6):
    print(i)


i = 0
while i < 5:
    print(i)
    i += 1


# დავალება 3


total = 0
for i in range(1, 11):
    total += i
print("The sum of numbers from 1 to 10 is:", total)


# დავალება 4


total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print("The sum of numbers from 1 to 10 is: ")


# დავალება 5


for i in range(2, 21, 2):
    print(i)


# დავალება 6


i = 31
while i < 70:
    print(i)
    i += 2



# დავალება 7


# Indexing (ინდექსირება) პითონში: Indexing პითონში ნიშნავს მოცემულ სერიაში (სიის, სტრიქონის, ტუუპლის და სხვა კოლექციების) კონკრეტული ელემენტის მისაღებად მისი პოზიციის მითითებას. თითოეული ელემენტს გააჩნია ინდექსი, რომელიც იწყება 0-დან.

# მაგალითად, სიის ინდექსები: [10, 20, 30]

# 0 ინდექსი აჩვენებს პირველ ელემენტს: 10

# 1 ინდექსი აჩვენებს მეორე ელემენტს: 20

# 2 ინდექსი აჩვენებს მესამე ელემენტს: 30


# დავალება 8


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input("შეიყვანეთ რიცხვი: "))
if is_prime(number):
    print(f"{number} არის მარტივი რიცხვი.")
else:
    print(f"{number} არ არის მარტივი რიცხვი.")



# დავალება 9


n = int(input("შეიყვანეთ რიცხვი: "))
total = sum(range(1, n + 1))
print(f"ჯამი 1-დან {n}-მდე რიცხვების არის: {total}")


# დავალება 10


# Flowchart-ის მიხედვით, თუ მომხმარებელი არის 14 წლის და არ არის სტუდენტი, პროგრამა მოითხოვს მისი ასაკის და სტატუსის შესამოწმებლად და, შესაბამისად, გამოიტანს შესაბამის შედეგს.

# მაგალითად:

age = int(input("გთხოვთ, შეიყვანოთ თქვენი ასაკი: "))
student = input("გხავთ სტუდენტი? (yes/no): ").lower()

if age == 14 and student == "no":
    print("თქვენ არ ხართ სტუდენტი და თქვენი ასაკი არის 14.")
else:
    print("შემდეგი შერჩევა.")
