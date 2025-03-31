# while ციკლი იმუშავებს, სანამ მოცემული პირობა True იქნება
counter = 1  # ცვლადს საწყისი მნიშვნელობა 1 ეძლევა

while counter <= 5:  # თუ counter უფრო მცირეა ან უდრის 5-ს
    print(counter)  # გამოგვიტანს ამ ცვლადის მნიშვნელობას
    counter += 1  # მაშინ რაც უფრო დიდი იქნება counter-ს 


#დავალება 3


# # for loop: გამოიყენება მაშინ, როცა იცით რამდენი ჯერ უნდა შესრულდეს ციკლი
# for i in range(1, 6):
#     print(i)

# # while loop: გამოიყენება მაშინ, როცა არ ვიცით ციკლის დასრულების დრო და მანამდე უნდა გაჩერდეს, სანამ გარკვეული პირობა არ შესრულდება
# counter = 1
# while counter <= 5:
#     print(counter)
#     counter += 1


#დავალება 4


# # განსაზღვრული პაროლი
# correct_password = "password123"

# # მომხმარებლის პაროლის მიღება და ციკლის დაწყება
# user_password = input("Enter your password: ")

# # while ციკლი, რომელიც ხელს უშლის მომხმარებელს პაროლის შეყვანას, სანამ არ შეუსაბამებს
# while user_password != correct_password:
#     print("Incorrect password. Try again.")
#     user_password = input("Enter your password: ")

# # სწორი პაროლის შეყვანის შემდეგ გამოდის შეტყობინება
# print("Correct password. You have successfully logged in.")


#დავალება 5

 #while ციკლი, რომელიც ბეჭდავს რიცხვებს 1-დან 20-მდე, ორ-ორი ნაბიჯით
number = 1
while number <= 20:
    print(number)
    number += 2  # ყოველ ჯერზე რიცხვი იზრდება ორით


#დავალება 6