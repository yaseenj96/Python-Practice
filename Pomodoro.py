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
clock = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(clock)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer.config(text="Work")
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clock
        clock = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50)

canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103,112, image = tomato_img)
timer_text = canvas.create_text(103,130,text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(row=1,column=1)


timer = Label(fg=GREEN, text="Timer",font=(FONT_NAME,50))
timer.grid(row=0,column=1)
start = Button(text="Start", command=start_timer)
start.grid(row=2,column=0)
reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2,column=2)
checkmark = Label(fg=GREEN)
checkmark.grid(row=3,column=1)
window.mainloop()
