from tkinter import *
import math

def click(ch):
    entered_value=entry.get()
    anwer=""
    
    try:
        if ch=="C":
            entry.delete(len(entry.get())-1,END)
            return
        elif ch == "CE":
            entry.delete(0,END)
        elif ch == "√":
            anwer = math.sqrt(eval(entered_value))
        elif ch == "π":
            anwer = math.pi
        elif ch == "cosθ":
            anwer = math.cos(math.radians(eval(entered_value)))
        elif ch == "sinθ":
            anwer = math.sin(math.radians(eval(entered_value)))
        elif ch == "tanθ":
            anwer = math.tan(math.radians(eval(entered_value)))
        elif ch == "2π":
            anwer = 2 * math.pi
        elif ch == "cosh":
            anwer = math.cosh(eval(entered_value))
        elif ch == "sinh":
            anwer = math.sinh(eval(entered_value))
        elif ch == "tanh":
            anwer = math.tanh(eval(entered_value))
        elif ch == chr(0x221B):
            anwer = eval(entered_value) ** (1 / 3)
        elif ch == "x\u02b8":
            entry.insert("end", "**")
            return
        elif ch == "x\u00B3":
            anwer = eval(entered_value) ** 3
        elif ch == "x\u00B2":
            anwer = eval(entered_value) ** 2
        elif ch == "ln":
            anwer = math.log2(eval(entered_value))
        elif ch == "deg":
            anwer = math.degrees(eval(entered_value))
        elif ch == "rad":
            anwer = math.radians(eval(entered_value))
        elif ch == "entered_value":
            anwer = math.entered_value
        elif ch == "log10":
            anwer = math.log10(eval(entered_value))
        elif ch == "x!":
            anwer = math.factorial(eval(entered_value))
        elif ch == "=":
            anwer = eval(entered_value)

        else:
            entry.insert("end", ch)
            return

        entry.delete(0, "end")
        entry.insert(0, anwer)

    except SyntaxError:
        pass
window =Tk()
window.title("Anjali's Scientific Calculator")
window.geometry("680x486")
window.config(bg="dark grey")
icon=PhotoImage(file='logo.png')
window.iconphoto(True,icon)
entry =Entry(window, font=("arial", 20, "bold"), bg="black", fg="white", bd=10, width=44)
entry.grid(row=0, column=0, columnspan=8)
button_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ", "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
               "4", "5", "6", "*", chr(0x221B), "x\u02b8", "x\u00B3", "x\u00B2", "7", "8", "9","/", "ln", "deg",
               "rad", "entered_value", "0", ".", "%", "=", "log10", "(", ")", "x!"]
row = 1
column = 0
for i in button_list:
    button = Button(window, width=5, height=2, bd=2, text=i, bg="dark grey", fg="black",
                            font=("arial", 18, "bold"), command=lambda button=i: click(button))
    button.grid(row=row, column=column, pady=2)
    column += 1
    if column > 7:
        row += 1
        column = 0

window.mainloop()
