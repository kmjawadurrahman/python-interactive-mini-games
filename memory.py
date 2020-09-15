# implementation of card game - Memory

import simplegui
import random

l1=['http://www.clker.com/cliparts/h/D/n/I/R/j/pink-female-stick-figure-th.png',
    'http://www.clker.com/cliparts/2/6/e/6/12065597661119442474nicubunu_Stick_figure_female_2.svg.thumb.png',
    'http://www.clker.com/cliparts/w/g/6/l/o/P/green-stick-figure-girl-th.png',
    'http://www.clker.com/cliparts/F/V/J/y/R/V/woman-th.png',
    'http://www.clker.com/cliparts/E/Z/s/2/B/p/purple-stick-man-th.png',
    'http://www.clker.com/cliparts/3/I/E/d/A/2/turquoise-stick-figure-th.png',
    'http://www.clker.com/cliparts/S/L/2/7/i/r/stick-man-red-th.png',
    'http://www.clker.com/cliparts/r/6/N/B/r/E/blue-stick-man-th.png']

l2=['http://www.clker.com/cliparts/h/D/n/I/R/j/pink-female-stick-figure-th.png',
    'http://www.clker.com/cliparts/2/6/e/6/12065597661119442474nicubunu_Stick_figure_female_2.svg.thumb.png',
    'http://www.clker.com/cliparts/w/g/6/l/o/P/green-stick-figure-girl-th.png',
    'http://www.clker.com/cliparts/F/V/J/y/R/V/woman-th.png',
    'http://www.clker.com/cliparts/E/Z/s/2/B/p/purple-stick-man-th.png',
    'http://www.clker.com/cliparts/3/I/E/d/A/2/turquoise-stick-figure-th.png',
    'http://www.clker.com/cliparts/S/L/2/7/i/r/stick-man-red-th.png',
    'http://www.clker.com/cliparts/r/6/N/B/r/E/blue-stick-man-th.png']

l = l1 + l2
li = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tracker1 = 0
tracker2 = 0
idx1 = 0
idx2 = 0
newgame = 1
turns = 0

random.shuffle(l)
image2 = 'http://www.silent9.com/blog/uploads/gimp/2source.png'
# helper function to initialize globals
def new_game():
    global state, newgame, li, turns
    state = 0
    newgame = 1
    turns = 0
    random.shuffle(l)
    label.set_text("Turns = " + str(turns))
    li = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, tracker1, tracker2, idx1, idx2, newgame, turns
    for i in range(16):
        if pos[0] >= 0 + 50*i-1 and pos[0] <= 49 + 50*i-1 and not li[i]:
            if newgame:
                if state == 0:
                    li[i] = 1
                    state = 1
                    tracker1 = l[i]
                    idx1 = i

                elif state == 1:
                    li[i] = 1
                    state = 2
                    tracker2 = l[i]
                    idx2 = i
                    turns += 1
                    label.set_text("Turns = " + str(turns))
                elif state == 2:
                     if tracker1 != tracker2:
                        li[idx1] = 0
                        li[idx2] = 0
                     li[i] = 1
                     state = 1
                     tracker1 = li[i]
                     idx1 = i
                     newgame = 0

            else:
                if state == 1:

                    li[i] = 1
                    state = 2
                    tracker2 = l[i]
                    idx2 = i
                    turns+=1
                    label.set_text("Turns = " + str(turns))

                elif state == 2:
                    if tracker1 != tracker2:
                        li[idx1] = 0
                        li[idx2] = 0
                    li[i] = 1
                    tracker1 = l[i]
                    idx1 = i
                    state =  1




# cards are logically 50x100 pixels in size
def draw(canvas):
    for i in range(16):
        image_i = simplegui.load_image(l[i])
        if not li[i]:
            canvas.draw_image(image, (50/2, 100/2), (50, 100), (50/2 + 50*i ,100/2), (50, 100))
        else:
            canvas.draw_image(image_i,  (50/2, 100/2), (50, 100), (25 + 50*i ,100/2), (50, 100))

image = simplegui.load_image(image2)

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
