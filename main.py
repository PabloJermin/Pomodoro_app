from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reseting():
    window.after_cancel(timer)
    global time_label
    time_label.config( text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
    canvas.itemconfig(time_counter, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    w_sec = WORK_MIN * 60
    short_br_sec = SHORT_BREAK_MIN * 60
    l_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(l_break)
        time_label.config(text="Long Break", fg= GREEN)
    elif reps % 2 == 0:
        count_down(short_br_sec)
        time_label.config(text="Short Break", fg=PINK)
    else:
        count_down(w_sec)
        time_label.config(text="Work Session", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    minits = math.floor(count / 60)
    secs = count % 60

    if secs == 0 or secs < 10:
        secs = f"0{secs}"

    canvas.itemconfig(time_counter, text=f"{minits}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            mark += "¤"
        check_label.config(text=mark)


        # if reps % 2 == 0:
        #     f_row = 3
        #     check_label.config(text="¤")
        #     check_label.grid(row=f_row, column=1)
        #     f_row += 1


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Task Time keeper")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200,  height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_counter = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



# ------------TIME LABEL-------------- #
time_label = Label( text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
time_label.grid(row= 0, column=1)



# -------------START BUTTON----------#
start_btn = Button(text="Start", font=(FONT_NAME, 15, "bold"), bg=YELLOW, command=start_timer)
start_btn.grid(row=2, column=0)



# ---------------RESET BUTTON -----------#
reset_btn = Button(text="Reset", font=(FONT_NAME, 15, "bold"), bg=YELLOW, command=reseting)
reset_btn.grid(row=2, column=2)


# --------------CHECK LABEL----------#
check_label = Label( font=(20), bg=YELLOW)
check_label.grid(row= 3, column=1)


window.mainloop()