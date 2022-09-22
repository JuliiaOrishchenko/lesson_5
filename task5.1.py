import random

while True:
    computer_digit = random.randint(1, 10)
    user_digit = int(input("Enter digit from 1 to 10: "))
    if computer_digit == user_digit:
        print("You guessed it!!!")
    else:
        print("You have not guessed")
