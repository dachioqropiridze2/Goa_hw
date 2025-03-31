#დავალება 1

#a = false
#b = false
#a and b = false
#a or b = false

#a = false
#b = true
#a and b = false
#a or b = true

#a = true
#b = true
#a and b = true
#a or b = true

#დავალება 2


print(True and False or True or True and False)   #true

#დავალება 3


num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if num1 == num2:
    print(True)
else: print(False)


#დავალება 4


score = int(input("enter your score: "))

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 70 and score < 90:
    print("Grade B")
elif score >= 50 and score < 70:
    print("Grade C")
elif score <= 0 or score > 100:
    print("ERROR")
else: print("Grade F")


#დავალება 5


number = int(input("enter number: "))

if number %2 == 0 and number > 10:
    print(True)
else: print(False)





