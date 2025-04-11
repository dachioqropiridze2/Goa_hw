# დავალება 1


# მთავარი მიზეზები, რატომ ვიყენებთ ფუნქციებს:
# კოდის გამეორების თავიდან აცილება:

# როცა ერთსა და იმავე მოქმედებას ბევრჯერ ვაკეთებთ, ჯობია ამისთვის ფუნქცია შევქმნათ და ყველგან გამოვიყენოთ.

# მაგ: თუ ორჯერ უნდა ვიპოვოთ ორი რიცხვის ჯამი, ჯობს sum(a, b) ფუნქცია გავაკეთოთ და ვიძახებდეთ.

# კოდის სისუფთავე და გასაგებლობა:

# ფუნქციები კოდს აწყობილს და წაკითხვადს ხდის. იცი ზუსტად, რომელმა ფუნქციამ რა გააკეთა.

# გადამუშავება (Reuse):

# ერთხელ დაწერილი ფუნქცია შეგვიძლია სხვადასხვა ადგილას გამოვიყენოთ. ეს ზოგავს დროსაც და ძალისხმევასაც.

# შეცდომების პოვნა (debugging) უფრო მარტივია:

# როცა კოდი ნაწილებადაა დაყოფილი (ფუნქციებში), შეცდომის პოვნა და გამოსწორება გაცილებით მარტივია.

# მარტივად გასაზრდელი კოდი:

# თუ პროექტი გაიზარდა, ფუნქციების დახმარებით მარტივად შეგვიძლია ახალი ფუნქციონალის დამატება.


# დავალება 3


def double_values(arr):
    return [x * 2 for x in arr]


print(double_values([1, 2, 3]))


# დავალება 4


def even_numbers(arr):
    return [x for x in arr if x % 2 == 0]

print(even_numbers([1, 2, 3, 4, 5, 6]))  


# დავალება 5


def square_values(arr):
    return [x ** 2 for x in arr]


print(square_values([1, 2, 3]))  


# დავალება 6


def filter_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char in vowels])

print(filter_vowels("hello world"))


# დავალება 7


def negative_numbers(arr):
    return [x for x in arr if x < 0]

print(negative_numbers([1, -2, 3, -4, 5]))


# დავალება 8


def positive_numbers(arr):
    return [x for x in arr if x > 0]

print(positive_numbers([1, -2, 3, -4, 5]))


# დავალება 9


def power(x, y):
    return x ** y

print(power(2, 3))