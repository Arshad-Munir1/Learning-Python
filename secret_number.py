secret_number = 9
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess = int(input("what is your guess? "))
    guess_count =+1
    if guess == secret_number:
        print("you guessed right!")
        break