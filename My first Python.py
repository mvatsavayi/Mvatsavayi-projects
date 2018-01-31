# Mahit Vatsavayi
# 10/11/17
# Makes siily sentences like mad lib
print("*" * 48)
print(" * Welcome to the duck word generator 3001 * ")
print("*" * 48)
# getting the player's name
player_name= input("Please enter a username:")

# + can also add or join strings together
message = "Bello, " + player_name + "! Let's make a duckie sentance or word!"
print (message.upper())

# gather input from user
famous_person = input("Enter a name of a football player")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
verb = input("Enter a verb ending in -ING: ")

silly_sentence = ("The " + adjective1 + " " + player_name + " is "
                  + verb + " the " + adjective2 + " " + famous_person)
print (silly_sentence)
                  




