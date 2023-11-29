# task 9
import string
import random

print("Welcome to the My Password Generator")

def get_user_input():
    while True:
        try:
            characters_number = int(input("Choose the length of your password : "))
            if characters_number < 5:
                print("Your number should be at least 5.")
            else:
                return characters_number
        except ValueError:
            print("Please enter numbers only.")

def generate_password(length):
    
    d1 = list(string.ascii_lowercase)
    d2 = list(string.ascii_uppercase)
    d3 = list(string.digits)
    d4 = list(string.punctuation)

    # shuffle lists
    random.shuffle(d1)
    random.shuffle(d2)
    random.shuffle(d3)
    random.shuffle(d4)

    # calculate the number of characters
    part1 = round(length * (30 / 100))
    part2 = round(length * (20 / 100))

    
    result = []

    # Use random.sample 
    result.extend(random.sample(d1, part1))
    result.extend(random.sample(d2, part1))
    result.extend(random.sample(d3, part2))
    result.extend(random.sample(d4, part2))

    # final result
    random.shuffle(result)

    # join result
    password = "".join(result)
    return password

# Execute the program
characters_number = get_user_input()
password = generate_password(characters_number)
print("Strong Password:", password)
