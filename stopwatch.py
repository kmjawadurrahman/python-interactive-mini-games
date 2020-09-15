# template for "Stopwatch: The Game"
import simplegui
# define global variables

t=0
time="0:00.0"
tries=0
wins=0
begin=False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    A=(t/10/60)
    B=int((((t/10)%60))/10)
    C=int(((t/10)%60)%10)
    D=t%10
    time =str(A)+":"+str(B)+str(C)+"."+str(D)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global begin
    begin=True

def stop():
    timer.stop()
    global tries, wins, begin
    if begin:
        if t%10==0:
            wins+=1
        begin=False
        tries+=1

def reset():
    global t, begin, tries, wins
    begin=False
    tries=0
    wins=0
    timer.stop()
    t=0
    format(t)

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t+=1
    format(t)

# define draw handler
def draw(canvas):
    canvas.draw_text(time, [100,160], 40, "Red")
    canvas.draw_text(str(wins)+"/"+str(tries), [250,30], 30, "Black")

# create frame
frame = simplegui.create_frame("Stopwatch - The Game", 300, 300)
frame.set_canvas_background("Pink")

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)
# start frame
frame.start()

# Please remember to review the grading rubric
