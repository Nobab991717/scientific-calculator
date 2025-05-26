import tkinter as tk
import math

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(screen.get()).replace("√", "math.sqrt").replace("π", "math.pi").replace("e", "math.e")))
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    elif text == "←":
        screen.set(screen.get()[:-1])
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Scientific Calculator")
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/", "sin", "cos"],
    ["4", "5", "6", "*", "tan", "log"],
    ["1", "2", "3", "-", "√", "π"],
    ["0", ".", "=", "+", "e", "C"],
    ["←"]
]

for row in buttons:
    frame = tk.Frame(root)
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", relief=tk.RIDGE, width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)
    frame.pack()

root.mainloop()
