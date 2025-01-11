import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold", bg="lightgray")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for i in range(4):
    for j in range(4):
        button = tk.Button(frame, text=buttons[i][j], font="lucida 15 bold", relief=tk.GROOVE, border=0)
        button.grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
        button.bind("<Button-1>", click)

root.mainloop()
