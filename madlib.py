# At least 2 strings
# At least 2 numbers
# And includes the following elements:
#
# One list/array
# One if statement with at least one logical operator
# One function
#   Must return a value
#   Must have and use parameters
# One loop


# And meet the following requirements:
#
# The mad lib's code must be well commented.
# Comments should explain code, not just label.
# All elements should have a purpose within the greater madlib.
# (In other words you can't create an array or function that isn't used)
# You must make required number meaningful commits to this file in your repository
# Any errors will earn an automatic ZERO on this assignment.
# Your mad lib should print out the entire story to the console.

# Mad Lib:
# There was a place were NOUN changed the way people ate their food.
# One day NAME ate NUMBER1 FOOD that made NAME very ill for NUMBER2 days.
# NAME , has never eaten FOOD again.

userMadLibList = []

print "Give me a noun."
userMadLibList.append(raw_input())

while len(userMadLibList) != 5:
    for i in range(len(userMadLibList)):
        if len(userMadLibList) == 0:
            print "You didn't answer the first question!"
            userMadLibList.append(raw_input())
        elif len(userMadLibList) == 1:
            print "What's your name?"
            userMadLibList.append(raw_input())
        elif len(userMadLibList) == 2:
            print "Give me a number."
            userMadLibList.append(raw_input())
        elif len(userMadLibList) == 3:
            print "What's your favorite food?"
            userMadLibList.append(raw_input())
        elif len(userMadLibList) == 4:
            print "Give me another number."
            userMadLibList.append(raw_input())

print userMadLibList