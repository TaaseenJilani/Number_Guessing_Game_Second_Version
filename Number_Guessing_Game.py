import random
print("Welcome to this number guessing game where you will be guessing a number between 1 to 100. You have to guess the number in less than 7 tries.")
guess = int(input("Please enter your guess: "))
number = random.randint(1, 101)
num_of_guesses = 1
while num_of_guesses < 7:
    num_of_guesses += 1
    if guess > number:
        print("Your guess is too high. Please try again.")
    elif guess < number:
        print("Your number is too low. Please try again.")
    guess = int(input("Please enter your guess: "))
    if guess == number:
        break

if guess == number:
    print("You are correct! The number is %d. You got it in %d tries. Thanks for playing!" % (number, num_of_guesses))
if guess != number:
     print("Unlucky. You couldn't guess the number withing 7 tries. The correct number was %d." % number)