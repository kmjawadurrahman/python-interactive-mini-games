# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == 'rock':
        number = 0;
    elif name == 'Spock':
        number = 1;
    elif name == 'paper':
        number = 2;
    elif name == 'lizard':
        number = 3;
    elif name == 'scissors':
        number = 4;
    else:
        print 'Invalid name!'
    return number

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        name = 'rock';
    elif number == 1:
        name = 'Spock';
    elif number == 2:
        name = 'paper';
    elif number == 3:
        name = 'lizard';
    elif number == 4:
        name = 'scissors';
    else:
        print 'Number is not in correct range!'
    return name

    # convert number to a name using if/elif/else
    # don't forget to return the result!


def rpsls(player_choice):
    # delete the following pass statement and fill in your code below
    print ""
    print 'Player chooses ' + player_choice
    player_number = name_to_number(player_choice);
    comp_number = random.randrange(0,5);
    comp_choice = number_to_name(comp_number);
    print 'Computer chooses ' + comp_choice
    result = (comp_number - player_number) % 5;
    if result == 1 or result == 2:
        print 'Computer wins!'
    elif result == 3 or result == 4:
        print 'Player wins!'
    else:
        print 'Player and computer tie!'


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
