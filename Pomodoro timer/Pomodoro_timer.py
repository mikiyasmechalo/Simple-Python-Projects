from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bd9ac"
# YELLOW = "#f7f5dd"
YELLOW = "#6b6b6b"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
count_timer = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(count_timer)
    canvas.itemconfig(timer, text='00:00')
    label.config(text='Timer')
    check_mark.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def raise_above_all(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


def start_timer():
    raise_above_all(window)
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label.config(text='BBreak', fg=RED, font=(FONT_NAME, 50, 'bold'))
        countdown(long_break_time)
    elif reps % 2 == 0:
        label.config(text='Break', fg=PINK, font=(FONT_NAME, 50, 'bold'))
        countdown(short_break_time)
    else:
        label.config(text='Work', fg=GREEN, font=(FONT_NAME, 50, 'bold'))
        countdown(work_time)
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    # if count == LONG_BREAK_MIN * 60:
    #     marks = 'fffffffff'
    #     check_mark.config(text=marks)

    count_min = math.floor(count / 60)
    count_sec = count % 60

    global reps
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global count_timer
        count_timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(reps / 2)):
            marks += '✔'
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=110, pady=80, bg=YELLOW)
window.title("Pomodoro Timer")
window.minsize(512, 500)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file='C:/Users/mikiy/Desktop/tomato.png')
canvas.create_image(100, 112, image=tomato_pic)
timer = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 50, 'bold'), bg=YELLOW)
label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer, height=2, width=5, bg='#808080', fg='#ffffff')
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer, height=2, width=5, bg='#707070', fg='#ffffff')
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
