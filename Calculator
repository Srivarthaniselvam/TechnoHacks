#Task 1

import tkinter as tk
from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clr():
    global expression
    expression = ""
    equation.set("")

def them():
    fg_col = "dark blue"
    bg_col = "light blue"

    disp.config(fg=fg_col, bg=bg_col)
    for button in buttons:
        button.config(bg=bg_col, fg=fg_col)

fg_col = "black"
bg_col = "white"

root = tk.Tk()
root.geometry("500x600")
root.title(" My Calculator")


frame0 = Frame(root)
Label(frame0, text="Simple Calculator", font="Helvetica 24 bold italic").pack()

frame0.pack(fill=X, ipadx=10, pady=12, padx=40)

equation = StringVar()


# frame1 
frame1 = Frame(root)
disp = Entry(frame1, font="Calibri 16 bold", textvariable=equation)
disp.pack(fill=X, ipadx=10, pady=12, padx=40)
disp.config(fg="black", bg="light blue")
frame1.pack(fill=X)

# frame2
frame2 = Frame(root)
Label(frame2, text=" ", font="times 8 bold").pack()
frame2.pack()

# Buttons
# frame3
frame3 = Frame(root)
button_texts = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '.', '0', '=', '/'
]

buttons = []

for i, text in enumerate(button_texts):
    row_num = i // 4 + 2
    col_num = i % 4
    button = Button(frame3, text=f' {text} ', fg=fg_col, bg=bg_col,
                    command=lambda t=text: press(t) if t != '=' else equal(),
                    height=4, width=12)
    button.grid(row=row_num, column=col_num)
    buttons.append(button)

frame3.pack()

# Clear button

frame4 = Frame(root)
clear_button = Button(frame4, text=' Clear ', fg=fg_col, bg=bg_col, command=clr, width=45, height=4)
clear_button.grid(row=5, column=1)
frame4.pack(expand=True)

# Main loop

root.mainloop()         
