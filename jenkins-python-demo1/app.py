import random

def guess_number():
    number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess a number (1-10): "))
        attempts += 1
        if guess < number:
            print("Too low 🚀")
        elif guess > number:
            print("Too high 🔥")
        else:
            print(f"🎉 Correct! You guessed in {attempts} attempts")
            break

guess_number()
