import random
number_of_guesses = 0
number = random.randint(10,25)

name = input("Welcome, may I know your name?")
print("Excellent " + name + " , Can you guess the number i chose from 10 to 25?\n")

while True:
    guess = int(input("guess a number : "))
    number_of_guesses += 1
    if guess == number:
        print("Bravo , You guessed right :)")
        print("You have tried to guess correctly" , number_of_guesses , "times")
        break
    else:
        if guess < number:
            print("Oops , please guess a higher number")
        else:
            print("Oops , please guess a lower number")
        continue
