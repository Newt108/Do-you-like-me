
import tkinter as tk
import random

def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Popup")
    label = tk.Label(popup, text="Thank you for accepting",font="1")
    label.pack(padx=20, pady=20)

def move_button(event):
    x = random.randint(0, 350)
    y = random.randint(0, 350)
    no_button.place(x=x, y=y)

root = tk.Tk()
root.title("Hazel")
root.geometry("400x400")

question_label = tk.Label(root, text ="Do you like me?", font="14")
question_label.pack(pady=20)

yes_button = tk.Button(root, text="Yes",font="4", command=show_popup)
yes_button.pack()

no_button = tk.Button(root, text="No",font="4")
no_button.pack()

no_button.bind("<Enter>", move_button)

root.mainloop()