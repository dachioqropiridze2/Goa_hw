# დავალება 4


# Get a sentence from the user
sentence = input("Enter a sentence: ")

# 1. All lowercase letters
print("Lowercase:", sentence.lower())

# 2. All uppercase letters
print("Uppercase:", sentence.upper())

# 3. First letter uppercase, the rest lowercase
print("Capitalized:", sentence.capitalize())


# დავალება 5


def format_sentence():
    # Get a sentence from the user
    sentence = input("Enter a sentence: ")
    
    # Print the sentence in different formats
    print("Lowercase:", sentence.lower())
    print("Uppercase:", sentence.upper())
    print("Capitalized:", sentence.capitalize())

# Call the function
format_sentence()