import random

n = random.randrange(1, 10)
guess = int(input("Enter Number: "))
while n != guess:
    if guess < n:
        print("too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("too high")
        guess = int(input("Enter number again: "))
    else:
        break
print("you guessed it right")
