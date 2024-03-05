import random
secret_number = random.randint(1,10)
print("Guess a number from 1 to 10. You have 5 attemps.")
print(secret_number)
for attemp in range(5):
    valid = False # flag
    while not valid:
        guess = int(input(f"#{attemp+1} Guess a number : "))
        if guess < 0 or guess >10:
            print("Invalid guess. Please retry the number 1 to 10")
        else:
            valid = True

    if guess > secret_number:
        print("Your number is too high. Please retry")
    elif guess < secret_number:
        print("Your number is too low. Please retry")
    else:
        print(f"You have won the game !!! The secret number is {secret_number}")
        break
if guess != secret_number:
    print("Sorry, you ran out of attempts. The number was", attemp+1)