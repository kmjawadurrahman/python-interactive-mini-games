# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

which_range = ""

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global guess_count
    global which_range
    global secret_number
    guess_count = 7
    which_range = 0
    secret_number = random.randrange(0,100)
    print "New game. Range is from 0 to 100"
    print "Number of guesses remaining is", guess_count
    print ""

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global guess_count
    global which_range
    global secret_number
    guess_count = 9
    which_range = 1
    secret_number = random.randrange(0,1000)
    print "New game. Range is from 0 to 1000"
    print "Number of guesses remaining is", guess_count
    print ""

def input_guess(guess):
    # main game logic goes here
    global guess_count
    guess_count -= 1
    guess_ = int(guess)
    print "Guess was", guess_
    print "Number of guesses remaining is", guess_count
    if guess_ < secret_number:
        print "Higher"
        print ""
    elif guess_ > secret_number:
        print "Lower"
        print ""
    else:
        print "Correct"
        print ""
        if which_range:
            range1000()
        else:
            range100()
    if guess_count <= 0:
        print "You ran out of guesses. The number was", secret_number
        print ""
        if which_range:
            range1000()
        else:
            range100()

# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game
new_game()


# always remember to check your completed program against the grading rubric
