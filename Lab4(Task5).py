from random import randint

secret = randint(0, 1000)
print("I have chosen a number between 0 and 1000. Try to guess it!")

while True:
    guess = input("Your guess: ")  # Asking the user for their guess
    try:
        guess = int(guess)
        if guess > secret:
            print("Try a smaller number (<)")
        elif guess < secret:
            print("Try a larger number (>)")
        else:
            print("Congratulations! You guessed it!")
            break
    except ValueError:
        print("Please enter a valid whole number.")

