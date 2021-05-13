from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(time)
    canvas.itemconfig(timer_value, text="00:00")
    timer.config(text="TIMER")
    check.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def set_timer():
    global reps, time
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer.config(text="LONG BREAK", fg=RED)
        counter(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="SHORT BREAK", fg=PINK)
        counter(short_break_sec)
    else:
        timer.config(text="WORKING")
        counter(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def counter(count):
    global time
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'
    canvas.itemconfig(timer_value, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        time = window.after(1000, counter, count - 20)
    else:
        set_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔'
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('POMODORO')
window.config(padx=100, pady=50, bg=YELLOW)

# Create Label
timer = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'bold'))
timer.grid(column=1, row=0)
# Create Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Get Image
img = PhotoImage(file='tomato.png')
# Create Image
canvas.create_image(100, 112, image=img)
timer_value = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

# Start Button
start = Button(text='Start', highlightthickness=0, command=set_timer)
start.grid(column=0, row=2)

# Reset Button
reset = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

# Check Symbol
check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
check.grid(column=1, row=3)
window.mainloop()
