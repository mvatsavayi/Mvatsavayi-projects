# Mahit Vatsavayi
# 10/18/2017
# Norweign Blue Guessing Game
# A guessing Game
import random



print("*" * 80)
print(" BELLO! WELCOME TO THE NORWEIGEN BLUE DUCK CHALLANGE")
print("*" * 80)

instructions = """ You walk into the pet shop seeking for the rare
Norweign duck. It is the pet you want. The clerk says you get 5 guesses to guess the age
  of the Duck. Then you may take it home for free!!!!!!!!

  Remember Only 5 guesses! """

print(instructions)

# Make up the ducks age
duck_age = random.randint(1,20)

# Set the number of guesses to 0
number_of_guesses = 0


while number_of_guesses < 6:
    # Get a guess from the user
    guess = input("GUESS THE AGE OF THE DUCK!! [1 to 20]:")
    guess = int(guess) # this is a string that converts an integer and puts it into box
    number_of_guesses = number_of_guesses + 1
    print(number_of_guesses)
    if guess == duck_age:
        print("YOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU WIN")
        break
    else:
        if guess < duck_age:
            print("Too Low")
        else:
            print("Too High")
        print("You are a wrong duck, but try again, even though you are the worst person in the entire world you duckie duckie duck")
print("Gracias for playing you duckie duckie duck. The duck was not even a parrot. The number was" , duck_age, "years old.")

