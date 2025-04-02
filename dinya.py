import tkinter as tk
import random

def print_hello():
    print("привет")

def change_color(event=None):
    colors = ['blue', 'yellow', 'pink', 'red', 'orange', 'brown', 'black']
    root.configure(bg=random.choice(colors))

root = tk.Tk()
root.title("hello")
root.geometry("450x470")

label = tk.Label(root, text="I'm a glad to see you", font=('Arial', 14))
label.pack(pady=20)

hello_button = tk.Button(root, text="Print", command=print_hello, width=15, height=2)
hello_button.pack(pady=10)

button_1 = tk.Button(root, text="Exit", command=root.destroy, width=15, height=2)
button_1.pack(pady=10)

button_3 = tk.Button(root, text="Смена цвета", width=15, height=2)
button_3.pack(pady=10)

button_3.bind("<Button-1>", change_color)

root.mainloop()